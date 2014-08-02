'''
Created on 21-jul.-2014

@author: Simon
'''
import Tkinter

import ImageTk

from Tooltip import createToolTip


class Widget(Tkinter.Widget):
    def __init__(self, parent=None):
        self.parent = parent


class Window(Widget, Tkinter.Frame):
    def __init__(self, parent=None, **kw):
        Tkinter.Frame.__init__(self, master=parent, **kw)
        Widget.__init__(self, parent)


class MainWindow(Window):
    def __init__(self, parent, **kw):
        Window.__init__(self, parent, **kw)
        self.c = Canvas(self)
        self.pack()
        '''

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
        '''

    def deselect(self):
        pass


class CreateWindow(Window):
    pass


class BrowseWindow(Window):
    pass


class Toolbar(Window):
    def __init__(self, parent):
        self.toolbar_frame = Tkinter.Frame(master=self)
        self.toolbar_bottom_frame = Tkinter.Frame(self.toolbar_frame)
        self.toolbar_canvas = Tkinter.Canvas(master=self.toolbar_frame,
                                             takefocus=1,
                                             scrollregion=(0, 0, self.master.winfo_screenwidth() * 2, 0))

        self.toolbar_canvas.square = Tkinter.Canvas(self.toolbar_bottom_frame, width=16, height=16)

        self.toolbar = Tkinter.Frame(self.toolbar_canvas)
        self.toolbar_canvas_handler = self.toolbar_canvas.create_window(0, 0, window=self.toolbar, anchor=Tkinter.NW)


class EditWindow(Window):
    pass


class Canvas(Window):
    def __init__(self, parent, **kw):
        Window.__init__(self, parent, **kw)

        CANVAS_SIZE_TUPLE = (0, 0, self.parent.winfo_screenwidth() * 2, self.parent.winfo_screenheight() * 2)
        self.c = Tkinter.Canvas(self, width=self.parent.winfo_screenwidth() * 2, height=self.parent.winfo_screenheight() * 2,
                                relief=Tkinter.RIDGE, scrollregion=CANVAS_SIZE_TUPLE)

        vbar = Tkinter.Scrollbar(self, orient=Tkinter.VERTICAL)
        vbar.config(command=self.c.yview)
        vbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        hbar = Tkinter.Scrollbar(self, orient=Tkinter.HORIZONTAL)
        hbar.config(command=self.c.xview)
        hbar.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)

        self.c.config(background='white', yscrollcommand=vbar.set, xscrollcommand=hbar.set)
        self.c.pack(expand=True, fill=Tkinter.BOTH)

        self.__gridLineSeperation = 20
        self.__gridLineColor = '#c8c8c8'
        self.__gridWidth = 1

        self.__gridSubdivisions = 5
        self.__gridLineSubdivisionColor = '#e8e8e8'
        self.__gridSubdivisionShow = True
        self.__gridSubdivisionWidth = 1

        self.clear()

        # self.c.bind("<Button-3>", self.create_instance)

        self.pack()

    def clear(self):
        CANVAS_SIZE_TUPLE = (0, 0, self.parent.winfo_screenwidth() * 2, self.parent.winfo_screenheight() * 2)
        self.c.delete("all")
        subdivisionSeperation = self.__gridLineSeperation * self.__gridSubdivisions
        for x in range(CANVAS_SIZE_TUPLE[0], CANVAS_SIZE_TUPLE[2], subdivisionSeperation):
            self.c.create_line(x, 0, x, CANVAS_SIZE_TUPLE[3], width=self.__gridSubdivisionWidth, fill=self.__gridLineSubdivisionColor)

        for y in range(CANVAS_SIZE_TUPLE[1], CANVAS_SIZE_TUPLE[3], subdivisionSeperation):
            self.c.create_line(0, y, CANVAS_SIZE_TUPLE[2], y, width=self.__gridSubdivisionWidth, fill=self.__gridLineSubdivisionColor)

        for x in range(CANVAS_SIZE_TUPLE[0], CANVAS_SIZE_TUPLE[2], self.__gridLineSeperation):
            for y in range(CANVAS_SIZE_TUPLE[1], CANVAS_SIZE_TUPLE[3], self.__gridLineSeperation):
                self.c.create_oval(x - self.__gridWidth, y - self.__gridWidth, x + self.__gridWidth, y + self.__gridWidth, width=0, fill=self.__gridLineColor)


class Button(Widget, Tkinter.Button):
    def __init__(self, parent, visual, tooltip=None, **kw):
        Tkinter.Button.__init__(self, parent, **dict(visual.get_params().items() + kw.items()))
        createToolTip(self, tooltip)


class ActionButton(Button):
    def __init__(self, parent, action, visual, tooltip=None, **kw):
        Button.__init__(self, parent)


class SelectButton(Button):
    pass


class Visual(object):
    def get_params(self):
        raise NotImplementedError()


class Text(Visual):
    def __init__(self, text):
        self.text = text

    def get_params(self):
        return {'text': self.text}


class Image(Visual):
    def __init__(self, location):
        self.icon = ImageTk.PhotoImage(Image.open(location).resize((64, 64), Image.ANTIALIAS))

    def get_params(self):
        return {'image': self.icon}


class SelectBox(Widget):
    pass


def main():
    root = Tkinter.Tk()
    root.state('zoomed')
    root.title('MvKFrontEnd')
    root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
    mw = MainWindow(parent=root)
    root.bind('<Delete>', lambda event: mw.delete())
    root.bind('<Escape>', mw.deselect)
    mw.mainloop()


if __name__ == '__main__':
    main()
