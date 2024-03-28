from dbfunc import *
import mysql.connector
from mysql.connector import Error


class Model:
    def __init__(self):
        self.conn = getConnection()
        self.tbName = ""
        if self.conn != None:
            if self.conn.is_connected():
                self.dbcursor = self.conn.cursor()
            else:
                print("DBfunc error")

    def getAll(self, limit=10):
        self.dbcursor.execute("select * from " + self.tbName + " limit " + str(limit))
        myresult = self.dbcursor.fetchall()
        if self.dbcursor.rowcount == 0:
            myresult = ()
        return myresult


class Student(Model):
    def __init__(self):
        super().__init__()
        self.tbName = "student"

    def getById(self, id):
        self.dbcursor.execute('select * from ' + self.tbName + ' where Sid = {}'.format(id))
        myresult = self.dbcursor.fetchone()
        if self.dbcursor.rowcount == 0:
            myresult = ()
        return myresult

    def addNew(self, student):
        self.dbcursor.execute('insert into ' + self.tbName + ' values (%s, %s, %s, %s)',
                              (student['sid'], student['sname'], student['email'],student['tut_id']))
        myresult = self.conn.commit()
        if self.dbcursor.rowcount == 0:
            return False
        return True
class Tutor(Model):
    def __init__(self):
        super().__init__()
        self.tbName = "tutor"