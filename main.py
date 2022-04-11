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

# DRIVER CHROME
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

load_dotenv()

# os path.join

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

        self.show()

    def addNewAccount(self):

        # addData
        conn = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        conn.execute(
            "INSERT INTO ACCOUNTS (username, password) VALUES ('{}', '{}')".format(self.lineEditUsername.text(), self.lineEditPassword.text()))
        conn.commit()
        # clear.fields
        self.lineEditUsername.clear()
        self.lineEditPassword.clear()

        conn.close()
        self.viewTable()

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
        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor = db.cursor()
        query = "DELETE from ACCOUNTS where ID = {};".format(
            self.rolldel.text())
        try:
            cursor.execute(query)
            db.commit()
        except:
            pass

        self.viewTable()
        self.rolldel.clear()

    def startAction(self):
        cond_scroll_time_lines = self.checkBoxScrollTimeLine.isChecked()
        cond_open_profile = self.checkBoxOpenProfile.isChecked()

        self.thread_bot = MyThread(cond_scroll_time_lines, cond_open_profile)
        self.thread_bot.notifyProgress.connect(self.displayListView)
        self.thread_bot.notifyProgressUserAgent.connect(self.displayUserAgent)

        self.startButtonAction.setEnabled(False)
        self.stopButtonAction.setEnabled(True)
        self.checkBoxScrollTimeLine.setEnabled(False)

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


class MyThread(QThread):
    notifyProgress = pyqtSignal(str)
    notifyProgressUserAgent = pyqtSignal(str)

    def __init__(self, condscrolltimelines, condopenprofile, parent=None):
        QThread.__init__(self, parent)

        self.condscrolltimelines = condscrolltimelines
        self.condopenprofile = condopenprofile

    def run(self):
        # database loads
        db = sqlite3.connect(os.path.join(os.path.expanduser(os.getcwd()), 'db', 'database.db'))
        cursor = db.cursor()
        query = "SELECT username, password from ACCOUNTS"
        results = cursor.execute(query)

        for result in results:
            app_thread = Thread(target=self.start_bot, kwargs={
                                "username": result[0], "password": result[1]})
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

        # ScrollTimeLines
        scroll = 0
        while self.condscrolltimelines:
            sleep(1)
            if scroll == 10:
                break
            try:
                scrolltimelines(driver, By, Keys)
                self.notifyProgress.emit(
                    str(kwargs["username"]+"-> scrolling the page.."))
            except:
                pass

            scroll += 1

        # OpenProfileActions
        if self.condopenprofile:
            message = "Hello"

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

            # list-all-friends | bermasalah
            friends_list = driver.find_elements_by_xpath('//a[@class="oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb btwxx1t3 abiwlrkh p8dawk7l lzcic4wl ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi a8c37x1j"]') 

            for act in friends_list:
                print("list LIST> {}".format(act.text))
                self.notifyProgress.emit("{} mengunjungi> {}".format(kwargs["username"], act.text.split("\n")[0]))
                act.click()
                
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
                action_prof.action_profile(
                    kwargs["username"], self.notifyProgress, driver, By, Keys, message, timeout=1, comment=False, emoji=False, like=True)


app = QApplication(sys.argv)
window = Facebook()
app.exec_()
