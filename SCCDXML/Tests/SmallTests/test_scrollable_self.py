'''
Created on 24-jul.-2014

@author: Simon
'''

from Tkinter import *


class Toolbar(Frame):
    PADDING = 5

    def __init__(self, name, master=None, cnf={}, **kw):
        Frame.__init__(self, master=master, cnf=cnf, **kw)
        self.config(relief=RAISED)
        Label(self, text=name).pack(side=TOP, pady=5)
        self.buttons = []

    def create_button(self, visual):
        new_button = None
        if isinstance(visual, str):
            new_button = Button(self, text=visual, command=lambda: self.create_button("Testtinngggzz"))
            new_button.pack(side=LEFT, fill=Y, padx=self.PADDING)
        elif isinstance(visual, ImageTk.PhotoImage):
            new_button = Button(self, image=visual)
            new_button.pack(side=LEFT, fill=Y, padx=self.PADDING)
            new_button.image = visual
        else:
            raise Exception('Can only create buttons with string or image visual.')
        self.buttons.append(new_button)


class HorizontalScrolledFrame(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a horizontal scrollbar for scrolling it
        hscrollbar = Scrollbar(self, orient=HORIZONTAL)
        hscrollbar.pack(fill=X, side=BOTTOM, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        xscrollcommand=hscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        hscrollbar.config(command=canvas.xview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        canvas.create_window(0, 0, window=interior, anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            print size
        interior.bind('<Configure>', _configure_interior)


class Test(Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        Tk.__init__(self, screenName=screenName, baseName=baseName, className=className, useTk=useTk, sync=sync, use=use)
        self.setup_gui()

    def setup_gui(self):
        self.title('MvKFrontEnd')
        self.bind('<Configure>', self.configure_gui)
        self.toolbar_frame = HorizontalScrolledFrame(self)
        self.toolbar_frame.pack(side=TOP, expand=True, fill=BOTH)
        for _ in range(20):
            tb = Toolbar("Test", self.toolbar_frame.interior)
            tb.create_button("Test1")
            tb.create_button("Test2")
            tb.create_button("Test3")
            tb.pack(side=LEFT)

    def configure_gui(self, event):
        # print 'Configure: (%i, %i)' % (event.width, event.height)
        pass


if __name__ == '__main__':
    t = Test()
    t.mainloop()
