'''
Created on 24-jul.-2014

@author: Simon
'''

import Tkinter as tk


class Test(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.setup_gui()

    def setup_gui(self):
        self.title('MvKFrontEnd')

        self.__gridLineSeperation = 20
        self.__gridLineColor = '#c8c8c8'
        self.__gridWidth = 1

        self.__gridSubdivisions = 5
        self.__gridLineSubdivisionColor = '#e8e8e8'
        self.__gridSubdivisionShow = True
        self.__gridSubdivisionWidth = 1

        CANVAS_SIZE_TUPLE = (0, 0, self.winfo_screenwidth() * 2, self.winfo_screenheight() * 2)
        self.c = tk.Canvas(self, relief=tk.RIDGE, scrollregion=CANVAS_SIZE_TUPLE)

        vbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vbar.config(command=self.c.yview)
        vbar.grid(row=0, column=1, rowspan=3, sticky=(tk.N, tk.S))

        hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        hbar.config(command=self.c.xview)
        hbar.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.c.config(background='white', yscrollcommand=vbar.set, xscrollcommand=hbar.set)
        self.c.grid(row=1, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))

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


if __name__ == '__main__':
    t = Test()
    t.mainloop()
