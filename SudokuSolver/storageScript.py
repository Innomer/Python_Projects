import os
from tkinter import *
import json
from tkinter.scrolledtext import ScrolledText
from turtle import width

from pyparsing import col

def Add(frame,category,fileLoc,details,aCDVar):
    details.append(f'{aCDVar}')
    with open(f'{fileLoc}','w') as f:
        f.write(json.dumps(details))
    if category=="Bank":
        Bank(frame)
    elif category=="Mutual Funds":
        MF(frame)
    elif category=="Insurance":
        IS(frame)
    elif category=="Mediclaim":
        MC(frame)
    elif category=="Loans":
        Loans(frame)
    elif category=="Share Market":
        SM(frame)
    


def generalLayout(frame,category,fileLoc,details=[]):
    categoryOptions=StringVar()
    global addButton
    categoryDrop=OptionMenu(frame,categoryOptions,*details)
    categoryDrop.grid(row=2,column=360,pady=10)
    aCDVar=StringVar()
    detailsToPass=details
    if addButton==True:
        Label(frame,text="ADD "+category,font=("Times","15","normal")).grid(column=360,pady=(100,0))
        addCategoryDetail=Entry(frame,textvariable=aCDVar,font=("Times","12","normal"),bg='cyan',width=50)
        addCategoryDetail.grid(row=100,column=360)
        aCDButton=Button(frame,text='ADD',font=("Times","15","normal"),command=lambda:Add(frame,category,fileLoc,detailsToPass,aCDVar=aCDVar.get()))
        aCDButton.grid(row=101,column=360)
        addButton=False
    



def Bank(frame):
    bankNameList=[]
    with open(f'SudokuSolver\\BNL.txt','r') as f:
        bankNameList=json.loads(f.read())
    generalLayout(frame,"Bank",'SudokuSolver\\BNL.txt',bankNameList)
def MF(frame):
    MFList=[]
    with open(f'SudokuSolver\\MFL.txt','r') as f:
        MFList=json.loads(f.read())
    generalLayout(frame,"Mutual Funds",'SudokuSolver\\MFL.txt',MFList)
def IS(frame):
    ISList=[]
    with open(f'SudokuSolver\\ISL.txt','r') as f:
        ISList=json.loads(f.read())
    generalLayout(frame,"Insurance",'SudokuSolver\\ISL.txt',ISList)
def MC(frame):
    MCList=[]
    with open(f'SudokuSolver\\MCL.txt','r') as f:
        MCList=json.loads(f.read())
    generalLayout(frame,"Mediclaims",'SudokuSolver\\MCL.txt',MCList)
def Loans(frame):
    LoansList=[]
    with open(f'SudokuSolver\\LL.txt','r') as f:
        LoansList=json.loads(f.read())
    generalLayout(frame,"Loans",'SudokuSolver\\LL.txt',LoansList)
def SM(frame):
    SMList=[]
    with open(f'SudokuSolver\\SML.txt','r') as f:
        SMList=json.loads(f.read())
    generalLayout(frame,"Share Market",'SudokuSolver\\SML.txt',SMList)




def getUploadType(frame,type_clicked="Bank"):
    if type_clicked=="Bank":
        Bank(frame)
    elif type_clicked=="Mutual Funds":
        MF(frame)
    elif type_clicked=="Insurance":
        IS(frame)
    elif type_clicked=="Mediclaim":
        MC(frame)
    elif type_clicked=="Loans":
        Loans(frame)
    elif type_clicked=="Share Market":
        SM(frame)


root=Tk()
root.geometry("1280x720")
root.resizable(False,False)
root.title('Home Storage Program')
root.config(bg='grey')
frame=Frame(root)
frame.pack(side="top",expand=True,fill="both")
Label(frame,text="Sudoku Solver",font=("Times","30","bold")).grid(row=0,column=360,pady=10)

drop_options=[
    "Bank",
    "Mutual Funds",
    "Insurance",
    "Mediclaim",
    "Loans",
    "Share Market"
]

type_clicked=StringVar()
addButton=True

drop=OptionMenu(frame,type_clicked,*drop_options,command=lambda type_clicked:getUploadType(frame,type_clicked))
drop.grid(row=1,column=360,pady=10)

root.mainloop()