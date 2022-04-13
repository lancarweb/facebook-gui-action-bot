# from sqlite3.dbapi2 import Cursor
# import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
import os

class Editprofile(QMainWindow):
    def __init__(self):
        super(Editprofile, self).__init__()
        loadUi(os.path.join(os.path.expanduser(os.getcwd()), 'ui', 'edit.ui'), self)
        self.setWindowTitle("Facebook - Edit")
       
        # load comboBoxId 
        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor = db.cursor()
        query = "SELECT id from Accounts"
        results = cursor.execute(query)

        result_items  =[str(result[0]) for result in results]
        self.comboBoxId.addItems(result_items)
        # print(type(result_items[0]))

        # load
        self.comboBoxId.activated.connect(self.load)

        # buttonsave
        self.pushButtonSave.clicked.connect(self.save)

    def insertItem(self):
        
        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor = db.cursor()
        query = "SELECT COUNT(id) from Accounts"
        cursor.execute(query)
        result_count = cursor.fetchone()[0]

        db_item = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor_item = db_item.cursor()
        query_item = "SELECT id from Accounts"
        result_items = cursor_item.execute(query_item)
        result_id = [result[0] for result in result_items]
        result_id_ = (result_id[result_count - 1])
        
        self.comboBoxId.insertItem(int(result_count) + 1, "{}".format(result_id_)) 
        
        #result_items  =[str(result[0]) for result in results]
        #self.comboBoxId.addItems(result_items)

    def load(self):
        print(self.comboBoxId.currentText())

        # loaddata
        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db')) 
        cursor = db.cursor()
        query = "SELECT * from Accounts where id={} ".format(self.comboBoxId.currentText())
        results = cursor.execute(query)

        for result in results:
            self.lineEditUsername.setText(result[1])
            self.lineEditPassword.setText(result[2])
            self.lineEditMessage.setText(result[3])
            self.spinBoxTimeout.setValue(result[4])
            self.spinBoxStep.setValue(result[5])

    def save(self):
        
        # update database
        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor = db.cursor()
        query = " UPDATE Accounts SET username='{}', password='{}', messages='{}', timeout='{}', timeoutstep='{}' where id='{}' ".format(self.lineEditUsername.text(), self.lineEditPassword.text(), self.lineEditMessage.text(), self.spinBoxTimeout.text(), self.spinBoxStep.text(), self.comboBoxId.currentText())
        cursor.execute(query)
        db.commit()

        # clear|field
        self.lineEditUsername.clear()
        self.lineEditPassword.clear()
        self.lineEditMessage.clear()
        self.spinBoxTimeout.setValue(0)
        self.spinBoxStep.setValue(0)
