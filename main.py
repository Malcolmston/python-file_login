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



def is_deleted(username):
    '''is deleted
    this function checks if a user has soft deleted there acoount
    Paremeters:
        username (str): the username of the user
    Returns:
        bool that is true if the user has soft deleted
    '''
    ans = sql.runRet( sql.select_limit("deleted", 'users','1', f'username = "{username}"') )[0]
    return False if (ans == None and ans == "None" and  ans == 'Null' and ans == 'null' and ans == 0) else True


def user_exsist(username):
    '''user_exsist
    a function that checks if a user exists by there username

    Parameter:
        username (str): username of the user
    Returns:
        Bool if the user exists; True, False otherwise
    '''
    ans = sql.runRet( sql.select_column("username", 'users', f'username = "{username}"') )
    return is_deleted(username) or ans is not None and len(ans) > 0 and ans is not [] 


def signup(dip_name, username,password, email):
    '''signup
    Parameters:
       dip_name (str): name of the user
       username (str): username of the user
       password (str): password of the user that will be hashed before entering the table
       email (str): email of the user
    
    Return:
        True if successful, False otherwise. 
    '''

    if not user_exsist(username):
        return False
    
    else:
        sql.run( 
        sql.insert("users", "dip_name, username, password, email, type, deleted",  f"'{dip_name}','{username}',hash('{password}',''),'{email}','basic'")
        )   
        return True




user_sql = [
    sql.call_row("id", "INTEGER", pk = True),
    sql.call_row("dip_name", "VARCHAR(255)"),
    sql.call_row("username", "VARCHAR(100)", False, True),
    sql.call_row("password", "VARCHAR(255)"),
    sql.call_row("email", "VARCHAR(255)", False, True),
    sql.call_row("type", "VARCHAR(100)", default='basic', is_null=True),
    sql.call_row("admin_id", "VARCHAR(100)", default='', is_null=True),
    sql.call_row("deleted", "DATE", is_null=True),
    sql.call_forgen(key="admin_id", foreign_table = "admin", foreign_column = "pwd" ),
    sql.check('type == "basic" OR type == "admin"'),
]

admin_sql = [
        sql.call_row("id", "INTEGER", pk = True),
        sql.call_row("pwd", "VARCHAR(255)", is_unique=True)

]


file_table = [
    sql.call_row("id", "INTEGER", pk=True),


    sql.call_row("path", "TEXT"),
    sql.call_row("name", "VARCHAR(255)",True, is_unique=True),

    sql.call_row("data", "BLOB"),
   

    sql.call_row("size", "INTEGER"),    

    sql.call_row("added", "DATE"),

    sql.call_row("created", "DATE"),
    sql.call_row("edited", "DATE"),

     sql.call_row("user_id", "INTEGER"),

    sql.call_row("deleted", "DATE", default='current_date'),


    sql.call_forgen(key="user_id", foreign_table = "users", foreign_column = "id" )
]


sql.conect("users.sqlite")

sql.run(sql.create_table("admin", ','.join(admin_sql)))
sql.run(sql.create_table("users", ','.join(user_sql)))
sql.run(sql.create_table("files", ','.join(file_table)))

# sql.run(  sql.insert("admin", "pwd", "'2er32'") )

password = "a"

def login(username, password, type = "basic") -> (bool):
    '''login
    allows a user to login with username and password

    Paremeters:
       username (str): username of the user
       password (str): password of the user that will be hashed before entering the table
        
    Returns:
        (Bool): True if login was successful or False otherwise
        '''
    if user_exsist(username):
        line =  sql.runRet(
    sql.select_column("dip_name, username, password, email, type", "users", f"hash('{password}','') == password AND username == '{username}'")
)
        return line is not [] and len(line) != 0 if line[0][4] == type else False 


def admin_login(username, password, uuid):
    '''Login
    a function that allows admin users to login
    '''
    user= sql.runRet(sql.select_column("id, type, admin_id", "users", f"username == '{username}'"))

    if user[0][1] == "admin":
     
        uuid = sql.runRet(sql.select_column("pwd", "admin",f"id == '{user[0][0]}' "))[0][0]
    
        ans = sql.runRet( sql.select_column("username", 'users', f'password == hash("{password}", "{uuid}")') )

        return login(username, ans+password, 'admin')
    else:
        return False


print( ans )

#login_page(window).place(x=5, y=0)
#admin_login(window).place(x=5, y=0)
# window.mainloop()


