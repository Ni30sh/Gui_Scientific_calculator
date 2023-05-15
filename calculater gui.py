from tkinter import *
import math

e = math.e
pi = math.pi


def log(item, base=10):
    return math.log(item, base)


def sqrt(item):
    return math.sqrt(item)  # Define other mathematical functions


# Define trigonometric functions
def sin(item):
    return math.sin(item)


def tan(item):
    return math.tan(item)


def cos(item):
    return math.cos(item)


def press(item):
    global statement
    statement = statement + str(item)  # new data in entry box
    input.set(statement)


def back():
    global statement  # outside data change by this command
    statement = statement[:-1]  # used to select all data variable except the last one (slicing)
    input.set(statement)  # data set in entry box


def clean():
    global statement
    statement = ""
    input.set("")


def equal():
    global statement
    try:  # to solve zero division error
        result = str(eval(statement, {'e': e, 'pi': pi, 'sin': sin, 'cos': cos, 'tan': tan, 'log': log,
                                      'sqrt': sqrt}))  # eval is one-linear mathematical data perform
    except:
        result = "Error"
    input.set(result)


statement = ""

win = Tk()
win.title("Calculater")
win.config(bg="black")
# win.iconbitmap(r"F:\Calculator-icon.ico")
win.geometry("405x470")  # width x height
# win.resizable(False,False)

input = StringVar()
e1 = Entry(win, font=("Time in romana", 25, "bold"), textvariable=input, justify="right")
e1.place(x=5, y=5, height=90, width=395)
# first column
l2a = Button(win, text="sin", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press("sin"))
l2a.place(x=10, y=110, height=50, width=70)
l6e = Button(win, text="cos", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press("cos"))
l6e.place(x=10, y=170, height=50, width=70)
l6aa = Button(win, text="tan", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press("tan"))
l6aa.place(x=10, y=230, height=50, width=70)
l6bb = Button(win, text="log", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press("lg"))
l6bb.place(x=10, y=290, height=50, width=70)
l6dt = Button(win, text="√", font=("Time in romana", 30, "bold"), bg="#c5ccd3", command=lambda: press("sqrt"))
l6dt.place(x=10, y=350, height=50, width=70)
l6vy = Button(win, text="", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press(""))
l6vy.place(x=10, y=410, height=50, width=70)

# second  column
l2 = Button(win, text="c", font=("Time in romana", 25, "bold"), bg="sky blue", command=lambda: clean())
l2.place(x=90, y=110, height=50, width=70)
l6 = Button(win, text="7", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("7"))
l6.place(x=90, y=170, height=50, width=70)
l6a = Button(win, text="4", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("4"))
l6a.place(x=90, y=230, height=50, width=70)
l6b = Button(win, text="1", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("1"))
l6b.place(x=90, y=290, height=50, width=70)
l6d = Button(win, text=".", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("."))
l6d.place(x=90, y=350, height=50, width=70)
l6v = Button(win, text="(", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press("("))
l6v.place(x=90, y=410, height=50, width=70)

# third column

l3 = Button(win, text="←", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: back())
l3.place(x=170, y=110, height=50, width=70)
l7 = Button(win, text="8", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("8"))
l7.place(x=170, y=170, height=50, width=70)
l7a = Button(win, text="5", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("5"))
l7a.place(x=170, y=230, height=50, width=70)
l7b = Button(win, text="2", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("2"))
l7b.place(x=170, y=290, height=50, width=70)
f = Button(win, text="0", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("0"))
f.place(x=170, y=350, height=50, width=70)
f1 = Button(win, text=")", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press(")"))
f1.place(x=170, y=410, height=50, width=70)

# forth column
l4 = Button(win, text="%", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("%"))
l4.place(x=250, y=110, height=50, width=70)
l8 = Button(win, text="9", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("9"))
l8.place(x=250, y=170, height=50, width=70)
l8a = Button(win, text="6", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("6"))
l8a.place(x=250, y=230, height=50, width=70)
l8b = Button(win, text="3", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("3"))
l8b.place(x=250, y=290, height=50, width=70)
l8c = Button(win, text="e", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("e"))
l8c.place(x=250, y=350, height=50, width=70)
l8n = Button(win, text="π", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press("pi"))
l8n.place(x=250, y=410, height=50, width=70)

# fifth column
l5 = Button(win, text="+", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("+"))
l5.place(x=330, y=110, height=50, width=70)
l5a = Button(win, text="-", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("-"))
l5a.place(x=330, y=170, height=50, width=70)
l5c = Button(win, text="*", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("*"))
l5c.place(x=330, y=230, height=50, width=70)
l5b = Button(win, text="=", font=("Time in romana", 25, "bold"), bg="#ffa500", command=lambda: equal())
l5b.place(x=330, y=350, height=110, width=70)
l5f = Button(win, text="/", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("/"))
l5f.place(x=330, y=290, height=50, width=70)

win.mainloop()
