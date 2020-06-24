'''
#! /usr/bin/env python
import tkinter
import sys
import ctypes

#Full HD
WIDTH=1280
HEIGHT=720

INTERBAL=20
SECTION_SIZE=10

BT_H=5
BT_W=10

class number_widget(tkinter.Frame):
    def __init__(self,master=None):
        tkinter.Frame.__init__(self,master,height=HEIGHT/2,width=WIDTH/2)
        self.master.title('Temperature')

        frame=tkinter.Frame(self,relief=tkinter.RIDGE)
        
        for i in range(0,10): 
            tenkey=tkinter.Button(frame,text = str(i))
            
            if i < 5:
                tenkey.grid(row=1,column=i%5+1)
            elif i >= 5:
                tenkey.grid(row=2,column=i%5+1)
            else:
                pass

            frame.place(x=0, y=0)


def main():
    
    #primary_screen=number_widget()
    ##primary_screen.title("Temperature")  
    ##primary_screen.geometry("{0}x{1}".format(WIDTH,HEIGHT))
    #primary_screen.size("{0}x{1}".format(WIDTH,HEIGHT))
    #primary_screen.pack()
    #primary_screen.mainloop()

    screen=tkinter.Tk()
    screen.mainloop()


if __name__ == '__main__':
    main()
'''

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()