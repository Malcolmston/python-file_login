import sqlite3
import numpy
import re


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
        cursor = conn.cursor()
        self.name = name
        self.cursor = cursor
        self.conn = conn

    def execute(self, run, key):
        self.conn.execute(run, key)
        self.conn.commit()

    
    