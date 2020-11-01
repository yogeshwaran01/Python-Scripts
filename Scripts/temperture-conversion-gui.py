from tkinter import Tk, Button, Label, END, Entry

root = Tk()
root.title("Temperture conversion")


def convert():
    a = float(e1.get())
    e2.insert(0, a * (9 / 5) + 32)


def real():
    b = float(e2.get())
    c = b - 32
    e1.insert(0, c * (5 / 9))


def clear():
    e1.delete(0, END)
    e2.delete(0, END)


l1 = Label(text="celsius:".upper(), background="tan1")
l1.grid(row=2, column=0)
e1 = Entry(root, width=10, borderwidth=10)
e1.grid(row=2, column=1)
l2 = Label(text="fahrenheit:".upper(), background="tan1")
l2.grid(row=3, column=0)
e2 = Entry(root, width=10, borderwidth=10)
e2.grid(row=3, column=1)
btn = Button(root, text=" FAHRENHEIT", padx=20, pady=5, command=convert)
btn.grid(row=4, column=1)
bt = Button(root, text=" CELSIUS", padx=35, pady=5, command=real)
bt.grid(row=4, column=0)
clr = Button(root, text=" CLEAR", padx=40, pady=10, command=clear)
clr.grid(row=5, column=0)
go = Button(root, text=" QUIT", padx=40, pady=10, command=quit)
go.grid(row=5, column=1)

root.mainloop()