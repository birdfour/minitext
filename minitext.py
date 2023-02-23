# import the necessary modules
from tkinter import Tk, Button, Frame, END, Label, Text, Scrollbar
from tkinter import simpledialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
row = 0

#open a file
def openfile():
    global currentFile
    inputfile = askopenfilename(filetypes=[("text files", "*.txt"), ("all files", "*.*")])
    if inputfile is not None:
        textbox.delete("1.0", END)
        with open(inputfile, mode="r", encoding="utf-8") as file:
            currentFile = file
            textbox.insert(END, file.read())
            window.title("minitext - " + file.name)

# open a file from a pinned button
def open2(inputfile):
    with open(inputfile, mode="r", encoding="utf-8") as file:
        textbox.delete("1.0", END)
        currentFile = file
        textbox.insert(END, file.read())
        window.title("minitext - " + file.name)

#save the text to a file
def savefileas():
    types = [("text file (.txt)", "*.txt"), ("all files", "*.*")]
    inputfile = asksaveasfilename(filetypes=types, defaultextension=types)
    with open(inputfile, mode="w", encoding="utf-8") as file:
        text = textbox.get("1.0", END)
        file.write(text)

#save the file
def savefile():
    if currentFile is not None:
        with open(currentFile.name, mode="w") as file:
            text = textbox.get("1.0", END)
            file.write(text)

#start a new file
def newfile():
    global currentFile
    currentFile = None
    textbox.delete("1.0", END)
    window.title("minitext - untitled")

#add a button to the pinned buttons column
def addbutton():
    global row
    types = [("text file (.txt)", "*.txt"), ("all files", "*.*")]
    inputfile = askopenfilename(filetypes=types)
    if inputfile != None:
        name = simpledialog.askstring("display name", "type a display name for this file")
        if name != "" or None:
            b = Button(pin, text=name, border=0, command=lambda inputfile=inputfile: open2(inputfile))
            b.grid(row=row, column=0, sticky="ew", padx=5, pady=2.5)
            row += 1

#initialize the window
window = Tk()
window.resizable(width=False, height=False)
window.title("minitext")

#add the basic components (text, sidebar, scrollbar)
textbox = Text(window)
sidebar = Frame(window, bg="#d4d4d4", bd=2)
pin = Frame(window, bg="#e4e4e4", bd=2)
vertical = Scrollbar(window, orient="vertical", command=textbox.yview)

#add buttons to the sidebar
l = Label(sidebar, text="-file-", bg="#d2d2d2")
openbutton = Button(sidebar, text="open", command=openfile, border=0)
saveasbutton = Button(sidebar, text="save as...", command=savefileas, border=0)
savebutton = Button(sidebar, text="save", command=savefile, border=0)
newbutton = Button(sidebar, text="new", command=newfile, border=0)
add = Button(sidebar, text="pin file...", command=addbutton, border=0)

#arrange the components
l.grid(row=0, column=0, sticky="ew", padx=5)
openbutton.grid(row=2, column=0, sticky="ew", padx=5)
saveasbutton.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
savebutton.grid(row=4, column=0, sticky="ew", padx=5)
newbutton.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
add.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
sidebar.grid(row=0, column=0, sticky="ns")
textbox.grid(row=0, column=2, sticky="nsew")
pin.grid(row=0, column=1, sticky="ns")
vertical.grid(row=0, column=3, sticky="nsew")
window.mainloop()
