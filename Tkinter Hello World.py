from tkinter import Tk
from tkinter import Button
from tkinter import messagebox
top = Tk()
def helloworld():
    messagebox.showinfo('Hello', 'Hello World!')
B = Button(top, text = "Hello", command = helloworld)
B.pack()
top.mainloop()