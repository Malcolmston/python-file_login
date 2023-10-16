import sqlite3
import numpy
import re

from validation import hide_password

# replace all the charicters in a string with a new charicter
def replace_all(sub, new_line, string):
    org = string  # unmadified string for forever problom
    i = 0
    while (sub in string):
        string = string.replace(sub, new_line)

        if i >= len(org):
            return string

        i += 1

    return string


class SQLHelper:

    def __init__(self, databace=None, name=None, cursor=None, conn=None):
        self.databace = databace
        self.name = name
        self.cursor = cursor
        self.conn = conn

    # allows for a user to connect there server
    def conect(self, name):
        conn = sqlite3.connect(name)


        conn.create_function("hash", 2, hide_password)

        cursor = conn.cursor()
        self.name = name
        self.cursor = cursor
        self.conn = conn

    def execute(self, run, key):
        self.conn.execute(run, key)
        self.conn.commit()

    
        # runs a line a sql code
   
    def run(self, txt, *extra):
        try:
            if extra:
                print(txt, extra )
                self.conn.execute(txt, extra)
            else:
                self.conn.execute(txt)

            self.conn.commit()
            return True
        except NameError:
            print(NameError)
            return False
        
    def check(self, if_statement = ''):
        expression = f"CHECK( {if_statement} )"
        
        return expression

    # runs a line a sql code with an expected output
    def runRet(self, txt):
        try:
            res = self.conn.execute(txt)
            # maps over the array of truples. the list is then converted from a array object to an array of arrays
            return numpy.array(
                list(map((lambda tru: numpy.asarray(tru)), res.fetchall())))
        except NameError:
            return False

    # returns the statement to create a table. the input arr varible should have name, statements
    def create_table(self, name, row_info):
        expresion = f"CREATE TABLE IF NOT EXISTS {name} ({row_info})"

        return expresion
    
        # allows user to insert a row into a sqlite table
   
    # allows for a user to create rows for a table
    def call_row(self,
                 name_tag=None,
                 data_type=None,
                 is_null=False,
                 is_unique=False,
                 default='',
                 pk=False):

        if (data_type == None):
            return ""
        elif (is_unique == True and is_null == True):
            #warning clause
            print(
                "this key may only have 1 null value. This will not be an ishue; however, you may want to consider removing the is_null parameter."
            )
        elif (is_null == True and not (default == '')):
            #warning clause
            print(
                "the default clause will always be run if a case is null. consider removing the is null parameter."
            )

        expresion = f"{name_tag} {data_type} {'' if is_null else 'NOT NULL '} {'UNIQUE ' if is_unique else ' '} {'PRIMARY KEY ' if pk else' '}"

        return replace_all("  ", " ", expresion)[:-1]

    # sets forgen key update and change types
    def foreign_func(self, type = 0 ):
        if type == 'null' or type == 'none' or type == None or type == 'Null' or type == 'empty':
            return "SET NULL"
        elif type == 'default' or type == 'def' or type == 'norm' or type == 'auto':
            return "SET DEFAULT"
        elif type == 'restrict' or type == 'rest' or type == 'lim' or type == 'limit' or type == 'block':
            return "RESTRICT"
        elif type == 'no' or type == '':
            return "NO ACTION"
        elif type == 'cascade' or type == 'update' or type == "change":
            return "CASCADE"
        else:
            return "CASCADE"
        
    # allows for a user to create forgen keys for a table
    def call_forgen(self, key, foreign_table, foreign_column, update="CASCADE", delete="SET NULL"):
        expresion = f"FOREIGN KEY ({key}) REFERENCES {foreign_table} ({foreign_column}) ON UPDATE {update} ON DELETE {delete}" 
         
        return expresion

   
    def insert(self, name, insert_rows, values):
        expresion = f"INSERT INTO {name} ({insert_rows}) VALUES ({values}) ON CONFLICT DO NOTHING"


        return expresion
 

        # allowes a user to delete a table from sqlite table
    
    # delets a table from sqlite table
    def delete(self, name):
        expresion = f"DROP TABLE IF EXISTS {name}"

        return expresion

    # allows for a user to insert a new header row to a sqlite table
    def add_column(self, name, insert_rows):
        expresion = f"ALTER TABLE {name} ADD {insert_rows} ON CONFLECT DO NOTHING"

        return expresion


    # allows for a user to remove a row to a sqlite table
    def drop_column(self, name, column_name):
        expresion = f"ALTER TABLE {name} DROP COLUMN {column_name} ON CONFLECT DO NOTHING"

        return expresion
    
    # re-name a column in a table
    def update_column(self, name, column_name, new_value, where = False):
        where = False if not(bool(where)) and len(where.strip() ) != 0 else where
        expresion = f"UPDATE {name} SET {column_name} = '{new_value}' { f'WHERE {where}' if where else ''}"

        return expresion
    
            # allows a user to re-name a table from sqlite table
    def rename_table(self, origonal_name, new_name):
        expresion = f"ALTER TABLE {origonal_name} RENAME TO IF NOT EXISTS {new_name}"

        return expresion
    
        # allows for a user select data using the header as keys. the * selecter will work.
    def select_column(self, rows, name, where = ""):
        expresion = f"SELECT {rows} FROM {name}{ ' WHERE '+where if where != '' else ''}"

        return expresion
    
    
    # will selcet values that are new from a table. it uses the same SQL as select_column with the keyword "DISTINCT"
    def select_distinct(self, rows, name):
        expresion = f"SELECT DISTINCT {rows} FROM {name} ON CONFLECT DO NOTHING"

        return expresion

    # selects using a limited pool
    def select_limit(self, rows, name, limit, where = ""):
        expresion = f"SELECT {rows} FROM {name}{ ' WHERE '+where if where != '' else ''} LIMIT {limit}"

        return expresion
    
        # allows for a user to call a temperay table form a second table, that will destroy on call
    def select_aliases(self, name, row_name, new_row_name):
        expresion = f"SELECT {row_name} AS {new_row_name} FROM {name} ON CONFLECT DO NOTHING"

        return expresion