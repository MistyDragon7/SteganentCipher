#ImagebasedSteganography.py
#Steganography is the process of hiding text into an image by editing its pixels. The results are invisible to the naked eye

from tkinter import *
from PIL import ImageTk, Image #PIL is Pillow Module
import pyperclip as pc

#PIL Module is used to extract the pixels of an image and edit it

#import mysql.connector
#from mysql.connector import Error

from datetime import datetime


 def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
       print("MySQL Database connection successful")
    except Error as err:
       print(f"Error: '{err}'")

    return connection

connection = create_db_connection("localhost", "root", "1234", "steganentcipher")

window=Tk()
window.title("Image based Steganography")
window.configure(bg="white")

label=Label(window, text="Please select from the options below",font=("Arial Bold",12),bg="white")
label.grid(column=0,row=0)

def handle_click(event):
    a=Label(window,text="Enter the text which you want to hide:",font=("Arial Bold",10),bg="white")
    a.grid(column=0,row=3)
    rep = Entry(window,width=20) #Creating an empty data field
    rep.grid(column=1,row=3)
    b=Label(window,text="Enter the name of the image in which you want to hide the file:",font=("Arial Bold",10),bg="white")
    b.grid(column=0,row=5)
    rep2= Entry(window,width=20)
    rep2.grid(column=1,row=5)
    c=Label(window,text="Enter the path of the image in which you want to hide the file(excluding the file name):",font=("Arial Bold",10),bg="white")
    c.grid(column=0,row=6)
    rep3= Entry(window,width=20)
    rep3.grid(column=1,row=6)

    def handle_click(event):
        repl=rep.get()
        repl2=rep2.get()
        repl3=rep3.get()+"\\"+repl2 #creating a full file path from name and location
        import stepic
        im=Image.open(repl3)
        secret=stepic.encode(im,bytes(repl,'utf8'))
        ni=repl3.replace(repl2,"Steganentcipher.png")
        secret.save(ni,"PNG")
        pc.copy(ni)  #Copying secret file path
        now = datetime.now()
    button = Button(window,text="Enter",font=("Comic Sans MS Bold",10),bg="light green",fg="white")
    button.grid(column=2,row=8)
    button.bind("<Button-1>", handle_click)

button = Button(window,text="Hide text",font=("Comic Sans MS Bold",10))
button.grid(column=1,row=1)
button.bind("<Button-1>", handle_click)

def handle_click(event):
    a=Label(window,text="Enter the path of the image in which the text is hidden(excluding the file name)",font=("Arial Bold",10),bg="white")
    a.grid(column=3,row=4)
    rep= Entry(window,width=20)
    rep.grid(column=4,row=4)
    b=Label(window,text="Enter the name of the image in which the text is hidden:",font=("Arial Bold",10),bg="white")
    b.grid(column=3,row=3)
    rep2= Entry(window,width=20)
    rep2.grid(column=4,row=3)
    def handle_click(event):
        repl=rep.get()+"//"+rep2.get()
        import stepic
        im2=Image.open(repl)
        a=Label(window,text="The text hidden in the image is:",font=("Arial Bold",10))
        a.grid(column=3,row=5)
        b=Label(window,text=stepic.decode(im2),font=("Arial Bold",10))
        b.grid(column=3,row=6)   
        pc.copy(stepic.decode(im2)) #copy hidden text
    button = Button(window,text="Enter",font=("Comic Sans MS Bold",10),bg="light green",fg="white")
    button.grid(column=4,row=5)
    button.bind("<Button-1>", handle_click)

button = Button(window,text="Reveal the text hidden",font=("Comic Sans MS Bold",10))
button.grid(column=3,row=1)
button.bind("<Button-1>", handle_click)

