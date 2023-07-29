#mainprog.py
from tkinter import *
#importing a Tkinter Window and Configuring

window = Tk()
window.title("Steganentcipher")
window.configure(bg="white")

#creating A Label To display Main text

label = Label(window, text=''' Welcome to Steganetcipher!!! Please select from the options below''',font=("Comic Sans MS ",12),bg="white")
label.grid(column=1,row=0)
def handle_click(event):
    import ciphers #Imported a File for a specific action created in the same directory  
button = Button(window,text=" Caesar's Cipher",font=("Comic Sans MS Bold",10),relief=FLAT,bg="black",fg="white")
button.grid(column=0,row=3)
button.bind("<Button-1>", handle_click)
def handle_click(event):
    import ImagebasedSteganography
button2 = Button(window,text="Image based Steganography(hiding files inside images)",font=("Comic Sans MS Bold",10),relief=FLAT,bg="black",fg="white")
button2.bind("<Button-1>", handle_click)
button2.grid(column=2,row=3)
def handle_click(event):
    import Fernet
button3=Button(window, text="AES Encryption",font=("Comic Sans MS Bold",10),relief=FLAT,bg="black",fg="white")
button3.bind("<Button-1>", handle_click)
button3.grid(column=1,row=4)
window.mainloop()


#mainprog.py

from tkinter import *

#importing a Tkinter Window and Configuring

window = Tk()
window.title("Steganentcipher")
window.configure(bg="white")

#creating A Label To display Main text

label = Label(window, text=''' Welcome to Steganetcipher!!! Please select from the options below''',font=("Comic Sans MS ",12),bg="white")

label.grid(column=1,row=0)

def handle_click(event):
    import ciphers #Imported a File for a specific action created in the same directory  

button = Button(window,text=" Caesar's Cipher",font=("Comic Sans MS Bold",10),relief=FLAT,bg="black",fg="white")
button.grid(column=0,row=3)
button.bind("<Button-1>", handle_click)

def handle_click(event):
    import ImagebasedSteganography

button2 = Button(window,text="Image based Steganography(hiding files inside images)",font=("Comic Sans MS Bold",10),relief=FLAT,bg="black",fg="white")
button2.bind("<Button-1>", handle_click)
button2.grid(column=2,row=3)

def handle_click(event):
    import Fernet

button3=Button(window, text="AES Encryption",font=("Comic Sans MS Bold",10),relief=FLAT,bg="black",fg="white")
button3.bind("<Button-1>", handle_click)
button3.grid(column=1,row=4)

window.mainloop()
#End of the main program
