#! /usr/bin/env python
import tkinter
import sys
import ctypes
from tkinter import ttk

#Full HD
WIDTH = 1280
HEIGHT = 720


class sub_frameB(tkinter.Frame):
    def __init__(self, master=None):
        self.text_num = tkinter.StringVar()
        self.text_num.set("Default")

        tkinter.Frame.__init__(self, master, height=HEIGHT/2, width=WIDTH/2)

        frame = tkinter.Frame(self)#,relief=tkinter.RIDGE)
        label_frame = tkinter.Frame(self)

        for i in range(0, 10):
            tenkey = tkinter.Button(frame, text=str(i))
            if i < 5:
                tenkey.grid(row=1, column=i%5+1, command=self.add_text(i))
            elif i >= 5:
                tenkey.grid(row=2, column=i%5+1, command=self.add_text(i))
            else:
                pass

        dot_button = tkinter.Button(frame,text=str("."), command=self.add_text("."))
        dot_button.grid(row=3, column=1)

        frame.place(x=0, y=0)


        text_label=tkinter.Label(label_frame,textvariable=self.text_num)
        text_label.pack()#.grid(row=4,column=1,columnspan=20)

        save_button=tkinter.Button(label_frame, text=str("SEND"), command=self.add_text("SEND"))
        save_button.pack()#.grid(row=3,column=3)

        clear_button=tkinter.Button(label_frame, text=str("CLEAR"))
        clear_button.pack()#.grid(row=3,column=2)


        label_frame.place(x=0, y=100)

    def add_text(self, add_text):
        try:
            self.text_num.set((self.text_num.get()) + str(add_text))
        except ValueError:
            pass

    def clear_text(self):
        self.text_num=''


class sub_frameA(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master, height=HEIGHT/2, width=WIDTH/2)

class sub_frameC(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master, height=HEIGHT/2, width=WIDTH/2)


def main():
    root_screen = tkinter.Tk()
    root_screen.geometry("{0}x{1}".format(WIDTH, HEIGHT))
    root_screen.title('Temperature')

    main_screen=ttk.Frame(root_screen)
    main_screen.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))

    tenkey_screen=sub_frameB(main_screen)
    tenkey_screen.grid(column=1, row=0)

    bodytm_screen=sub_frameA(main_screen)
    bodytm_screen.grid(column=0, row=0)

    saving_screen=sub_frameC(main_screen)
    saving_screen.grid(column=1, row=1)

    for child in main_screen.winfo_children():
        child.grid_configure(padx=1, pady=1)

    root_screen.mainloop()


if __name__ == '__main__':
    main()
