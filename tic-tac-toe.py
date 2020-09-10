from tkinter import *
from tkinter import messagebox
master = Tk()
master.geometry("1555x1500+0+0")
master.title("X-O-X")
master.iconbitmap("c:/gui/xox.ico")
master.configure(background="gold2")

topframe=Frame(master,bg="gold2",pady=2,height=100,width=1350,relief=RIDGE)
topframe.grid(row=0,column=0)
labtitle=Label(topframe,font=('arial',60,'bold italic'),text="   X-0-X     THE ULTIMATE FUN GAME       ",bd=21,fg="olivedrab1",justify=CENTER)
labtitle.grid(row=0,column=0)
mainframe=Frame(master,bg="sienna2",bd=6,height=600,width=1555,relief=RIDGE)
mainframe.grid(row=2,column=0)
lf=Frame(mainframe,bg="sienna2",bd=10,height=500,width=750,relief=SUNKEN,padx=10,pady=2)
lf.grid(row=1,column=0)
topframe=Frame(master,bg="gold2",pady=2,height=100,width=1350,relief=RIDGE)
topframe.grid(row=1,column=0)




playerx=IntVar()
playerO=IntVar()

playerx.set(0)
playerO.set(0)

buttons = StringVar()
click= True


def checker(buttons):
    global click
    if buttons["text"] == "" and click==True:
        buttons["text"]="X"
        click=False
        scorekeeper()
    elif buttons["text"] == "" and click==False:
        buttons["text"]="O"
        click=True
        scorekeeper()


def scorekeeper():
    if (btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X"):
        btn1.configure(background="pink")
        btn2.configure(background="pink")
        btn3.configure(background="pink")
        res=messagebox.showinfo("winner", "palyer X won the game")
        if(res=="ok"):
            clr()
        else:
            pass


    elif(btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X"):
        btn4.configure(background="pink")
        btn5.configure(background="pink")
        btn6.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer X won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X"):
        btn7.configure(background="pink")
        btn8.configure(background="pink")
        btn9.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer X won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X"):
        btn1.configure(background="pink")
        btn5.configure(background="pink")
        btn9.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer X won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X"):
        btn3.configure(background="pink")
        btn5.configure(background="pink")
        btn7.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer X won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X"):
        btn1.configure(background="pink")
        btn4.configure(background="pink")
        btn7.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer X won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X"):
        btn2.configure(background="pink")
        btn5.configure(background="pink")
        btn8.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer X won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X"):
        btn3.configure(background="pink")
        btn6.configure(background="pink")
        btn9.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer X won the game")
        if (res == "ok"):
            clr()
        else:
            pass



    elif (btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O"):
        btn1.configure(background="pink")
        btn2.configure(background="pink")
        btn3.configure(background="pink")
        res=messagebox.showinfo("winner", "palyer O won the game")
        if (res=="ok"):
            clr()
        else:
            pass

    elif (btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O"):
        btn4.configure(background="pink")
        btn5.configure(background="pink")
        btn6.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer O won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O"):
        btn7.configure(background="pink")
        btn8.configure(background="pink")
        btn9.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer O won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O"):
        btn1.configure(background="pink")
        btn5.configure(background="pink")
        btn9.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer O won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O"):
        btn3.configure(background="pink")
        btn5.configure(background="pink")
        btn7.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer O won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O"):
        btn1.configure(background="pink")
        btn4.configure(background="pink")
        btn7.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer O won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O"):
        btn2.configure(background="pink")
        btn5.configure(background="pink")
        btn8.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer O won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    elif (btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O"):
        btn3.configure(background="pink")
        btn6.configure(background="pink")
        btn9.configure(background="pink")
        res = messagebox.showinfo("winner", "palyer O won the game")
        if (res == "ok"):
            clr()
        else:
            pass

    else:
        pass



def clr():
    btn1["text"] = ""
    btn2["text"] = ""
    btn3["text"] = ""
    btn4["text"] = ""
    btn5["text"] = ""
    btn6["text"] = ""
    btn7["text"] = ""
    btn8["text"] = ""
    btn9["text"] = ""

    btn1.configure(background="maroon1")
    btn2.configure(background="maroon1")
    btn3.configure(background="maroon1")
    btn4.configure(background="maroon1")
    btn5.configure(background="maroon1")
    btn6.configure(background="maroon1")
    btn7.configure(background="maroon1")
    btn8.configure(background="maroon1")
    btn9.configure(background="maroon1")


btn1=Button(lf,text="",font=("times",26, "bold"),height=3,width=8,bg="maroon1",command=lambda :checker(btn1))
btn1.grid(row=1,column=0,sticky=S+N+E+W)

btn2=Button(lf,text="",font=("times",26, "bold"),height=3,width=8,bg="maroon1",command=lambda :checker(btn2))
btn2.grid(row=1,column=1,sticky=S+N+E+W)

btn3=Button(lf,text="",font=("times",26, "bold"),height=3,width=8,bg="maroon1",command=lambda :checker(btn3))
btn3.grid(row=1,column=2,sticky=S+N+E+W)

btn4=Button(lf,text="",font=("times",26, "bold"),height=3,width=8,bg="maroon1",command=lambda :checker(btn4))
btn4.grid(row=2,column=0,sticky=S+N+E+W)

btn5=Button(lf,text="",font=("times",26, "bold"),height=3,width=8,bg="maroon1",command=lambda :checker(btn5))
btn5.grid(row=2,column=1,sticky=S+N+E+W)

btn6=Button(lf,text="",font=("times",26, "bold"),height=3,width=8,bg="maroon1",command=lambda :checker(btn6))
btn6.grid(row=2,column=2,sticky=S+N+E+W)

btn7=Button(lf,text="",font=("times",26, "bold"),height=3,width=8,bg="maroon1",command=lambda :checker(btn7))
btn7.grid(row=3,column=0,sticky=S+N+E+W)

btn8=Button(lf,text="",font=("times",26, "bold"),height=3,width=8,bg="maroon1",command=lambda :checker(btn8))
btn8.grid(row=3,column=1,sticky=S+N+E+W)

btn9=Button(lf,text="",font=("times",26, "bold"),height=3,width=8,bg="maroon1",command=lambda :checker(btn9))
btn9.grid(row=3,column=2,sticky=S+N+E+W)

btnclr=Button(master,text="RESET",bg="RED",command=clr)
btnclr.grid(row=4,column=0)

ml=Label(master,text="IF THE MATCH IS DRAW PRESS").grid(row=3,column=0)



master.mainloop()

