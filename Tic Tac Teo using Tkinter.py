from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkFont


game = Tk()
game.title("Tic Tac Teo")
tag1 = "O"
tag2= "X"
counter = 0
board=["0","1","2","3","4","5","6","7","8"]
f1 = tkFont.Font(family='Helvetica', size=25, weight='bold')
def click(id):
    global counter
    if counter % 2 == 0:
        board[id]= tag2
    elif counter % 2 != 0:
        board[id]= tag1
    update(id)
    header2.grid(row=1,column=0, columnspan=3)
    print(board)
    counter += 1
    if counter > 4:
        check()

def check ():
    msg1="Congrats Player "+ board[0] +" Won The Game !!! "
    msg2="Congrats Player "+ board[4] +" Won The Game !!! "
    msg3="Congrats Player "+ board[8] +" Won The Game !!! "
    msg4="Congrats Player "+ board[2] +" Won The Game !!! "
    msg5="waw It seems we have a DRAW ! "
    if board[1] == board[2] == board[0] or board[0] == board[4] == board[8] or board[0] == board[3] == board[6]:
        messagebox.showinfo(title="Winner Winner Chicken Dinner  ", message=msg1)
    elif board[1] == board[4] == board[7] or board[3] == board[4] == board[5]:
        messagebox.showinfo(title="Winner Winner Chicken Dinner  ", message=msg2)
    elif board[2] == board[5] == board[8] or board[6] == board[7] == board[8]:
        messagebox.showinfo(title="Winner Winner Chicken Dinner  ", message=msg3)
    elif board[2] == board[4] == board[6]:
        messagebox.showinfo(title="Winner Winner Chicken Dinner  ", message=msg4)
    elif counter > 8:
        messagebox.showinfo(title="Equally smart or Equally Stupid : ) ", message=msg5)




header = Label(game, text="Welcom To Tic Tac Teo", font=f1)
header.grid(row=0,column=0, columnspan=3)

b0 = Button(game, text=" ", borderwidth=4, padx=55, pady= 50, command=lambda: click(0), font=f1, fg="black" )
b0.grid(row=2, column= 0)
b1 = Button(game, text=" ", borderwidth=4, padx=55, pady= 50, command=lambda: click(1), font=f1  )
b1.grid(row=2, column= 1)
b2 = Button(game, text=" ", borderwidth=4, padx=55, pady= 50, command=lambda: click(2), font=f1  )
b2.grid(row=2, column= 2)
b3 = Button(game, text=" ", borderwidth=4, padx=55, pady= 50, command=lambda: click(3), font=f1  )
b3.grid(row=3, column= 0)
b4 = Button(game, text=" ", borderwidth=4, padx=55, pady= 50, command=lambda: click(4), font=f1  )
b4.grid(row=3, column= 1)
b5 = Button(game, text=" ", borderwidth=4, padx=55, pady= 50, command=lambda: click(5), font=f1  )
b5.grid(row=3, column= 2)
b6 = Button(game, text=" ", borderwidth=4, padx=55, pady= 50, command=lambda: click(6), font=f1  )
b6.grid(row=4, column= 0)
b7 = Button(game, text=" ", borderwidth=4, padx=55, pady= 50, command=lambda: click(7), font=f1  )
b7.grid(row=4, column= 1)
b8 = Button(game, text=" ", borderwidth=4, padx=55, pady= 50, command=lambda: click(8), font=f1  )
b8.grid(row=4, column= 2)

def update(id):
    if id == 0:
        if counter % 2 == 0:
            b0.config( fg="red", text= tag2)
        elif counter % 2 != 0:
            b0.config(fg="blue", text= tag1)
        b0.config(state=DISABLED, bg="light gray")

    elif id == 1:
        if counter % 2 == 0:
            b1.config(text= tag2, fg="red")
        elif counter % 2 != 0:
            b1.config(text= tag1, fg="blue")
        b1.config(state=DISABLED, bg="light gray")
    elif id == 2:
        if counter % 2 == 0:
            b2.config(text= tag2)
        elif counter % 2 != 0:
            b2.config(text= tag1)
        b2.config(state=DISABLED, bg="light gray")
    elif id == 3:
        if counter % 2 == 0:
            b3.config(text= tag2)
        elif counter % 2 != 0:
            b3.config(text= tag1)
        b3.config(state=DISABLED, bg="light gray")
    elif id == 4:
        if counter % 2 == 0:
            b4.config(text= tag2)
        elif counter % 2 != 0:
            b4.config(text= tag1)
        b4.config(state=DISABLED, bg="light gray")
    elif id == 5:
        if counter % 2 == 0:
            b5.config(text= tag2)
        elif counter % 2 != 0:
            b5.config(text= tag1)
        b5.config(state=DISABLED, bg="light gray")
    elif id == 6:
        if counter % 2 == 0:
            b6.config(text= tag2)
        elif counter % 2 != 0:
            b6.config(text= tag1)
        b6.config(state=DISABLED, bg="light gray")
    elif id == 7:
        if counter % 2 == 0:
            b7.config(text= tag2)
        elif counter % 2 != 0:
            b7.config(text= tag1)
        b7.config(state=DISABLED, bg="light gray")
    elif id == 8:
        if counter % 2 == 0:
            b8.config(text= tag2)
        elif counter % 2 != 0:
            b8.config(text= tag1)
        b8.config(state=DISABLED, bg="light gray")


game.mainloop()
