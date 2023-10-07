from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog


window = Tk()

window.geometry("600x600")


def login_page(window = window):
    '''Login page
    A function that allows for a user to login with the inputs

    Inputs:
        window ( TK = window object ): the main window object for your page
    Returns:
    fame (window): returns a frame that contains the login page.

    '''
    log_in_frame = Frame(window)


    Label(log_in_frame , text="Log in", width=13,font=("arial",20)).grid(column=3, row=1)


    Label(log_in_frame , text="Username").grid(column=2, row=2)
    username = Entry(log_in_frame, width=26)
    username.insert(0, "malcolm")

    Label(log_in_frame , text="Password").grid(column=2, row=3)
    password = Entry(log_in_frame , show="*", width=26)
    password.insert(0, "Malcolmstone18")


    button = Button(log_in_frame, text= "enter")


    username.grid(column=3, row=2)
    password.grid(column=3, row=3)

    button.bind("<Button-1>", print)

    button.grid(column=3, row=4)

    return log_in_frame

log_in_frame = Frame(window)


Label(log_in_frame , text="Admin Log in", width=13,font=("arial",20)).grid(column=3, row=1)


Label(log_in_frame , text="Username").grid(column=2, row=2)
username = Entry(log_in_frame, width=26)
username.insert(0, "malcolm")

Label(log_in_frame , text="Password").grid(column=2, row=3)
password = Entry(log_in_frame , show="*", width=26)
password.insert(0, "Malcolmstone18")

Label(log_in_frame , text="Admin id").grid(column=2, row=4)
admin_id = Entry(log_in_frame , width=26)
admin_id.insert(0, "pq12#2")

button = Button(log_in_frame, text= "enter")


username.grid(column=3, row=2)
password.grid(column=3, row=3)
admin_id.grid(column=3, row=4)

button.bind("<Button-1>", print)

button.grid(column=3, row=5)




#login_page(window).place(x=5, y=0)
log_in_frame.place(x=5, y=0)
window.mainloop()