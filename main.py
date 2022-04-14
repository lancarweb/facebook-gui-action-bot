from dotenv import load_dotenv
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
from threading import Thread
from time import sleep

# facebookbot main. modul
from facebookmod.scrolltimeline import scrolltimelines
from facebookmod.openprofile import Actionprofile
import os

# Edit
from edit import Editprofile

# DRIVER CHROME
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

load_dotenv()

# baseurl
baseurl = os.environ["BASE"]

class Facebook(QMainWindow):
    def __init__(self):
        super(Facebook, self).__init__()
        loadUi(os.path.join(os.path.expanduser(os.getcwd()), 'ui', 'uifb.ui'), self)
        self.setWindowTitle("Facebook")

        # Table Control
        self.table.verticalHeader().setVisible(False)

        self.viewTable()

        # profile start btn
        self.startButtonAction.clicked.connect(self.startAction)  # startAction
        # profile stop btn /close all
        self.stopButtonAction.clicked.connect(self.stopAction)
        self.stopButtonAction.setEnabled(False)
        # addAccountButtonActions
        self.addButtonAction.clicked.connect(self.addNewAccount)
        # delete.Roll.ID
        self.deleteButtonAction.clicked.connect(self.deleteRoll)
        
        # pushbuttonedit
        self.pushButtonEdit.clicked.connect(self.pushedit)

        # pushButtonReload
        self.pushButtonReload.clicked.connect(self.viewTable)

        # comboRollDel
        self.comborolldel()
        #db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        #cursor = db.cursor()
        #query = "SELECT id from Accounts"
        #results = cursor.execute(query)
        #iddel_items = [str(result[0]) for result in results]
        #self.comboBoxDel.addItems(iddel_items)

        # edit window
        self.editwindow = Editprofile()
        
        self.show()

    def percobaan(self):
        print('Hello Percobaan saja.')

    def comborolldel(self):
        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor = db.cursor()
        query = "SELECT id from Accounts"
        results = cursor.execute(query)
        iddel_items = [str(result[0]) for result in results]
        self.comboBoxDel.addItems(iddel_items)

        #for row_data, result_data  in enumerate(results):
        #    print(row_data, result_data)
        #    for row, data in enumerate(result_data):
        #        print(row, data)
        #        self.comboBoxDel.addItem(str(data))

    def comborolldelinsert(self):
        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor = db.cursor()
        query = "SELECT COUNT(id) from Accounts"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        # db.close()
        # print(result)

        db_item = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor_item = db_item.cursor()
        query_item = "SELECT id from Accounts"
        result_items = cursor_item.execute(query_item)
        result_id = [result[0] for result in result_items]
        result_id_ = (result_id[result - 1])

        self.comboBoxDel.insertItem(int(result)+1, "{}".format(result_id_))
    
    def pushedit(self):
        # self.editwindow.insertItem()
        self.editwindow.show()

    def addNewAccount(self):
        # addData
        conn = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        conn.execute(
            "INSERT INTO ACCOUNTS (username, password, messages, timeout, timeoutstep) VALUES ('{}', '{}', '{}', {}, {})".format(self.lineEditUsername.text(), self.lineEditPassword.text(), self.lineEditMessage.text(), self.spinBoxTimeout.text(), self.spinBoxStep.text()))
        conn.commit()
        # clear.fields
        self.lineEditUsername.clear()
        self.lineEditPassword.clear()
        self.lineEditMessage.clear()
        self.spinBoxTimeout.setValue(0)
        self.spinBoxStep.setValue(0)

        conn.close()
        self.viewTable()
        self.comborolldelinsert()
        self.editwindow.insertItem()

    def viewTable(self):
        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor = db.cursor()
        query = " SELECT * from ACCOUNTS "
        result = cursor.execute(query)

        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number,
                                   QTableWidgetItem(str(data)))

    def deleteRoll(self):
        #select count
        #db_count = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        #cursor_count = db_count.cursor()
        #query_count = "SELECT * from Accounts where id='{}'".format(self.comboBoxDel.currentText())
        #result_count = cursor_count.execute(query_count)
        #for i in result_count:
        #    print(i)

        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor = db.cursor()
        query = "DELETE from ACCOUNTS where ID = {};".format(
            self.comboBoxDel.currentText())
        try:
            cursor.execute(query)
            db.commit()
        except:
            pass

        self.viewTable()
        # print(self.comboBoxDel.currentIndex())
        self.comboBoxDel.removeItem(self.comboBoxDel.currentIndex())
        self.editwindow.removecombodel()

    def startAction(self):
        cond_scroll_time_lines = self.checkBoxScrollTimeLine.isChecked()
        # open|profile
        cond_open_profile = self.checkBoxOpenProfile.isChecked()
        set_enable_op_comment = self.checkBoxOpComment.isChecked()
        set_enable_op_like = self.checkBoxOpLike.isChecked()
        set_enable_op_emoji = self.checkBoxOpEmoji.isChecked()
        set_spinboxscst = self.spinBoxScSt.text()
        set_spinboxscop = self.spinBoxScOp.text()
        # print(set_spinboxscst, set_spinboxscop)

        self.thread_bot = MyThread(cond_scroll_time_lines, cond_open_profile, set_enable_op_comment, set_enable_op_like, set_enable_op_emoji, set_spinboxscst, set_spinboxscop)
        self.thread_bot.notifyProgress.connect(self.displayListView)
        self.thread_bot.notifyProgressUserAgent.connect(self.displayUserAgent)

        self.startButtonAction.setEnabled(False)
        self.stopButtonAction.setEnabled(True)
        self.checkBoxScrollTimeLine.setEnabled(False)
        self.checkBoxOpenProfile.setEnabled(False)
        self.checkBoxOpComment.setEnabled(False)
        self.checkBoxOpLike.setEnabled(False)
        self.checkBoxOpEmoji.setEnabled(False)
        self.spinBoxScSt.setEnabled(False)
        self.spinBoxScOp.setEnabled(False)

        self.bot_running()

        self.listwdg = 0

    def displayListView(self, data):
        self.listWidget.insertItem(self.listwdg, data)
        self.listwdg += 1

    def displayUserAgent(self, data):
        self.userAgentInfo.setText(data)

    def stopAction(self):
        # print(self.thread_bot.start_bot())
        # self.startButtonAction.setEnabled(False)
        # self.playButtonAction.setEnabled(False)
        # self.pauseButtonAction.setEnabled(False)
        # self.stopButtonAction.setEnabled(False)
        sys.exit()

    def bot_running(self):
        self.thread_bot.start()

# Thread
class MyThread(QThread):
    notifyProgress = pyqtSignal(str)
    notifyProgressUserAgent = pyqtSignal(str)

    def __init__(self, condscrolltimelines, condopenprofile, setenableopcomment, setenableoplike, setenableopemoji, setspinboxscst, setspinboxscop,  parent=None):
        QThread.__init__(self, parent)

        self.condscrolltimelines = condscrolltimelines
        # open|profile
        self.condopenprofile = condopenprofile
        self.setenableopcomment = setenableopcomment
        self.setenableoplike = setenableoplike
        self.setenableopemoji = setenableopemoji
        self.setspinboxscst = setspinboxscst
        self.setspinboxscop = setspinboxscop

    def run(self):
        # database loads
        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor = db.cursor()
        query = "SELECT username, password, messages, timeout, timeoutstep from ACCOUNTS"
        results = cursor.execute(query)

        for result in results:
            app_thread = Thread(target=self.start_bot, kwargs={
                "username": result[0], "password": result[1], "messages": result[2], "timeout": result[3], "timeoutstep": result[4]})
            app_thread.start()

    def start_bot(self, **kwargs):
        # CHROME.DRIVER.OPTIONS
        options = Options()
        options.add_argument("--disable-notifications")
        # options.add_argument("--headless")
        options.add_argument("--window-size=200,400")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36")

        # driver
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=options)

        # get-urlbase
        driver.get(baseurl)

        # user-agent
        user_agent = driver.execute_script(
            "return navigator.userAgent;")
        self.notifyProgressUserAgent.emit(user_agent)

        # Login
        while True:
            sleep(1)
            try:
                driver.find_element(
                    By.XPATH, '//input[@id="email"]').send_keys(kwargs["username"])

                driver.find_element(
                    By.XPATH, '//input[@id="pass"]').send_keys(kwargs["password"])

                driver.find_element(
                    By.XPATH, '//button[@name="login"]').click()
                break
            except:
                pass

        # while forever
        while True:
            # ScrollTimeLines
            if self.condscrolltimelines:
                
                # loading
                while True:
                    sleep(1)
                    try:
                        driver.find_element(By.XPATH, '//*[@preserveAspectRatio="xMidYMid slice"]')
                        break
                    except:
                        pass

                # go timeline
                driver.get("https://facebook.com")

                for scl in range(int(self.setspinboxscst)):
                    sleep(1)
                    try:
                        scrolltimelines(driver, By, Keys)
                        self.notifyProgress.emit(
                            str(kwargs["username"]+"-> scrolling the page.."))
                    except:
                        pass

                # timeout | step
                sleep(kwargs["timeoutstep"])

            # OpenProfileActions
            if self.condopenprofile:
                
                message = kwargs["messages"]

                # loading-after-login
                while True:
                    sleep(1)
                    try:
                        driver.find_element(By.XPATH, '//*[@class="ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 hpfvmrgz qt6c0cv9 jb3vyjys l9j0dhe7 du4w35lb bp9cbjyn btwxx1t3 dflh9lhu scb9dxdr nnctdnn4"]')
                        break

                    except:
                        pass

                # get-url-list-friends
                driver.get("https://www.facebook.com/friends/list")
                
                # loading-after-get-url-list
                while True:
                    sleep(1)
                    try:
                        driver.find_element(By.XPATH, '//*[@data-visualcompletion="ignore-dynamic"]')
                        
                        break
                    except:
                        pass

                # list-all-friends
                friends_list = driver.find_elements(By.XPATH, '//*[@data-visualcompletion="ignore-dynamic"]')

                for act in friends_list:
                    try:
                        act_log = act.find_element(By.TAG_NAME, 'a').get_attribute('href')
                        # print(act_log)
                        act.click()
                        self.notifyProgress.emit("{} mengunjungi> {}".format(kwargs["username"], act.text.split('\n')[0]))
                    except:
                        continue 
                    
                    # loading
                    while True:
                        sleep(1)
                        try:
                            driver.find_element(By.XPATH, '//*[@class="rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw i1fnvgqd gs1a9yip owycx6da btwxx1t3 hv4rvrfc dati1w0a jb3vyjys b5q2rw42 lq239pai mysgfdmx hddg9phg"]').click()
                            break
                        except:
                            pass


                    # actionall

                    action_prof = Actionprofile()
                    action_prof.action_profile(kwargs["username"], self.notifyProgress, driver, By, Keys, message, timeout=1, comment=self.setenableopcomment, emoji=self.setenableopemoji, like=self.setenableoplike, scrolltimeout=self.setspinboxscop)

            # timeout
            sleep(kwargs["timeout"])

app = QApplication(sys.argv)
window = Facebook()
app.exec_()
