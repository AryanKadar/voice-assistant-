import va as vv
import time
from tkinter import *
rt=Tk()
rt.title("Voice Assistant")
rt.geometry("466x567")
rt.resizable(width=False,height=False)
p=PhotoImage(file="david.png")
l1=Label(rt,image=p,width=305,height=300).place(x=70,y=0)
text=Text(rt,width=51,height=12)
text.place(x=0,y=350)
text.configure(font=("Helvetica", 12))		
b=Button(rt,text="Play",command=lambda:[vv.vaa(text,rt,l1)],width=8,height=2,bg="blue",fg="white").place(x=190,y=300)
rt.mainloop()