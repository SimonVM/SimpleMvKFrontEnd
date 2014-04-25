'''
Created on 10-apr.-2014

@author: Simon
'''
from Tkinter import *

from PIL import ImageTk, Image
from Tooltip import createToolTip
from mvk.impl.python.constants import CreateConstants, CRUDConstants
from mvk.impl.python.datatype import TypeFactory
from mvk.impl.python.datavalue import AnyValue, BooleanValue, DataValueFactory, EnumValue, FloatValue, LocationValue, StringValue, IntegerValue, MappingValue, \
ImmutableMappingValue, ImmutableSequenceValue, ImmutableSetValue, InfiniteValue, SequenceValue, SetValue, TupleValue, VoidValue
import mvk.interfaces.object
from mvk.mvk import MvK
from mvk.plugins.transformation.mt import ramify_scd


class Application(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, master=master, cnf=cnf, **kw)
        self.mvk = MvK()
        self.mvk.restore(StringValue('protected'))
        self.tm_buttons = []
        self.tm_frames = []
        self.types = []
        self.text_ids = {}
        self.instances = {}
        self.widget_ids = {}
        self.record_on = True
        self.fname = 'record.txt'
        open(self.fname, 'wb').close()
        self.model_location = None
        self.selected_type = None
        self.selected_instance = None
        self.pack()
        self.create_widgets()
        master.focus_force()

    def open_browse_window(self, custom_filter=lambda x: True):
        self.ret_val = None

        browse_window = Toplevel()
        browse_window.transient(root)
        browse_window.grab_set()

        listbox = Listbox(browse_window)

        self.curr_package = self.mvk.read(LocationValue('')).get_item()

        def populate_window():
            listbox.delete(0, END)
            el_it = self.curr_package.get_elements().__iter__()
            while el_it.has_next():
                next_el = self.curr_package.get_element(el_it.next())
                if isinstance(next_el, mvk.interfaces.object.Package):
                    if isinstance(next_el, mvk.interfaces.object.Model):
                        if next_el.get_potency() > IntegerValue(0):
                            listbox.insert(END, str(next_el.get_name()))
                    else:
                        listbox.insert(END, str(next_el.get_name()))

            def new_level(name):
                self.curr_package = self.curr_package.get_element(name)
                populate_window()
            listbox.bind("<Double-Button-1>", lambda event: new_level(StringValue(listbox.get(ACTIVE))))

        def up_level():
            if self.curr_package.get_parent():
                self.curr_package = self.curr_package.get_parent()
                populate_window()
            else:
                self.curr_package = self.mvk.read(LocationValue('')).get_item()
                populate_window()

        back_icon_img = ImageTk.PhotoImage(Image.open("icons/back-icon.png").resize((32, 32), Image.ANTIALIAS))
        back_button = Button(browse_window, image=back_icon_img, command=up_level)
        back_button.pack(side=TOP, fill=Y)
        back_button.image = back_icon_img
        createToolTip(back_button, "Go up one level.")

        listbox.pack()

        def select_model():
            try:
                m = self.curr_package.get_element(StringValue(listbox.get(ACTIVE)))
                if (isinstance(m, mvk.interfaces.object.Model) and custom_filter(m)):
                    self.ret_val = m
                    browse_window.destroy()
            except mvk.interfaces.exception.MvKKeyError:
                return

        select_button = Button(browse_window, text="SELECT", command=select_model)
        select_button.pack(side=TOP, fill=Y)
        createToolTip(select_button, "Select this model.")

        populate_window()

        root.wait_window(browse_window)

        return self.ret_val

    def clear_toolbar(self):
        for g in self.tm_frames:
            g.destroy()
        del self.tm_buttons[:]
        del self.tm_frames[:]
        del self.types[:]

    def select_type(self, i):
        self.selected_type = self.types[i]

    def populate_toolbar(self, tm, append=False):
        if not append:
            self.clear_toolbar()
            self.types = []
        tm_frame = Frame(self.toolbar_canvas)
        tm_frame.config(height=64, bd=1, relief=RAISED)
        tm_frame.pack(side=LEFT, fill=Y)
        self.tm_frames.append(tm_frame)
        Label(tm_frame, text=str(tm.get_name())).pack(side=TOP, pady=5)
        el_it = tm.get_elements().__iter__()
        while el_it.has_next():
            next_el = tm.get_element(el_it.next())
            if isinstance(next_el, mvk.interfaces.object.Clabject) and (not isinstance(next_el, mvk.interfaces.object.Composition)) and next_el.get_potency() > IntegerValue(0) and not next_el.is_abstract():
                i = len(self.types)
                self.types.append(next_el)
                new_button = Button(tm_frame, text=next_el.get_name(), command=lambda x=i: self.select_type(x))
                new_button.pack(side=LEFT, fill=Y, padx=5)
                createToolTip(new_button, "Create a %s." % next_el.get_name())
                self.tm_buttons.append(new_button)

    def open_attribute_window(self, node):
        self.ret_val = {}

        attr_window = Toplevel()
        attr_window.transient(root)
        attr_window.grab_set()

        attr_widgets = {}

        if isinstance(node, mvk.interfaces.object.Model):
            attr_frame = Frame(attr_window)
            attr_frame.pack(side=TOP, pady=5)
            Label(attr_frame, text=str('Location: ')).pack(side=LEFT)
            e = Entry(attr_frame)
            e.insert(0, '')
            e.pack(side=LEFT)
            attr_widgets[('location', LocationValue)] = e

        if isinstance(node, mvk.interfaces.object.Association):
            for endpoint in [node.get_from_multiplicity(), node.get_to_multiplicity()]:
                attr_frame = Frame(attr_window)
                attr_frame.pack(side=TOP, pady=5)
                Label(attr_frame, text=str(endpoint.get_port_name())).pack(side=LEFT)
                e = Entry(attr_frame)
                e.insert(0, '')
                e.pack(side=LEFT)
                attr_widgets[(endpoint.get_port_name(), LocationValue)] = e

        attr_it = (node.get_all_attributes() if isinstance(node, mvk.interfaces.object.Clabject) else node.get_attributes()).__iter__()
        while attr_it.has_next():
            next_attr = attr_it.next()
            if next_attr.get_potency() > IntegerValue(0):
                attr_frame = Frame(attr_window)
                attr_frame.pack(side=TOP, pady=5)
                Label(attr_frame, text=str(next_attr.get_short_location()) + ': ').pack(side=LEFT)
                e = Entry(attr_frame)
                e.insert(0, str(next_attr.get_default()))
                e.pack(side=LEFT)
                attr_widgets[(next_attr.get_short_location(), next_attr.get_default().__class__)] = e

        def compute_attrs():
            for k, v in attr_widgets.iteritems():
                val = v.get()
                if val.find('Value(') != -1 or val.find('Type(') != -1:
                    val = eval(val)
                if isinstance(val, mvk.interfaces.element.Element):
                    self.ret_val[k[0]] = val
                elif issubclass(k[1], mvk.interfaces.datavalue.DataValue):
                    self.ret_val[k[0]] = DataValueFactory.create_instance(v.get(), k[1])
                else:
                    self.ret_val[k[0]] = TypeFactory.get_type(v.get())
            attr_window.destroy()

        ok_button = Button(attr_window, text="OK", command=compute_attrs)
        ok_button.pack(side=TOP, fill=Y)
        createToolTip(ok_button, "Create.")

        root.wait_window(attr_window)

        return self.ret_val

    def open_attribute_window_instance(self, node):
        self.ret_val = {}

        attr_window = Toplevel()
        attr_window.transient(root)
        attr_window.grab_set()

        attr_widgets = {}

        attr_it = (node.get_all_attributes() if isinstance(node, mvk.interfaces.object.Clabject) else node.get_attributes()).__iter__()
        while attr_it.has_next():
            next_attr = attr_it.next()
            if next_attr.get_potency() == IntegerValue(0):
                attr_frame = Frame(attr_window)
                attr_frame.pack(side=TOP, pady=5)
                Label(attr_frame, text=str(next_attr.get_name()) + ': ').pack(side=LEFT)
                e = Entry(attr_frame)
                e.insert(0, str(next_attr.get_value()))
                e.pack(side=LEFT)
                attr_widgets[(next_attr.get_name(), next_attr.get_value().__class__)] = e

        def insert_child(children, assoc, node):
            l = children[assoc.get_name()]
            l.insert(END, str(node.get_name()))

        assoc_it = node.typed_by().get_out_associations().__iter__()
        children = {}
        while assoc_it.has_next():
            next_assoc = assoc_it.next()
            if isinstance(next_assoc, mvk.interfaces.object.Composition) and next_assoc.get_potency() > IntegerValue(0):
                def create_child(the_type, assoc_type, parent_loc, children):
                    cl = self.create_instance_composition(the_type, parent_loc)
                    if cl and cl.is_success():
                        attr_it = cl[CreateConstants.ATTRS_KEY].__iter__()
                        while attr_it.has_next():
                            next_attr = attr_it.next()
                            if next_attr[StringValue('name')] == StringValue('name'):
                                instance_location = cl[CreateConstants.LOCATION_KEY] + StringValue('.') + next_attr[StringValue('value')]
                        insert_child(children, assoc_type, self.mvk.read(instance_location).get_item())

                assoc_button = Button(attr_window, text=str('Add %s (%s)' % (next_assoc.get_to_multiplicity().get_node().get_name(),
                                                                             next_assoc.get_name())),
                                      command=lambda the_type=next_assoc.get_to_multiplicity().get_node().get_location(), assoc_type=next_assoc, parent_loc=node.get_location(), children=children: create_child(the_type, assoc_type, parent_loc, children))
                assoc_button.pack(side=TOP, pady=5)
                child_frame = Frame(attr_window)
                child_frame.pack(side=TOP, pady=5)
                Label(child_frame, text=str(next_assoc.get_name()) + ': ').pack(side=TOP)
                l = Listbox(child_frame)
                l.pack(side=TOP)
                children[next_assoc.get_name()] = l

                def delete_child(list_box):
                    self.delete(node.get_location() + StringValue('.') + StringValue(l.get(ACTIVE)))
                    list_box.delete(ACTIVE)

                l.bind("<Delete>", lambda event, lb=l: delete_child(lb))

        assoc_it = node.get_out_associations().__iter__()
        while assoc_it.has_next():
            next_assoc = assoc_it.next()
            if isinstance(next_assoc, mvk.interfaces.object.Composition) and next_assoc.get_potency() == IntegerValue(0):
                insert_child(children, next_assoc.typed_by(), next_assoc.get_to_multiplicity().get_node())

        def compute_attrs():
            for k, v in attr_widgets.iteritems():
                new_val = DataValueFactory.create_instance(v.get(), k[1])
                if new_val != node.get_attribute(k[0]).get_value():
                    self.ret_val[k[0]] = new_val
            attr_window.destroy()

        ok_button = Button(attr_window, text="OK", command=compute_attrs)
        ok_button.pack(side=TOP, fill=Y)
        createToolTip(ok_button, "Create.")

        root.wait_window(attr_window)

        return self.ret_val

    def apply_operation(self, op, attrs):
        if self.record_on:
            with open(self.fname, 'ab') as f:
                if op == 'create' or op == 'update':
                    attr_it = attrs[CreateConstants.ATTRS_KEY].__iter__()
                    attrs_for_str = []
                    while attr_it.has_next():
                        k = attr_it.next()
                        v = attrs[CreateConstants.ATTRS_KEY][k]
                        fix = '\'' if isinstance(v, StringValue) else ''
                        attrs_for_str.append('StringValue(\'%s\'): %s(%s)' % (str(k), v.__class__.__name__, '' if v is None or isinstance(v, mvk.interfaces.datatype.DataType) else fix + str(v) + fix))
                    attrs_str = ', '.join(attrs_for_str)
                    f.write('self.mvk.%s(%s)\n' % (op, 'MappingValue(CreateConstants.LOCATION_KEY: LocationValue(\'%s\'), \
                                                                     CreateConstants.TYPE_KEY: LocationValue(\'%s\'), \
                                                                     CreateConstants.ATTRS_KEY: MappingValue({%s})' % (str(attrs[CRUDConstants.LOCATION_KEY]),
                                                                                                                       str(attrs[CRUDConstants.TYPE_KEY]),
                                                                                                                       attrs_str)
                                                   )
                            )
                else:
                    f.write('self.mvk.%s(LocationValue(%s))' % (op, '\'' + attrs + '\''))
        return eval('self.mvk.%s(attrs)' % op)

    def create_instance(self, event=None, the_type=None, loc=None):
        if not the_type:
            the_type = self.selected_type
        if the_type:
            attrs = self.open_attribute_window(the_type)

            if len(attrs) > 0:
                attrs = MappingValue({CreateConstants.LOCATION_KEY: self.model_location if loc is None else loc,
                                      CreateConstants.TYPE_KEY: the_type.get_location(),
                                      CreateConstants.ATTRS_KEY: MappingValue(attrs)})

                cl = self.apply_operation('create', attrs)
                if not cl.is_success():
                    print cl
                    return cl

                if event:
                    instance_location = None
                    if isinstance(cl, mvk.interfaces.changelog.MvKCompositeLog):
                        cls_iter = cl.get_logs().__iter__()
                        found = False
                        while cls_iter.has_next() and not found:
                            next_cl = cls_iter.next()
                            attr_it = next_cl[CreateConstants.ATTRS_KEY].__iter__()
                            while attr_it.has_next():
                                next_attr = attr_it.next()
                                if next_attr[StringValue('name')] == StringValue('name'):
                                    instance_location = next_cl[CreateConstants.LOCATION_KEY] + StringValue('.') + next_attr[StringValue('value')]
                                if next_attr[StringValue('name')] == StringValue('class') and next_attr[StringValue('value')] == the_type.get_location():
                                    found = True
                    else:
                        attr_it = cl[CreateConstants.ATTRS_KEY].__iter__()
                        while attr_it.has_next():
                            next_attr = attr_it.next()
                            if next_attr[StringValue('name')] == StringValue('name'):
                                instance_location = cl[CreateConstants.LOCATION_KEY] + StringValue('.') + next_attr[StringValue('value')]

                    new_instance = self.mvk.read(instance_location).get_item()

                    if isinstance(new_instance, mvk.interfaces.object.Association):
                        from_w = self.widget_ids[new_instance.get_from_multiplicity().get_node().get_name()]
                        to_w = self.widget_ids[new_instance.get_to_multiplicity().get_node().get_name()]
                        f_coords = self.c.coords(from_w)
                        t_coords = self.c.coords(to_w)
                        self.c.create_line(f_coords[0] + 50, f_coords[1], t_coords[0] + 50, t_coords[1], arrow="last", tags=("to_%s" % new_instance.get_to_multiplicity().get_node().get_name(),
                                                                                                                             "from_%s" % new_instance.get_from_multiplicity().get_node().get_name()))
                    else:
                        x = self.c.canvasx(event.x)
                        y = self.c.canvasy(event.y)
                        new_id = self.c.create_rectangle(x, y, x + 200, y + 30, fill='ghost white')
                        text_id = self.c.create_text(x + 100, y + 15, text=str(new_instance.get_name()) + ': ' + str(new_instance.typed_by().get_name()))
                        self.text_ids[new_id] = text_id

                        self.instances[new_id] = new_instance
                        self.widget_ids[new_instance.get_name()] = new_id

                        def on_click(event, item_id):
                            self.old_coords = (self.c.canvasx(event.x), self.c.canvasy(event.y))
                            if self.selected_instance and self.selected_instance != item_id:
                                self.deselect()
                            self.selected_instance = item_id
                            self.c.itemconfig(item_id, fill="yellow")

                        def on_release(event, item_id):
                            deltax = self.c.canvasx(event.x) - self.old_coords[0]
                            deltay = self.c.canvasy(event.y) - self.old_coords[1]
                            self.c.move(item_id, deltax, deltay)
                            self.c.move(self.text_ids[item_id], self.c.canvasx(event.x) - self.old_coords[0], self.c.canvasy(event.y) - self.old_coords[1])
                            handles = self.c.find_withtag("from_%s" % self.instances[item_id].get_name())
                            for h in handles:
                                coords = self.c.coords(h)
                                coords[0] += deltax
                                coords[1] += deltay
                                self.c.coords(h, *coords)
                            handles = self.c.find_withtag("to_%s" % self.instances[item_id].get_name())
                            for h in handles:
                                coords = self.c.coords(h)
                                coords[2] += deltax
                                coords[3] += deltay
                                self.c.coords(h, *coords)
                            self.old_coords = (self.c.canvasx(event.x), self.c.canvasy(event.y))

                        def edit_item(event, item_id):
                            item = self.instances[item_id]
                            attrs = self.open_attribute_window_instance(item)

                            if len(attrs) > 0:
                                attrs = MappingValue({CreateConstants.LOCATION_KEY: item.get_location(),
                                                      CreateConstants.TYPE_KEY: item.typed_by().get_location(),
                                                      CreateConstants.ATTRS_KEY: MappingValue(attrs)})
                                self.apply_operation('update', attrs)
                                self.c.itemconfig(self.text_ids[item_id], text=str(item.get_name()) + ': ' + str(item.typed_by().get_name()))

                        self.c.tag_bind(new_id, '<ButtonPress-1>', lambda event, item_id=new_id: on_click(event, item_id))
                        self.c.tag_bind(new_id, '<B1-Motion>', lambda event, item_id=new_id: on_release(event, item_id))
                        self.c.tag_bind(new_id, '<ButtonRelease-1>', lambda event, item_id=new_id: on_release(event, item_id))
                        self.c.tag_bind(new_id, '<ButtonPress-2>', lambda event, item_id=new_id: edit_item(event, item_id))

                return cl

    def deselect(self, event=None):
        if self.selected_instance:
            self.c.itemconfig(self.selected_instance, fill="ghost white")

    def create_instance_composition(self, the_type, parent_loc):
        return self.create_instance(None, self.mvk.read(the_type).get_item(), parent_loc)

    def create_model(self):
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
        selected_tm = self.open_browse_window(custom_filter=lambda x: x.get_potency() > IntegerValue(0))
        self.populate_toolbar(selected_tm, append=True)

    def open_model(self):
        pass

    def record(self):
        self.record_on = True

    def delete(self, loc=None):
        if loc:
            self.apply_operation('delete', loc)
        else:
            self.apply_operation('delete', self.instances[self.selected_instance].get_location())
            self.c.delete(self.selected_instance)
            self.c.delete(self.text_ids[self.selected_instance])
            self.selected_instance = None

    def ramify(self):
        print ramify_scd(self.model_location)

    def clear_canvas(self):
        CANVAS_SIZE_TUPLE = (0, 0, self.master.winfo_screenwidth() * 2, self.master.winfo_screenheight() * 2)
        self.c.delete("all")
        subdivisionSeperation = self.__gridLineSeperation * self.__gridSubdivisions
        for x in range(CANVAS_SIZE_TUPLE[0], CANVAS_SIZE_TUPLE[2], subdivisionSeperation):
            self.c.create_line(x, 0, x, CANVAS_SIZE_TUPLE[3], width=self.__gridSubdivisionWidth, fill=self.__gridLineSubdivisionColor)

        for y in range(CANVAS_SIZE_TUPLE[1], CANVAS_SIZE_TUPLE[3], subdivisionSeperation):
            self.c.create_line(0, y, CANVAS_SIZE_TUPLE[2], y, width=self.__gridSubdivisionWidth, fill=self.__gridLineSubdivisionColor)

        for x in range(CANVAS_SIZE_TUPLE[0], CANVAS_SIZE_TUPLE[2], self.__gridLineSeperation):
            for y in range(CANVAS_SIZE_TUPLE[1], CANVAS_SIZE_TUPLE[3], self.__gridLineSeperation):
                self.c.create_oval(x - self.__gridWidth, y - self.__gridWidth, x + self.__gridWidth, y + self.__gridWidth, width=0, fill=self.__gridLineColor)

    def save(self):
        self.mvk.backup(StringValue('protected'))

    def create_widgets(self):
        CANVAS_SIZE_TUPLE = (0, 0, self.master.winfo_screenwidth() * 2, self.master.winfo_screenheight() * 2)

        self.toolbar_frame = Frame(master=self)
        self.toolbar_bottom_frame = Frame(self.toolbar_frame)
        self.toolbar_canvas = Canvas(master=self.toolbar_frame,
                                     takefocus=1,
                                     scrollregion=(0, 0, self.master.winfo_screenwidth() * 2, 0))

        self.toolbar_canvas.square = Canvas(self.toolbar_bottom_frame, width=16, height=16)

        self.toolbar = Frame(self.toolbar_canvas)
        self.toolbar_canvas_handler = self.toolbar_canvas.create_window(0, 0, window=self.toolbar, anchor=NW)

        new_icon_img = ImageTk.PhotoImage(Image.open("icons/new-icon.png").resize((64, 64), Image.ANTIALIAS))
        self.new_button = Button(self.toolbar_canvas, image=new_icon_img, command=self.create_model)
        self.new_button.pack(side=LEFT, fill=Y, padx=5)
        self.new_button.image = new_icon_img
        createToolTip(self.new_button, "Create a new model.")

        load_mm_icon_img = ImageTk.PhotoImage(Image.open("icons/load-mm-icon.png").resize((64, 64), Image.ANTIALIAS))
        self.load_mm_button = Button(self.toolbar_canvas, image=load_mm_icon_img, command=self.load_type_model)
        self.load_mm_button.pack(side=LEFT, fill=Y, padx=5)
        self.load_mm_button.image = load_mm_icon_img
        createToolTip(self.load_mm_button, "Load a type model.")

        open_icon_img = ImageTk.PhotoImage(Image.open("icons/open-icon.png").resize((64, 64), Image.ANTIALIAS))
        self.open_button = Button(self.toolbar_canvas, image=open_icon_img, command=self.open_model)
        self.open_button.pack(side=LEFT, fill=Y, padx=5)
        self.open_button.image = open_icon_img
        createToolTip(self.open_button, "Load a model.")

        self.ramify_button = Button(self.toolbar_canvas, text="RAMIFY", command=self.ramify)
        self.ramify_button.pack(side=LEFT, fill=Y, padx=5)
        self.ramify_button.image = open_icon_img
        createToolTip(self.ramify_button, "Ramify current model.")

        record_icon_img = ImageTk.PhotoImage(Image.open("icons/record-icon.png").resize((64, 64), Image.ANTIALIAS))
        self.record_button = Button(self.toolbar_canvas, image=record_icon_img, command=self.record)
        self.record_button.pack(side=LEFT, fill=Y, padx=5)
        self.record_button.image = record_icon_img
        createToolTip(self.record_button, "Record all actions.")

        save_icon_img = ImageTk.PhotoImage(Image.open("icons/save-icon.png").resize((64, 64), Image.ANTIALIAS))
        self.save_button = Button(self.toolbar_canvas, image=save_icon_img, command=self.save)
        self.save_button.pack(side=LEFT, fill=Y, padx=5)
        self.save_button.image = save_icon_img
        createToolTip(self.save_button, "Save the modelverse.")

        self.toolbar_frame.pack(side=TOP, fill=X, expand=0)
        # self.toolbar_canvas.square.pack(side=RIGHT, fill=X, expand=0)
        self.toolbar_canvas.pack(side=LEFT, fill=X, expand=1)

        canvas_frame = Frame(master=self)

        self.c = Canvas(canvas_frame, width=self.master.winfo_screenwidth() * 2, height=self.master.winfo_screenheight() * 2,
                        relief=RIDGE, scrollregion=CANVAS_SIZE_TUPLE)

        vbar = Scrollbar(canvas_frame, orient=VERTICAL)
        vbar.config(command=self.c.yview)
        vbar.pack(side=RIGHT, fill=Y)

        hbar = Scrollbar(canvas_frame, orient=HORIZONTAL)
        hbar.config(command=self.c.xview)
        hbar.pack(side=BOTTOM, fill=X)

        self.c.config(background='white', yscrollcommand=vbar.set, xscrollcommand=hbar.set)
        self.c.pack(expand=True, fill=BOTH)

        self.__gridLineSeperation = 20
        self.__gridLineColor = '#c8c8c8'
        self.__gridWidth = 1

        self.__gridSubdivisions = 5
        self.__gridLineSubdivisionColor = '#e8e8e8'
        self.__gridSubdivisionShow = True
        self.__gridSubdivisionWidth = 1

        self.clear_canvas()

        self.c.bind("<Button-3>", self.create_instance)

        canvas_frame.pack()

root = Tk()
root.state('zoomed')
root.title('MvKFrontEnd')
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
app = Application(master=root)
root.bind('<Delete>', lambda event: app.delete())
root.bind('<Escape>', app.deselect)
app.mainloop()
