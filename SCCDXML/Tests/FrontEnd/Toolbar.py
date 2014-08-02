'''
Created on 22-jul.-2014

@author: Simon
'''

import Image
import ImageTk

import Tkinter as tk


class Toolbar(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        tk.Frame.__init__(self, master=master, cnf=cnf, **kw)
        self.toolbar_bottom_frame = tk.Frame(self)
        self.toolbar_canvas = tk.Canvas(master=self,
                                        takefocus=1,
                                        scrollregion=(0, 0, self.master.winfo_screenwidth() * 2, 0))

        self.toolbar_canvas.square = tk.Canvas(self.toolbar_bottom_frame,
                                               width=16, height=16)

        self.toolbar = tk.Frame(self.toolbar_canvas)
        self.toolbar_canvas_handler = self.toolbar_canvas.create_window(0, 0, window=self.toolbar, anchor=tk.NW)

        new_icon_img = ImageTk.PhotoImage(Image.open("icons/new-icon.png").resize((64, 64), Image.ANTIALIAS))
        self.new_button = tk.Button(self.toolbar_canvas, image=new_icon_img, command=self.create_model)
        self.new_button.pack(side=tk.LEFT, fill=tk.Y, padx=5)
        self.new_button.image = new_icon_img

        self.pack(side=tk.TOP, fill=tk.X, expand=0)
        self.toolbar_canvas.pack(side=tk.LEFT, fill=tk.X, expand=1)

    def update(self, delta):
        pass

    def create_model(self, blaat):
        pass
