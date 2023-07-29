


from tkinter import *
from cryptography.fernet import Fernet
import pyperclip as pc
import mysql.connector

from mysql.connector import Error

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

connection= create_db_connection("localhost", "root", "1234", "steganentcipher")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(*query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

window= Tk()
window.title("AES Encryption")
window.configure(bg="white")

label=Label(window, text="Please select from options below", font=("Arial Bold", 10), bg="white")
label.grid(column=0, row=3)

def handle_click(event):
    a = Label(window, text="Enter message to be encrypted")
    a.grid(column=3, row=4)
    rep=Entry(window,width=20)
    rep.grid(column=4,row=4)
    
    def handle_click(event):
        repl1=rep.get()
        key = Fernet.generate_key()
        f =Fernet(key)
        repl1 = bytes(repl1, 'utf-8')
        token = f.encrypt(repl1)
        print("The encrypted data is:")
        decoded = token.decode()
        pc.copy(token.decode())
        print(token.decode())
        now = datetime.now()
        decoded_key = key.decode()
        print("The encryption key is:")
        print(decoded_key)

        now = datetime.now()

        sql = """INSERT INTO fernet(
            hashed_data, date_time)
            VALUES (%s, %s);""", (decoded, now)
        execute_query(connection, sql)

    button = Button(window,text="Enter",font=("Comic Sans MS Bold",10),bg="light green",fg="white")
    button.grid(column=2,row=8)
    button.bind("<Button-1>", handle_click)

button = Button(window,text="Hide text",font=("Comic Sans MS Bold",10))
button.grid(column=1,row=1)
button.bind("<Button-1>", handle_click)


def handle_click(event):
    a = Label(window, text="Enter the encrypted message")
    a.grid(column=3,row=4)
    rep=Entry(window, width=20)
    rep.grid(column=4,row=4)
    b=Label(window,text="Enter the encryption key")
    b.grid(column=3,row=6)
    rep_1=Entry(window, width=20)
    rep_1.grid(column=4,row=6)

    def handle_click(event):
        key=rep_1.get()
        key_binary = key.encode('utf-8')
        raw_data = rep.get()
        binary_data = raw_data  .encode('utf-8')
        x = Fernet(key_binary)
        decrypted_data = x.decrypt(binary_data)
        data = decrypted_data.decode()
        pc.copy(data)
        print(data)


    button = Button(window,text="Enter",font=("Comic Sans MS Bold",10),bg="light green",fg="white")
    button.grid(column=6,row=8)
    button.bind("<Button-1>", handle_click)
    
button = Button(window,text="Show Hidden Text",font=("Comic Sans MS Bold",10))
button.grid(column=5,row=1)
button.bind("<Button-1>", handle_click)
    
