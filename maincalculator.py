from tkinter import Button, END, Text, Tk
import re
from math import sqrt

root = Tk()
root.title("calculator")
root.geometry("420x400+450+50")
root.configure(bg="black")
root.resizable(width=0, height=0)


def calculate():
    get_all = entry.get(1.0, END)
    value = get_all
    value = re.sub(u"\u00F7", "/", value)
    value = re.sub("X", "*", value)
    value = re.sub("%", "/100", value)
    answer = eval(value)
    entry.delete(1.0, END)
    entry.insert(1.0, answer)

def remove():
    current_text = entry.get(1.0, END).strip()
    updated_text = current_text[:-1]
    entry.delete(1.0, END)
    entry.insert(1.0, updated_text)

def clear():
    entry.delete(1.0, END)


def buttons(text):
    entry.insert(END, text)


def squareroot():
    get_all = entry.get(1.0, END)
    value = get_all
    answer = sqrt(int(value))
    entry.delete(1.0, END)
    entry.insert(1.0, answer)


entry = Text(root, width=31, height=2, bg="white", bd=10, font="5")
entry.place(x=32, y=10)


def all_buttons():
    button_nine = Button(root, text="9", width=7, bd=5,
                         font="1", bg="white", command=lambda: buttons("9"))
    button_nine.place(x=30, y=100)
    button_eight = Button(root, text="8", width=7, bd=5,
                          font="1", bg="white", command=lambda: buttons("8"))
    button_eight.place(x=120, y=100)
    button_seven = Button(root, text="7", width=7, bd=5,
                          font="1", bg="white", command=lambda: buttons("7"))
    button_seven.place(x=210, y=100)
    button_six = Button(root, text="6", width=7, bd=5,
                        font="1", bg="white", command=lambda: buttons("6"))
    button_six.place(x=30, y=150)
    button_five = Button(root, text="5", width=7, bd=5,
                         font="1", bg="white", command=lambda: buttons("5"))
    button_five.place(x=120, y=150)
    button_four = Button(root, text="4", width=7, bd=5,
                         font="1", bg="white", command=lambda: buttons("4"))
    button_four.place(x=210, y=150)
    button_three = Button(root, text="3", width=7, bd=5,
                          font="1", bg="white", command=lambda: buttons("3"))
    button_three.place(x=30, y=200)
    button_two = Button(root, text="2", width=7, bd=5,
                        font="1", bg="white", command=lambda: buttons("2"))
    button_two.place(x=120, y=200)
    button_one = Button(root, text="1", width=7, bd=5,
                        font="1", bg="white", command=lambda: buttons("1"))
    button_one.place(x=210, y=200)
    button_zero = Button(root, bg="white", text="0", width=7, bd=5,
                         font="1", command=lambda: buttons("0"))
    button_zero.place(x=30, y=250)
    button_dot = Button(root, text=u"\u2022", width=7, bd=5,
                        font="1", bg="yellow", command=lambda: buttons("."))
    button_dot.place(x=120, y=250)
    button_plus = Button(root, text="+", width=7, bd=5,
                         font="1", bg="yellow", command=lambda: buttons("+"))
    button_plus.place(x=300, y=250)
    button_minus = Button(root, text="-", width=7, bd=5,
                          font="1", bg="yellow", command=lambda: buttons("-"))
    button_minus.place(x=300, y=200)
    button_div = Button(root, text=u"\u00F7", width=7, bd=5,
                        font="1", bg="yellow", command=lambda: buttons(u"\u00F7"))
    button_div.place(x=300, y=100)
    button_multi = Button(root, text="x", width=7, bd=5,
                          font="1", bg="yellow", command=lambda: buttons("X"))
    button_multi.place(x=300, y=150)
    button_squareroot = Button(root, text=u'\u221a', width=7, bd=5,
                               font="1", height=2, bg="yellow", command=lambda: squareroot())
    button_squareroot.place(x=30, y=300)
    button_percent = Button(root, text="%", width=7, bd=5,
                            font="1", bg="yellow", command=lambda: buttons("%"))
    button_percent.place(x=210, y=250)
    button_clear = Button(root, text="AC", width=7, bd=5,
                          font="1", height=2, bg="yellow", command=lambda: clear())
    button_clear.place(x=120, y=300)
    button_remove = Button(root, text="\u232B", width=7, bd=5,
                          font="1", height=2, bg="yellow", command=lambda: remove())
    button_remove.place(x=210, y=300)
    button_calc = Button(root, text="=", width=7, height=2,
                         bd=5, font="1", bg="yellow", command=calculate)
    button_calc.place(x=300, y=300)


all_buttons()

root.mainloop()
