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

    # runs a line a sql code with an expected output
    def runRet(self, txt):
        try:
            res = self.conn.execute(txt)
            # maps over the array of truples. the list is then converted from a array object to an array of arrays
            return numpy.array(
                list(map((lambda tru: numpy.asarray(tru)), res.fetchall())))
        except NameError:
            return False
