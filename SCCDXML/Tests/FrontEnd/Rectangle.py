'''
Created on 22-jul.-2014

@author: Simon
'''
import rectangle_controller
from python_runtime.statecharts_core import Event


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
