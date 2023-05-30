import os
from tkinter import *
from tkinter import filedialog
from os import system

root = Tk("Text Editor")
root.title('Simple Text Editor')
text = Text(root)
text.grid()

def SaveButton():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files","*.txt"),("All Files","*.*")))
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()
    print("Saving file...")


def OpenButton():
    global text
    openlocation = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files","*.txt"),("all files","*.*")))
    with open(openlocation, "r") as f:
        Label(root, text = f.read())

button = Button(root, text = "Save", command = SaveButton)
button.grid()

button = Button(root, text = "Open", command = OpenButton)
button.grid()

def Font_Verdana():
    global text
    text.config(font = "Verdana")

def Font_Helvetica():
    global text
    text.config(font = "Helvetica")

def Font_Courier():
    global text
    text.config(font = "Courier")

def Font_TimesNewRoman():
    global text
    text.config(font = "Times")

font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

Helvetica = IntVar()
arial = IntVar()
Times = IntVar()
Courier = IntVar()
Verdana = IntVar()


font.menu.add_checkbutton(label = "Courier", variable = Courier,
command = Font_Courier)

font.menu.add_checkbutton(label = "Helvetica", variable = Helvetica,
command = Font_Helvetica)

font.menu.add_checkbutton(label = "Verdana", variable = Verdana,
command = Font_Verdana)

font.menu.add_checkbutton(label = "Times", variable = Times,
command = Font_TimesNewRoman)

root.mainloop()
