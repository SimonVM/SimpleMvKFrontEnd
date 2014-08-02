'''
Created on 21-jul.-2014

@author: Simon
'''
import time

import Tkinter as tk
import app_controller
from python_runtime.statecharts_core import Event
import rectangle_controller


class Test(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.setup_gui()
        self.last_event = None
        self.controller = app_controller.Controller(self)
        self.controller.start()
        self.widgets = []
        self.fixed_update_time = 20  # milliseconds
        self.schedule_time = time.time()
        self.scheduled_update_id = self.after(self.fixed_update_time, self.update)

    def setup_gui(self):
        self.state('zoomed')
        self.title('MvKFrontEnd')
        self.geometry("%dx%d" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        self.bind("<Button>", self.button_pressed)
        CANVAS_SIZE_TUPLE = (0, 0, self.winfo_screenwidth() * 2, self.winfo_screenheight() * 2)
        self.c = tk.Canvas(self, width=self.winfo_screenwidth() * 2, height=self.winfo_screenheight() * 2,
                                relief=tk.RIDGE, scrollregion=CANVAS_SIZE_TUPLE)

        vbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vbar.config(command=self.c.yview)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)

        hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        hbar.config(command=self.c.xview)
        hbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.c.config(background='white', yscrollcommand=vbar.set, xscrollcommand=hbar.set)
        self.c.pack(expand=True, fill=tk.BOTH)

        self.__gridLineSeperation = 20
        self.__gridLineColor = '#c8c8c8'
        self.__gridWidth = 1

        self.__gridSubdivisions = 5
        self.__gridLineSubdivisionColor = '#e8e8e8'
        self.__gridSubdivisionShow = True
        self.__gridSubdivisionWidth = 1

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

    def create_rectangle(self):
        x, y = self.last_event.x, self.last_event.y
        tag = self.c.create_rectangle(x, y, x + 50, y + 50)
        self.widgets.append(Rectangle(self.c, tag))

    def button_pressed(self, event):
        self.last_event = event
        event_name = None

        if event.num == 1:
            event_name = "left-click"
        elif event.num == 2:
            event_name = "middle-click"
        elif event.num == 3:
            event_name = "right-click"

        if self.controller and event_name:
            self.controller.addInput(Event(event_name, "input"))

    def update(self):
        self.schedule_time = time.time()
        self.scheduled_update_id = self.after(self.fixed_update_time, self.update)
        self.controller.update(self.fixed_update_time / 1000.0)
        for w in self.widgets:
            w.update(self.fixed_update_time / 1000.0)


class Rectangle:
    def __init__(self, c, tag):
        self.c = c
        self.tag = tag
        self.controller = rectangle_controller.Controller(self)
        self.controller.start()
        self.c.tag_bind(self.tag, "<Button>", self.button_pressed)
        self.c.tag_bind(self.tag, "<ButtonRelease>", self.button_released)
        self.c.tag_bind(self.tag, "<Motion>", self.drag)
        self.event_x = None
        self.event_y = None
        self.unhighlight()

    def button_pressed(self, event):
        event_name = None

        if event.num == 1:
            self.event_x = event.x
            self.event_y = event.y
            event_name = "left-click"

        if self.controller and event_name:
            self.controller.addInput(Event(event_name, "input"))

    def button_released(self, event):
        if self.controller:
            self.event_x = event.x
            self.event_y = event.y
            self.controller.addInput(Event("left-release", "input"))

    def drag(self, event):
        if self.controller:
            self.event_x = event.x
            self.event_y = event.y
            self.controller.addInput(Event("drag", "input"))

    def move(self):
        deltax = self.c.canvasx(self.event_x) - self.c.canvasx(self.c.coords(self.tag)[0])
        deltay = self.c.canvasy(self.event_y) - self.c.canvasy(self.c.coords(self.tag)[1])
        self.c.move(self.tag, deltax, deltay)

    def highlight(self):
        self.c.itemconfig(self.tag, fill="yellow")

    def unhighlight(self):
        self.c.itemconfig(self.tag, fill="ghost white")

    def update(self, delta):
        self.controller.update(delta)


if __name__ == '__main__':
    t = Test()
    t.mainloop()
