from tkinter import *
import tkinter as tk
import math

e = math.e
pi = math.pi

win = tk.Tk()
win.title("Calculator")
win.geometry("360x415+990+100")
win.configure(bg="#292F33")

equation = tk.StringVar()
expression_field = tk.Entry(win, relief=GROOVE,borderwidth=7, textvariable=equation, font=("Time in romana", 30), bg="white")
expression_field.place(x=1, y=50, height=50, width=360)
label_title = tk.Label(win, text="Calculator", font=("Times New Roman", 30, "bold"), bg="#ffbf00")
label_title.place(x=1, y=0, height=48, width=360)


def press(num):
    equation.set(equation.get() + str(num))


def equal():
    try:
        result = eval(equation.get())
        equation.set(str(result))
    except:
        equation.set("Error")


def clean():
    equation.set("")


def back():
    equation.set(equation.get()[:-1])


def sin():
    try:
        result = math.sin(eval(equation.get()))
        equation.set(str(result))
    except:
        equation.set("Error")


def cos():
    try:
        result = math.cos(eval(equation.get()))
        equation.set(str(result))
    except:
        equation.set("Error")


def tan():
    try:
        result = math.tan(eval(equation.get()))
        equation.set(str(result))
    except:
        equation.set("Error")


# Define other mathematical functions
def logarithm(base=10):
    try:
        result = math.log(eval(equation.get()), base)
        equation.set(str(result))
    except:
        equation.set("Error")


def square_root():
    try:
        result = math.sqrt(eval(equation.get()))
        equation.set(str(result))
    except:
        equation.set("Error")  # Define other mathematical functions


# first column
l2a = tk.Button(win, text="sin", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: sin())
l2a.place(x=5, y=105, height=50, width=70)
l6e = tk.Button(win, text="cos", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: cos())
l6e.place(x=5, y=156, height=50, width=70)
l6aa = tk.Button(win, text="tan", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: tan())
l6aa.place(x=5, y=207, height=50, width=70)
l6bb = tk.Button(win, text="log", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: logarithm())
l6bb.place(x=5,y=258, height=50, width=70)
l6dt = tk.Button(win, text="√", font=("Time in romana", 30, "bold"), bg="#c5ccd3", command=lambda: square_root())
l6dt.place(x=5, y=309, height=50, width=70)
l6vy = tk.Button(win, text="", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press(""))
l6vy.place(x=5, y=360, height=50, width=70)

# second  column
l6v = tk.Button(win, text="(", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press("("))
l6v.place(x=76, y=105, height=50, width=70)
l2 = tk.Button(win, text="c", font=("Time in romana", 25, "bold"), bg="sky blue", command=lambda: clean())
l2.place(x=76, y=156, height=50, width=70)
l6 = tk.Button(win, text="7", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("7"))
l6.place(x=76, y=207, height=50, width=70)
l6a = tk.Button(win, text="4", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("4"))
l6a.place(x=76,y=258, height=50, width=70)
l6b = tk.Button(win, text="1", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("1"))
l6b.place(x=76, y=309, height=50, width=70)
l6d = tk.Button(win, text=".", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("."))
l6d.place(x=76, y=360, height=50, width=70)


# third column

l3 = tk.Button(win, text="←", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: back())
l3.place(x=147, y=156, height=50, width=70)
l7 = tk.Button(win, text="8", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("8"))
l7.place(x=147,  y=207, height=50, width=70)
l7a = tk.Button(win, text="5", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("5"))
l7a.place(x=147, y=258, height=50, width=70)
l7b = tk.Button(win, text="2", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("2"))
l7b.place(x=147,y=309, height=50, width=70)
f = tk.Button(win, text="0", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("0"))
f.place(x=147,y=360, height=50, width=70)
f1 = tk.Button(win, text=")", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press(")"))
f1.place(x=147, y=105, height=50, width=70)

# forth column
l4 = tk.Button(win, text="%", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("%"))
l4.place(x=218, y=156, height=50, width=70)
l8 = tk.Button(win, text="9", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("9"))
l8.place(x=218, y=207, height=50, width=70)
l8a = tk.Button(win, text="6", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("6"))
l8a.place(x=218, y=258, height=50, width=70)
l8b = tk.Button(win, text="3", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("3"))
l8b.place(x=218, y=309, height=50, width=70)
l8c = tk.Button(win, text="e", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("e"))
l8c.place(x=218, y=360, height=50, width=70)
l8n = tk.Button(win, text="π", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press("pi("))
l8n.place(x=218, y=105, height=50, width=70)

# fifth column
l5 = tk.Button(win, text="+", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("+"))
l5.place(x=289,y=105, height=50, width=70)
l5a = tk.Button(win, text="-", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("-"))
l5a.place(x=289,  y=156, height=50, width=70)
l5c = tk.Button(win, text="*", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("*"))
l5c.place(x=289,y=207, height=50, width=70)
l5f = tk.Button(win, text="/", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("/"))
l5f.place(x=289, y=258, height=50, width=70)
l5b = tk.Button(win, text="=", font=("Time in romana", 25, "bold"), bg="#ffa500", command=lambda: equal())
l5b.place(x=289, y=309, height=101, width=70)


win.mainloop()
#############################################$$$$$$$$$$$ MY CODE  $$$$$$$$$$$$$$$$###################################
# from tkinter import *
#
#
# def press(item):
#     global statement
#     statement = statement + str(item)
#     input.set(statement)
#
#
# def clean():
#     global statement
#     statement = ""
#     input.set("")
#
#
# def equal():
#     global statement
#     result = str(eval(statement))
#     input.set(result)
#     statement = ""
#
#
# statement = ""
#
# win = Tk()
# win.title("Calculater")
# win.config(bg="black")
# win.iconbitmap(r"F:\Calculator-icon.ico")
# win.geometry("359x465")     # width x height
# # win.resizable(False,False)
#
# input = StringVar()
#
# e = Entry(win, font=("Time in romana", 25, "bold"), textvariable=input, justify="right")
# e.place(x=5, y=5, height=90, width=346)
#
# l2 = Button(win, text="c", font=("Time in romana", 25, "bold"), bg="sky blue", command=lambda: clean())
# l2.place(x=10, y=120, height=50, width=70)
#
# l3 = Button(win, text="/", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("/"))
# l3.place(x=100, y=120, height=50, width=70)
#
# l4 = Button(win, text="*", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("*"))
# l4.place(x=190, y=120, height=50, width=70)
# #
# l5 = Button(win, text="-", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("-"))
# l5.place(x=280, y=120, height=50, width=70)
#
# l5a = Button(win, text="+", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("+"))
# l5a.place(x=280, y=190, height=50, width=70)
#
# l5c = Button(win, text="%", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("%"))
# l5c.place(x=280, y=260, height=50, width=70)
#
#
# l5b = Button(win, text="=", font=("Time in romana", 25, "bold"), bg="#ffa500", command=lambda: equal())
# l5b.place(x=280, y=330, height=120, width=70)
#
# l6 = Button(win, text="7", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("7"))
# l6.place(x=10, y=190, height=50, width=70)
#
# l6a = Button(win, text="4", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("4"))
# l6a.place(x=10, y=260, height=50, width=70)
#
# l6b = Button(win, text="1", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("1"))
# l6b.place(x=10, y=330, height=50, width=70)
#
# l6b = Button(win, text="0", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("0"))
# l6b.place(x=10, y=400, height=50, width=160)
# #
# l7 = Button(win, text="8", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("8"))
# l7.place(x=100, y=190, height=50, width=70)
#
# l7a = Button(win, text="5", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("5"))
# l7a.place(x=100, y=260, height=50, width=70)
#
# l7b = Button(win, text="2", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("2"))
# l7b.place(x=100, y=330, height=50, width=70)
# #
# l8 = Button(win, text="9", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("9"))
# l8.place(x=190, y=190, height=50, width=70)
#
# l8a = Button(win, text="6", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("6"))
# l8a.place(x=190, y=260, height=50, width=70)
#
# l8b = Button(win, text="3", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("3"))
# l8b.place(x=190, y=330, height=50, width=70)
#
# l8 = Button(win, text=".", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("."))
# l8.place(x=190, y=400, height=50, width=70)
#
# win.mainloop()