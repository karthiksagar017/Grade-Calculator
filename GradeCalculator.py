import tkinter
from tkinter import *

root = Tk()
root.title("Grade Calculator")
root.geometry("500x400")

def calculation():
    english= int(englishentry.get())
    maths=int(mathsentry.get())
    science=int(scienceentry.get())
    total=(english+maths+science)
    Label(text=f"{total}",font="arial 15 bold").place(x=250, y=140)
    average=int(total/3)
    Label(text=f"{average}",font="arial 15 bold").place(x=250, y=180)

    if(average>50):
        grade="PASSED"
    else:
        grade="FAILED"
    Label(text=f"{grade}",font="arial 15 bold").place(x=250, y=220)
    

sub1=Label(root,text="English",font="arial 10")
sub2=Label(root,text="Maths",font="arial 10")
sub3=Label(root,text="Science",font="arial 10")
total=Label(root,text="Total",font="arial 10")
avg=Label(root,text="Average",font="arial 10")
grade=Label(root,text="Grade",font="arial 10")

sub1.place(x=50, y=20)
sub2.place(x=50, y=60)
sub3.place(x=50, y=100)
total.place(x=50, y=140)
avg.place(x=50, y=180)
grade.place(x=50, y=220)

englishvalue=StringVar()
mathsvalue=StringVar()
sciencevalue=StringVar()

englishentry=Entry(root, textvariable=englishvalue, font="arial 15" , width=15)
mathsentry=Entry(root, textvariable=mathsvalue, font="arial 15" , width=15)
scienceentry=Entry(root, textvariable=sciencevalue, font="arial 15" , width=15)

englishentry.place(x=250, y=20)
mathsentry.place(x=250, y=60)
scienceentry.place(x=250, y=100)

Button(text="Calculate", font="arial 15", bg="white",bd=10, command=calculation).place(x=50, y=300)
Button(text="Exit", font="arial 15", bg="white",bd=10,width=8,command=lambda:exit()).place(x=250, y=300)

root.mainloop()
