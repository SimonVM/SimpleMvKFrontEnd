'''
Created on 27-jul.-2014

@author: Simon
'''
import time
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
