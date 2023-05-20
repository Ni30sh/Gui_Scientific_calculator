import tkinter as tk
import math

e = math.e
pi = math.pi

win = tk.Tk()
win.title("Calculator")
win.geometry("400x470")
win.configure(bg="#292F33")

equation = tk.StringVar()
expression_field = tk.Entry(win, textvariable=equation, font=("Time in romana", 20), bg="white")
expression_field.place(x=5, y=5, height=90, width=395)


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
l2a.place(x=10, y=110, height=50, width=70)
l6e = tk.Button(win, text="cos", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: cos())
l6e.place(x=10, y=170, height=50, width=70)
l6aa = tk.Button(win, text="tan", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: tan())
l6aa.place(x=10, y=230, height=50, width=70)
l6bb = tk.Button(win, text="log", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: logarithm())
l6bb.place(x=10, y=290, height=50, width=70)
l6dt = tk.Button(win, text="√", font=("Time in romana", 30, "bold"), bg="#c5ccd3", command=lambda: square_root())
l6dt.place(x=10, y=350, height=50, width=70)
l6vy = tk.Button(win, text="", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press(""))
l6vy.place(x=10, y=410, height=50, width=70)

# second  column
l2 = tk.Button(win, text="c", font=("Time in romana", 25, "bold"), bg="sky blue", command=lambda: clean())
l2.place(x=90, y=110, height=50, width=70)
l6 = tk.Button(win, text="7", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("7"))
l6.place(x=90, y=170, height=50, width=70)
l6a = tk.Button(win, text="4", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("4"))
l6a.place(x=90, y=230, height=50, width=70)
l6b = tk.Button(win, text="1", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("1"))
l6b.place(x=90, y=290, height=50, width=70)
l6d = tk.Button(win, text=".", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("."))
l6d.place(x=90, y=350, height=50, width=70)
l6v = tk.Button(win, text="(", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press("("))
l6v.place(x=90, y=410, height=50, width=70)

# third column

l3 = tk.Button(win, text="←", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: back())
l3.place(x=170, y=110, height=50, width=70)
l7 = tk.Button(win, text="8", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("8"))
l7.place(x=170, y=170, height=50, width=70)
l7a = tk.Button(win, text="5", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("5"))
l7a.place(x=170, y=230, height=50, width=70)
l7b = tk.Button(win, text="2", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("2"))
l7b.place(x=170, y=290, height=50, width=70)
f = tk.Button(win, text="0", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("0"))
f.place(x=170, y=350, height=50, width=70)
f1 = tk.Button(win, text=")", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press(")"))
f1.place(x=170, y=410, height=50, width=70)

# forth column
l4 = tk.Button(win, text="%", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("%"))
l4.place(x=250, y=110, height=50, width=70)
l8 = tk.Button(win, text="9", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("9"))
l8.place(x=250, y=170, height=50, width=70)
l8a = tk.Button(win, text="6", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("6"))
l8a.place(x=250, y=230, height=50, width=70)
l8b = tk.Button(win, text="3", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("3"))
l8b.place(x=250, y=290, height=50, width=70)
l8c = tk.Button(win, text="e", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("e"))
l8c.place(x=250, y=350, height=50, width=70)
l8n = tk.Button(win, text="π", font=("Time in romana", 20, "bold"), bg="#c5ccd3", command=lambda: press("pi("))
l8n.place(x=250, y=410, height=50, width=70)

# fifth column
l5 = tk.Button(win, text="+", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("+"))
l5.place(x=330, y=110, height=50, width=70)
l5a = tk.Button(win, text="-", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("-"))
l5a.place(x=330, y=170, height=50, width=70)
l5c = tk.Button(win, text="*", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("*"))
l5c.place(x=330, y=230, height=50, width=70)
l5b = tk.Button(win, text="=", font=("Time in romana", 25, "bold"), bg="#ffa500", command=lambda: equal())
l5b.place(x=330, y=350, height=110, width=70)
l5f = tk.Button(win, text="/", font=("Time in romana", 25, "bold"), bg="#c5ccd3", command=lambda: press("/"))
l5f.place(x=330, y=290, height=50, width=70)

win.mainloop()

