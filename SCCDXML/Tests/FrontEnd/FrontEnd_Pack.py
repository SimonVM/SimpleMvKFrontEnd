'''
Created on 24-jul.-2014

@author: Simon
'''

import time

import ImageTk, Image
import Tkinter as tk
from Tooltip import ToolTip
import button_controller
import frontend_controller
import browse_window_controller
from mvk.impl.python.constants import CreateConstants
from mvk.impl.python.datavalue import IntegerValue, MappingValue, LocationValue, StringValue
import mvk.interfaces.changelog
from mvk.mvk import MvK
from python_runtime.statecharts_core import Event


class DummyController:
    def addInput(self, inp):
        pass

    def start(self):
        pass

    def update(self, delta):
        pass


class MvKWidget(tk.Widget):
    def __init__(self, controller, bindable=None):
        if bindable is None:
            bindable = self
        if controller is None:
            controller = DummyController()
        self.bindable = bindable
        self.controller = controller
        self.bindable.bind("<Button>", self.on_click)
        self.bindable.bind("<ButtonRelease>", self.on_release)
        self.bindable.bind("<Motion>", self.on_motion)
        self.bindable.bind("<Enter>", self.on_enter)
        self.bindable.bind("<Leave>", self.on_leave)
        self.bindable.bind("<Key>", self.on_key)
        self.bindable.bind("<KeyRelease>", self.on_key_release)
        self.controller.start()
        self.last_x = 0
        self.last_y = 0

    def on_click(self, event):
        event_name = None

        if event.num == 1:
            event_name = "left-click"
        elif event.num == 2:
            event_name = "middle-click"
        elif event.num == 3:
            event_name = "right-click"

        if event_name:
            self.last_x = event.x
            self.last_y = event.y
            self.controller.addInput(Event(event_name, "input"))

    def on_release(self, event):
        event_name = None

        if event.num == 1:
            event_name = "left-release"
        elif event.num == 2:
            event_name = "middle-release"
        elif event.num == 3:
            event_name = "right-release"

        if event_name:
            self.last_x = event.x
            self.last_y = event.y
            self.controller.addInput(Event(event_name, "input"))

    def on_motion(self, event):
        self.last_x = event.x
        self.last_y = event.y
        self.controller.addInput(Event("motion", "input"))

    def on_enter(self, event):
        self.bindable.focus_force()
        self.controller.addInput(Event("enter", "input"))

    def on_leave(self, event):
        self.controller.addInput(Event("leave", "input"))

    def on_key(self, event):
        event_name = None
        print self.__class__.__name__, event.keysym

        if event.keysym == 'Escape':
            event_name = "escape"
        elif event.keysym == 'Return':
            event_name = "return"
        elif event.keysym == 'Delete':
            event_name = "delete"
        elif event.keysym == 'Shift_L':
            event_name = "shift"

        if event_name:
            self.controller.addInput(Event(event_name, "input"))

    def on_key_release(self, event):
        event_name = None
        print self.__class__.__name__, event.keysym

        if event.keysym == 'Escape':
            event_name = "escape-release"
        elif event.keysym == 'Return':
            event_name = "return-release"
        elif event.keysym == 'Delete':
            event_name = "delete-release"
        elif event.keysym == 'Shift_L':
            event_name = "shift-release"

        if event_name:
            self.controller.addInput(Event(event_name, "input"))

    def update_widget(self, delta):
        self.controller.update(delta)


class Button(tk.Button, MvKWidget):
    def __init__(self, tooltip_text=None, master=None, command=None, cnf={}, **kw):
        tk.Button.__init__(self, master=master, cnf=cnf, **kw)
        MvKWidget.__init__(self, button_controller.Controller(self), None)
        self.tooltip = ToolTip(self, tooltip_text)
        self.command = command

    def show_tooltip(self):
        self.tooltip.showtip()

    def hide_tooltip(self):
        self.tooltip.hidetip()

    def pressed(self):
        if self.command:
            self.command()


class HorizontalScrolledFrame(tk.Frame):
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a horizontal scrollbar for scrolling it
        hscrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        hscrollbar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                                xscrollcommand=hscrollbar.set, height=78)
        self.canvas.pack(side=tk.LEFT, fill=tk.X, expand=tk.TRUE)

        hscrollbar.config(command=self.canvas.xview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = tk.Frame(self.canvas)
        self.canvas.create_window(0, 0, window=interior, anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            self.canvas.config(scrollregion="0 0 %s %s" % size)

        interior.bind('<Configure>', _configure_interior)


class ToolbarFrame(HorizontalScrolledFrame):
    INTER_SPACING = 5

    def __init__(self, master=None, cnf={}, **kw):
        HorizontalScrolledFrame.__init__(self, parent=master, cnf=cnf, **kw)

        self.toolbars = {}

    def create_toolbar(self, name):
        toolbar = Toolbar(name, self, self.interior)
        toolbar.pack(side=tk.LEFT, fill=tk.Y, padx=self.INTER_SPACING, pady=self.INTER_SPACING)

        self.toolbars[name] = toolbar
        return toolbar


class Toolbar(tk.Frame):
    PADDING = 2

    def __init__(self, name, toolbar_frame, master=None, cnf={}, **kw):
        tk.Frame.__init__(self, master=master, cnf=cnf, **kw)

        self.config(relief=tk.RAISED, bd=1)
        tk.Label(self, text=name).pack(side=tk.TOP, pady=5)
        self.toolbar_frame = toolbar_frame
        self.buttons = []

    def create_button(self, visual, tooltip=None, command=lambda master: None):
        new_button = None
        if isinstance(visual, str):
            new_button = Button(tooltip, self, command=command, text=visual)
            new_button.pack(side=tk.LEFT, fill=tk.Y, padx=self.PADDING)
        elif isinstance(visual, ImageTk.PhotoImage):
            new_button = Button(tooltip, self, command=command, image=visual)
            new_button.pack(side=tk.LEFT, fill=tk.Y, padx=self.PADDING)
            new_button.image = visual
        else:
            raise Exception('Can only create buttons with string or image visual.')
        self.buttons.append(new_button)

    def update_widget(self, delta):
        for b in self.buttons:
            b.update_widget(delta)


class BrowseWindow(tk.Toplevel, MvKWidget):
    def __init__(self, custom_filter=lambda x: True, master=None, cnf={}, **kw):
        tk.Toplevel.__init__(self, master=master, cnf=cnf, **kw)

        self.listbox = tk.Listbox(self)
        self.custom_filter = custom_filter

        MvKWidget.__init__(self, browse_window_controller.Controller(self), self.listbox)

        self.transient(master)
        self.grab_set()
        self.curr_package = MvK().read(LocationValue('')).get_item()

        back_icon_img = ImageTk.PhotoImage(Image.open("icons/back-icon.png").resize((32, 32), Image.ANTIALIAS))
        self.back_button = Button("Go up one level.", self, lambda master=self: self.up_level(), image=back_icon_img)
        self.back_button.pack(side=tk.TOP, fill=tk.Y)
        self.back_button.image = back_icon_img

        self.listbox.pack()

        self.select_button = Button("Select this model.", self, lambda master=self: self.select_model, text="SELECT")
        self.select_button.pack(side=tk.TOP, fill=tk.Y)

        self.populate_window()

    def populate_window(self):
        self.listbox.delete(0, tk.END)
        el_it = self.curr_package.get_elements().__iter__()
        while el_it.has_next():
            next_el = self.curr_package.get_element(el_it.next())
            if isinstance(next_el, mvk.interfaces.object.Package):
                if isinstance(next_el, mvk.interfaces.object.Model):
                    if next_el.get_potency() > IntegerValue(0):
                        self.listbox.insert(tk.END, str(next_el.get_name()))
                else:
                    self.listbox.insert(tk.END, str(next_el.get_name()))

    def new_level(self):
        self.curr_package = self.curr_package.get_element(StringValue(self.listbox.get(tk.ACTIVE)))
        self.populate_window()

    def up_level(self):
        if self.curr_package.get_parent():
            self.curr_package = self.curr_package.get_parent()
            self.populate_window()
        else:
            self.curr_package = self.mvk.read(LocationValue('')).get_item()
            self.populate_window()

    def select_entry(self):
        self.listbox.activate(self.listbox.nearest(self.last_y))

    def select_model(self):
        try:
            m = self.curr_package.get_element(StringValue(self.listbox.get(tk.ACTIVE)))
            if (isinstance(m, mvk.interfaces.object.Model) and self.custom_filter(m)):
                self.ret_val = m
                self.destroy()
        except mvk.interfaces.exception.MvKKeyError:
            return

        self.populate_window()

    def get_selection(self):
        return self.ret_val

    def update_widget(self, delta):
        self.back_button.update_widget(delta)
        self.select_button.update_widget(delta)


class FrontEnd(tk.Tk, MvKWidget):
    def __init__(self):
        tk.Tk.__init__(self)
        self.widgets = []
        self.setup_gui()
        MvKWidget.__init__(self, frontend_controller.Controller(self), self.c)
        self.fixed_update_time = 20  # milliseconds
        '''
        self.schedule_time = time.time()
        self.scheduled_update_id = self.after(self.fixed_update_time, self.update_widget)
        '''
        self.update_widget()
        self.selected_type = None

    def setup_gui(self):
        self.title('MvKFrontEnd')
        self.maxsize(self.winfo_screenwidth() - 15, self.winfo_screenheight() - 15)

        self.toolbar_frame = ToolbarFrame(master=self)
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X, expand=0)

        main_toolbar = self.toolbar_frame.create_toolbar('Main')
        main_toolbar.create_button(ImageTk.PhotoImage(Image.open("icons/new-icon.png").resize((32, 32), Image.ANTIALIAS)),
                                   "Create a New Model", lambda master=self: master.new_model())
        main_toolbar.create_button(ImageTk.PhotoImage(Image.open("icons/load-type-model.png").resize((32, 32), Image.ANTIALIAS)),
                                   "Load a Type Model", lambda master=self: master.load_type_model())
        main_toolbar.create_button(ImageTk.PhotoImage(Image.open("icons/open-icon.png").resize((32, 32), Image.ANTIALIAS)),
                                   "Open a Model", lambda master=self: master.open_model())
        main_toolbar.create_button(ImageTk.PhotoImage(Image.open("icons/save-icon.png").resize((32, 32), Image.ANTIALIAS)),
                                   "Save the Modelverse", lambda master=self: master.save())
        main_toolbar.create_button(ImageTk.PhotoImage(Image.open("icons/undo-icon.png").resize((32, 32), Image.ANTIALIAS)),
                                   "Undo", lambda master=self: master.undo())
        main_toolbar.create_button(ImageTk.PhotoImage(Image.open("icons/redo-icon.png").resize((32, 32), Image.ANTIALIAS)),
                                   "Redo", lambda master=self: master.redo())
        main_toolbar.create_button(ImageTk.PhotoImage(Image.open("icons/record-icon.png").resize((32, 32), Image.ANTIALIAS)),
                                   "Record All Actions", lambda master=self: master.record())
        main_toolbar.create_button("RAMify", "RAMify Current Model", lambda master=self: master.ramify())

        self.widgets.append(main_toolbar)

        self.__gridLineSeperation = 20
        self.__gridLineColor = '#c8c8c8'
        self.__gridWidth = 1

        self.__gridSubdivisions = 5
        self.__gridLineSubdivisionColor = '#e8e8e8'
        self.__gridSubdivisionShow = True
        self.__gridSubdivisionWidth = 1

        CANVAS_SIZE_TUPLE = (0, 0, self.winfo_screenwidth() * 2, self.winfo_screenheight() * 2)
        self.c = tk.Canvas(self, relief=tk.RIDGE, scrollregion=CANVAS_SIZE_TUPLE)
        self.c.focus_force()

        def on_mousewheel(event):
            self.c.yview_scroll(-1 * (event.delta / 120), "units")

        ''' TODO: Also make toolbar frame scrollable. Maybe using Statecharts this is possible. '''
        self.bind_all("<MouseWheel>", on_mousewheel)

        vbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vbar.config(command=self.c.yview)
        vbar.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 16))

        hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        hbar.config(command=self.c.xview)
        hbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.c.config(background='white', yscrollcommand=vbar.set, xscrollcommand=hbar.set)
        self.c.pack(expand=True, fill=tk.BOTH)

        self.clear()

    def clear(self):
        CANVAS_SIZE_TUPLE = (0, 0, self.winfo_screenwidth() * 2, self.winfo_screenheight() * 2)
        self.c.delete("all")
        subdivisionSeperation = self.__gridLineSeperation * self.__gridSubdivisions
        for x in range(CANVAS_SIZE_TUPLE[0], CANVAS_SIZE_TUPLE[2], subdivisionSeperation):
            self.c.create_line(x, 0, x, CANVAS_SIZE_TUPLE[3], width=self.__gridSubdivisionWidth, fill=self.__gridLineSubdivisionColor)

        for y in range(CANVAS_SIZE_TUPLE[1], CANVAS_SIZE_TUPLE[3], subdivisionSeperation):
            self.c.create_line(0, y, CANVAS_SIZE_TUPLE[2], y, width=self.__gridSubdivisionWidth, fill=self.__gridLineSubdivisionColor)

        for x in range(CANVAS_SIZE_TUPLE[0], CANVAS_SIZE_TUPLE[2], self.__gridLineSeperation):
            for y in range(CANVAS_SIZE_TUPLE[1], CANVAS_SIZE_TUPLE[3], self.__gridLineSeperation):
                self.c.create_oval(x - self.__gridWidth, y - self.__gridWidth, x + self.__gridWidth, y + self.__gridWidth, width=0, fill=self.__gridLineColor)

    def update_widget(self):
        self.controller.update(self.fixed_update_time / 1000.0)
        for w in self.widgets:
            w.update_widget(self.fixed_update_time / 1000.0)
        # self.schedule_time = time.time()
        self.scheduled_update_id = self.after(self.fixed_update_time, self.update_widget)

    def create_instance(self):
        pass

    def open_browse_window(self, custom_filter=lambda x: True):
        self.ret_val = None

        browse_window = BrowseWindow(custom_filter, self)
        self.wait_window(browse_window)

        return browse_window.get_selection()

    def new_model(self):
        selected_tm = self.open_browse_window(custom_filter=lambda x: x.get_potency() > IntegerValue(0))

        if selected_tm:
            attrs = self.open_attribute_window(selected_tm)
            if 'location' in attrs:
                loc = attrs['location']
                del attrs['location']

                attrs = MappingValue({CreateConstants.LOCATION_KEY: loc,
                                      CreateConstants.TYPE_KEY: selected_tm.get_location(),
                                      CreateConstants.ATTRS_KEY: MappingValue(attrs)})

                cl = self.apply_operation('create', attrs)

                self.model_location = None
                if isinstance(cl, mvk.interfaces.changelog.MvKCompositeLog):
                    cls_iter = cl.get_logs().__iter__()
                    while cls_iter.has_next():
                        next_cl = cls_iter.next()
                        if next_cl[CreateConstants.TYPE_KEY] == LocationValue('mvk.object.Model'):
                            attr_it = next_cl[CreateConstants.ATTRS_KEY].__iter__()
                            while attr_it.has_next():
                                next_attr = attr_it.next()
                                if next_attr[StringValue('name')] == StringValue('name'):
                                    self.model_location = next_cl[CreateConstants.LOCATION_KEY] + StringValue('.') + next_attr[StringValue('value')]
                else:
                    attr_it = cl[CreateConstants.ATTRS_KEY].__iter__()
                    while attr_it.has_next():
                        next_attr = attr_it.next()
                        if next_attr[StringValue('name')] == StringValue('name'):
                            self.model_location = cl[CreateConstants.LOCATION_KEY] + StringValue('.') + next_attr[StringValue('value')]

                assert self.model_location

                self.clear_canvas()
                self.populate_toolbar(selected_tm)

    def load_type_model(self):
        pass

    def open_model(self):
        pass

    def save(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass

    def record(self):
        pass

    def ramify(self):
        pass

if __name__ == '__main__':
    t = FrontEnd()
    t.mainloop()
