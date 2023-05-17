from winsound import Beep
from winsound import SND_ASYNC
import tkinter as tk

def c():
    Beep(262)
def csh():
    Beep(277)
def d():
    Beep(294)
def dsh():
    Beep(311)
def e(x):
    Beep(330, x)
def f(x):
    Beep(349, x)
def fsh(x):
    Beep(370, x)
def g(x):
    Beep(392, x)
def gsh(x):
    Beep(415, x)
def a(x):
    Beep(440, x)
def ash(x):
    Beep(466, x)
def b(x):
    Beep(494, x)
def cva(x):
    Beep(523, x)
def cshva(x):
    Beep(554, x)
def dva(x):
    Beep(587, x)
def dshva(x):
    Beep(622, x)
def eva(x):
    Beep(659, x)
def fva(x):
    Beep(698, x)
def fshva(x):
    Beep(740, x)
def gva(x):
    Beep(784, x)
def gshva(x):
    Beep(831, x)
def ava(x):
    Beep(880, x)
def ashva(x):
    Beep(932, x)
def bva(x):
    Beep(988, x)
def cvva(x):
    Beep(1047, x)


def cvb(x):
    Beep(131, x)
def cshvb(x):
    Beep(139, x)
def dvb(x):
    Beep(147, x)
def dshvb(x):
    Beep(156, x)
def evb(x):
    Beep(165, x)
def fvb(x):
    Beep(175, x)
def fshvb(x):
    Beep(185, x)
def gvb(x):
    Beep(196, x)
def gshvb(x):
    Beep(208, x)
def avb(x):
    Beep(220, x)
def ashvb(x):
    Beep(233, x)
def bvb(x):
    Beep(247, x)
def cshvvb(x):
    Beep(69, x)
def dvvb(x):
    Beep(73, x)
def dshvvb(x):
    Beep(78, x)
def evvb(x):
    Beep(82, x)
def fvvb(x):
    Beep(87, x)
def fshvvb(x):
    Beep(93, x)
def gvvb(x):
    Beep(98, x)
def gshvvb(x):
    Beep(104, x)
def avvb(x):
    Beep(110, x)
def ashvvb(x):
    Beep(117, x)
def bvvb(x):
    Beep(123, x)
def cvvvb(x):
    Beep(33, x)

def keypress(event):
    state = pygame.key.get_pressed()
    if event.keysym == 'Escape':
        root.destroy()
    x = event.char
    while x == 'c':
        c()

    while x == 'f':
        csh()

    while x == 'v':
        d()

    while x == 'g':
        dsh()

    while x == 'b':
        e(200)

    while x == 'n':
        f(200)

    while x == 'j':
        fsh(200)

    while x == 'm':
        g(200)

    while x == 'k':
        gsh(200)

    while x == ',':
        a(200)

    while x == 'l':
        ash(200)

    while x == '.':
        b(200)

    while x == '/':
        cva(200)

    if x == 'C':
        cva(200)

    if x == 'F':
        cshva(200)

    if x == 'V':
        dva(200)

    if x == 'G':
        dshva(200)

    if x == 'B':
        eva(200)

    if x == 'N':
        fva(200)

    if x == 'J':
        fshva(200)

    if x == 'M':
        gva(200)

    if x == 'K':
        gshva(200)

    if x == '<':
        ava(200)

    if x == 'L':
        ashva(200)

    if x == '>':
        bva(200)

    if x == '?':
        cvva(200)



    if x == '5':
        cshvvb(200)

    if x == 't':
        dvvb(200)

    if x == '6':
        dshvvb(200)

    if x == 'y':
        evvb(200)

    if x == 'u':
        fvvb(200)

    if x == '8':
        fshvvb(200)

    if x == 'i':
        gvvb(200)

    if x == '9':
        gshvvb(200)

    if x == 'o':
        avvb(200)

    if x == '0':
        ashvvb(200)

    if x == 'p':
        bvvb(200)

    if x == '[':
        cvb(200)

    if x == 'R':
        cvb(200)

    if x == '%':
        cshvb(200)

    if x == 'T':
        dvb(200)

    if x == '^':
        dshvb(200)

    if x == 'Y':
        evb(200)

    if x == 'U':
        fvb(200)

    if x == '*':
        fshvb(200)

    if x == 'I':
        gvb(200)

    if x == '(':
        gshvb(200)

    if x == 'O':
        avb(200)

    if x == ')':
        ashvb(200)

    if x == 'P':
        bvb(200)

    if x == '{':
        c()

root = tk.Tk()
print('''Welcome to the Keyboard
Keys R to [ are Notes C2 to C4
Keys C to / are Notes C4 to C6
Use Shift to Raise the Note an Octave
Press Esc to Quit''')
root.bind_all('<Key>', keypress, SND_ASYNC)
root.withdraw()
root.mainloop()