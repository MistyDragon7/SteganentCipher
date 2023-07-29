#ciphers.py
from tkinter import *
import pyperclip as pc


from datetime import datetime
#Current datetime
now=datetime.now()
window=Tk()
window.title("Caesar's Cipher")

window.configure(bg="white")

a=Label(window,text="Enter the string which you want to use:",font=("Arial Bold",10))
a.grid(column=0,row=0)
rep= Entry(window,width=20)
rep.grid(column=1,row=0)
d=Label(window,text="Enter the shift pattern:",font=("Arial Bold",10))
d.grid(column=0,row=1)
rep2= Entry(window,width=20)
rep2.grid(column=1,row=1)

def handle_click(event):
        repl=rep.get()
        repl2=int(rep2.get())
        b=len(repl)
        f=''
        for i in range(b):
            c=ord(repl[i])
            e=repl2+c
            g=chr(e)
            f+=g
        b=Label(window,text=f,font=("Arial Bold",10))
        b.grid(column=1,row=4) 
        pc.copy(f)  #Copies the resultant encrypted message 
        now=datetime.now()
button = Button(window,text="Enter",font=("Comic Sans MS Bold",10),bg="light green",fg="white")
button.grid(column=0,row=3)
button.bind("<Button-1>", handle_click)
