from random import randint
from tkinter import Tk
from tkinter import Button
from tkinter import messagebox
top = Tk()
p = 0
def hello():
    global p
    p = p + 1
    x = randint(1, 6)
    y = randint(1, 6)
    if (x + y == 7 or x + y == 11) and p == 1:
        messagebox.showinfo('Craps', 'You rolled a {}! You win!'.format(x + y))
    elif (x + y == 2 or x + y == 3 or x + y == 12) and p == 1:
        messagebox.showinfo('Craps', 'You rolled a {}! You Lose!'.format(x + y))
    else:
        messagebox.showinfo('Craps', '''First Die: {}
Second Die: {}
Total:
Point: {}'''.format(x, y, x + y))



B = Button(top, text = "Roll", command = hello)
B.pack()

top.mainloop()