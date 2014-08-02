'''
Created on 31-jul.-2014

@author: Simon
'''

import Image
import ImageTk

import Tkinter as tk
from python_runtime.statecharts_core import Event


class MvKWidget(tk.Widget):
    def __init__(self, controller, bindable=None, tagorid=None):
        if bindable is None:
            bindable = self
        self.bindable = bindable
        self.controller = controller
        self.id = tagorid or id(self)
        if isinstance(self, tk.Toplevel):
            self.protocol("WM_DELETE_WINDOW", self.window_close)
        if tagorid:
            self.bindable.tag_bind(tagorid, "<Button>", self.on_click)
            self.bindable.tag_bind(tagorid, "<ButtonRelease>", self.on_release)
            self.bindable.tag_bind(tagorid, "<Motion>", self.on_motion)
            self.bindable.tag_bind(tagorid, "<Enter>", self.on_enter)
            self.bindable.tag_bind(tagorid, "<Leave>", self.on_leave)
            self.bindable.tag_bind(tagorid, "<Key>", self.on_key)
        else:
            self.bindable.bind("<Button>", self.on_click)
            self.bindable.bind("<ButtonRelease>", self.on_release)
            self.bindable.bind("<Motion>", self.on_motion)
            self.bindable.bind("<Enter>", self.on_enter)
            self.bindable.bind("<Leave>", self.on_leave)
            self.bindable.bind("<Key>", self.on_key)
        self.controller.start()
        self.last_x = 50
        self.last_y = 50
        self.selected_type = None

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
            self.controller.addInput(Event(event_name, "input", [id(self)]))

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
            self.controller.addInput(Event(event_name, "input", [id(self)]))

    def on_motion(self, event):
        self.last_x = event.x
        self.last_y = event.y
        self.controller.addInput(Event("motion", "input", [id(self)]))

    def on_enter(self, event):
        self.bindable.focus_force()
        self.controller.addInput(Event("enter", "input", [id(self)]))

    def on_leave(self, event):
        self.controller.addInput(Event("leave", "input", [id(self)]))

    def on_key(self, event):
        event_name = None

        if event.keysym == 'Escape':
            event_name = "escape"
        elif event.keysym == 'Return':
            event_name = "return"
        elif event.keysym == 'Delete':
            event_name = "delete"
        elif event.keysym == 'Shift_L':
            event_name = "shift"

        if event_name:
            self.controller.addInput(Event(event_name, "input", [id(self)]))

    def on_key_release(self, event):
        event_name = None

        if event.keysym == 'Escape':
            event_name = "escape-release"
        elif event.keysym == 'Return':
            event_name = "return-release"
        elif event.keysym == 'Delete':
            event_name = "delete-release"
        elif event.keysym == 'Shift_L':
            event_name = "shift-release"

        if event_name:
            self.controller.addInput(Event(event_name, "input", [id(self)]))

    def window_close(self):
        self.controller.addInput(Event("window-close", "input", [id(self)]))


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


class Visual(object):
    def get_params(self):
        raise NotImplementedError()


class TextVisual(Visual):
    def __init__(self, text):
        super(TextVisual, self).__init__()
        self.text = text

    def get_params(self):
        return {'text': self.text}


class ImageVisual(Visual):
    def __init__(self, img_loc):
        super(ImageVisual, self).__init__()
        self.img = ImageTk.PhotoImage(Image.open(img_loc).resize((32, 32), Image.ANTIALIAS))

    def get_params(self):
        return {'image': self.img}


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.text = text

    def showtip(self):
        "Display text in tooltip window"
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + cx + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() - 20
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        try:
            # For Mac OS
            tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", tw._w,
                       "help", "noActivates")
        except tk.TclError:
            pass
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
