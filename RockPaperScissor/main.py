# Requires Pillow Library

from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()
root.geometry('600x600')
root.resizable(False, False)
root.title('Rock Paper and Scissors')
root.config(bg='cyan')
Label(root, text="Rock, Paper and Scissors", font=("Times", "30", "bold"), bg="cyan").pack(pady=7)
playerchoose = Label(root, text="Choose Your Option", font=("Times", "20", "bold"), bg="cyan", fg="red")
playerchoose.pack(pady=10)
userchoice = ""

uc=0

def rocks():
    userchoice = "rock"
    uc = 1
    print(uc)


def scissors():
    userchoice = "scissor"
    uc = 2
    print(uc)


def papers():
    userchoice = "paper"
    uc = 3
    print(uc)


def destroybuttons():
    b1.place_forget()
    b2.place_forget()
    b3.place_forget()
    playerchoose.pack_forget()
    choosingText.place(x=175, y=150)
    cpuChoose()


choosingText = Label(root, text="CPU is Choosing\n\nPlease Wait", font=("Times", "25", "bold"), bg="cyan", fg="red")

rock = Image.open('rock.png')
rock = rock.resize((100, 100), Image.ANTIALIAS)
rock = ImageTk.PhotoImage(rock)
b1 = Button(root, image=rock, command=lambda: [rocks(), destroybuttons()])
b1.place(x=75, y=150)

scissor = Image.open('scissor.png')
scissor = scissor.resize((100, 100), Image.ANTIALIAS)
scissor = ImageTk.PhotoImage(scissor)
b2 = Button(root, image=scissor, command=lambda: [scissors(), destroybuttons()])
b2.place(x=250, y=150)

paper = Image.open('paper.png')
paper = paper.resize((100, 100), Image.ANTIALIAS)
paper = ImageTk.PhotoImage(paper)
b3 = Button(root, image=paper, command=lambda: [papers(), destroybuttons()])
b3.place(x=425, y=150)

cpuchoice = ""
paperImage = Label(root, image=paper)
scissorImage = Label(root, image=scissor)
rockImage = Label(root, image=rock)


def finalResult():
    result = StringVar()
    if uc == cc:
        result = "TIE!"
    elif uc == 1 and cc == 2:
        result = "YOU WIN!"
    elif uc == 1 and cc == 3:
        result = "YOU LOSE!"
    elif uc == 2 and cc == 1:
        result = "YOU LOSE!"
    elif uc == 2 and cc == 3:
        result = "YOU WIN!"
    elif uc == 3 and cc == 1:
        result = "YOU WIN!"
    elif uc == 3 and cc == 2:
        result = "YOU LOSE!"
    L3 = Label(root, text=result, font=("Times", "20", "bold"), bg="cyan", fg="red")
    L3.after(3000, L3.place(x=250, y=400))


cc = 0


def cpuChoose():
    cc = random.randint(1, 3)
    choosingText.after(3000, lambda: choosingText.place_forget())
    print(uc,cc)
    l2 = Label(root, text="CPU Chose:", font=("Times", "20", "bold"), bg="cyan", fg="red")
    l2.after(3000, lambda: l2.place(x=100, y=250))
    if cc == 1:
        cpuchoice = "rock"
        rockImage.after(3000, lambda: [rockImage.place(x=300, y=225), finalResult()])
    elif cc == 2:
        cpuchoice = "scissor"
        scissorImage.after(3000, lambda: [scissorImage.place(x=300, y=225), finalResult()])

    else:
        cpuchoice = "paper"
        paperImage.after(3000, lambda: [paperImage.place(x=300, y=225), finalResult()])


root.mainloop()
