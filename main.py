from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog


from sql import SQLHelper

sql = SQLHelper()

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

def admin_login(window = window): 
    '''admin login page
    A function that allows for a user to login with the inputs. Thif function is for admin users.

    Inputs:
        window ( TK = window object ): the main window object for your page
    Returns:
        frame (window): returns a frame that contains the login page.

    '''
        
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

    return log_in_frame

def signup_page(window = window):
    '''signup page
    A function that allows for a user to signup with the inputs

    Inputs:
        window ( TK = window object ): the main window object for your page
    Returns:
    fame (window): returns a frame that contains the signup page.

    '''
        
    sign_up_frame = Frame(window)

    # window.title("Sign up")

    Label(sign_up_frame, text="Sign up", width=13, font=("arial", 20)).grid(column=3,
                                                                    row=1)

    Label(sign_up_frame, text="Display name").grid(column=2, row=2)
    name = Entry(sign_up_frame, width=26)
    name.insert(0, "malcolm")

    Label(sign_up_frame, text="Username").grid(column=2, row=3)
    username = Entry(sign_up_frame, width=26)
    username.insert(0, "malcolm")


    Label(sign_up_frame, text="Password").grid(column=2, row=4)
    password = Entry(sign_up_frame, show="*", width=26)
    password.insert(0, "Malcolmstone18")


    Label(sign_up_frame, text="email").grid(column=2, row=5)
    email = Entry(sign_up_frame, width=26)
    email.insert(0, "mstone@coolmail.com")


    button = Button(sign_up_frame, text="enter")


    name.grid(column=3, row=2)
    username.grid(column=3, row=3)

    password.grid(column=3, row=4)
    email.grid(column=3, row=5)



    button.grid(column=3, row=6)

    return sign_up_frame



user_sql = [
    sql.call_row("id", "INTEGER", False, False, '', '', True),
    sql.call_row("dip_name", "VARCHAR(255)"),
    sql.call_row("username", "VARCHAR(100)", False, True),
    sql.call_row("password", "VARCHAR(255)"),
    sql.call_row("email", "VARCHAR(255)", False, True),
    sql.call_row("type", "VARCHAR(100)", default='basic', is_null=True),
    sql.call_row("admin_id", "VARCHAR(100)", default='', is_null=True),
    sql.call_row("deleted", "DATE", default='current_date'),
    sql.call_forgen(key="admin_id", foreign_table = "admin", foreign_column = "pwd" )
]

admin_sql = [
        sql.call_row("id", "INTEGER", False, False, '', '', True),
        sql.call_row("pwd", "VARCHAR(255)", is_unique=True)

]

sql.conect("users.sqlite")

sql.run(sql.create_table("admin", ','.join(admin_sql)))
sql.run(sql.create_table("users", ','.join(user_sql)))



#login_page(window).place(x=5, y=0)
#admin_login(window).place(x=5, y=0)
# window.mainloop()


