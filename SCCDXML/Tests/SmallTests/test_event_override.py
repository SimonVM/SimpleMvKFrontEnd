'''
Created on 27-jul.-2014

@author: Simon
'''
import time
import Tkinter as tk


class MvKWidget(tk.Widget):
    def __init__(self, bindable=None, tagorid=None):
        if bindable is None:
            bindable = self
        self.bindable = bindable
        self.tagorid = tagorid
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
        self.last_x = 0
        self.last_y = 0
        self.selected_type = None

    def on_click(self, event):
        event_name = None
        print self.tagorid

        if event.num == 1:
            event_name = "left-click"
        elif event.num == 2:
            event_name = "middle-click"
        elif event.num == 3:
            event_name = "right-click"

        if event_name:
            self.last_x = event.x
            self.last_y = event.y
            self.add_input(event_name)

        return 'break'

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
            self.add_input(event_name)

        return 'break'

    def on_motion(self, event):
        self.last_x = event.x
        self.last_y = event.y
        self.add_input("motion")

        return 'break'

    def on_enter(self, event):
        self.bindable.focus_force()
        self.add_input("enter")

        return 'break'

    def on_leave(self, event):
        self.add_input("leave")

        return 'break'

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
            self.add_input(event_name)

        return 'break'


class FrontEnd(tk.Tk, MvKWidget):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('TestOverride')
        self.right_clicked = False

        CANVAS_SIZE_TUPLE = (0, 0, self.winfo_screenwidth() * 2, self.winfo_screenheight() * 2)
        self.c = tk.Canvas(self, relief=tk.RIDGE, scrollregion=CANVAS_SIZE_TUPLE)
        self.c.focus_force()
        self.c.pack(expand=True, fill=tk.BOTH)

        self.balls = []

        MvKWidget.__init__(self, self.c)

    def add_input(self, event_name):
        if event_name == 'right-click':
            print 'in FrontEnd.right_click()!'
            self.right_clicked = True
        if event_name == 'right-release' and self.right_clicked:
            self.balls.append(Ball(self.c, self.last_x, self.last_y))
            self.right_clicked = False


class Ball(MvKWidget):
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.right_clicked = False
        self.r = 15.0
        self.id = self.canvas.create_oval(x, y, x + (self.r * 2), y + (self.r * 2), fill="black")
        MvKWidget.__init__(self, self.canvas, self.id)

    def add_input(self, event_name):
        if event_name == 'right-click':
            print 'in Ball.right_click()!'
            self.canvas.focus(self.id)
            self.right_clicked = True
        if event_name == 'right-release' and self.right_clicked:
            self.canvas.delete(self.id)
            self.right_clicked = False


if __name__ == '__main__':
    f = FrontEnd()
    f.mainloop()
