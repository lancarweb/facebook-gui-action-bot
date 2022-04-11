# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uifb.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(420, 400)
        Form.setMinimumSize(QSize(420, 400))
        Form.setMaximumSize(QSize(420, 400))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 401, 381))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.horizontalLayoutWidget_2 = QWidget(self.home)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 280, 371, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.startButtonAction = QPushButton(self.horizontalLayoutWidget_2)
        self.startButtonAction.setObjectName(u"startButtonAction")

        self.horizontalLayout_2.addWidget(self.startButtonAction)

        self.stopButtonAction = QPushButton(self.horizontalLayoutWidget_2)
        self.stopButtonAction.setObjectName(u"stopButtonAction")

        self.horizontalLayout_2.addWidget(self.stopButtonAction)

        self.label_12 = QLabel(self.home)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 71, 21))
        font1 = QFont()
        font1.setBold(True)
        self.label_12.setFont(font1)
        self.userAgentInfo = QLabel(self.home)
        self.userAgentInfo.setObjectName(u"userAgentInfo")
        self.userAgentInfo.setGeometry(QRect(80, 10, 301, 20))
        self.listWidget = QListWidget(self.home)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(15, 41, 361, 231))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tabWidget.addTab(self.home, "")
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.horizontalLayoutWidget_3 = QWidget(self.profile)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 10, 371, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEditUsername = QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEditUsername.setObjectName(u"lineEditUsername")

        self.horizontalLayout_3.addWidget(self.lineEditUsername)

        self.lineEditPassword = QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEditPassword.setObjectName(u"lineEditPassword")

        self.horizontalLayout_3.addWidget(self.lineEditPassword)

        self.addButtonAction = QPushButton(self.horizontalLayoutWidget_3)
        self.addButtonAction.setObjectName(u"addButtonAction")

        self.horizontalLayout_3.addWidget(self.addButtonAction)

        self.rolldel = QLineEdit(self.horizontalLayoutWidget_3)
        self.rolldel.setObjectName(u"rolldel")

        self.horizontalLayout_3.addWidget(self.rolldel)

        self.deleteButtonAction = QPushButton(self.horizontalLayoutWidget_3)
        self.deleteButtonAction.setObjectName(u"deleteButtonAction")

        self.horizontalLayout_3.addWidget(self.deleteButtonAction)

        self.table = QTableWidget(self.profile)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 50, 371, 261))
        self.table.setColumnCount(3)
        self.tabWidget.addTab(self.profile, "")
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        self.gridLayoutWidget = QWidget(self.setting)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 361, 226))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.checkBoxScrollTimeLine = QCheckBox(self.gridLayoutWidget)
        self.checkBoxScrollTimeLine.setObjectName(u"checkBoxScrollTimeLine")

        self.gridLayout.addWidget(self.checkBoxScrollTimeLine, 0, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 3, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 2, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout.addWidget(self.checkBox_5, 4, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout.addWidget(self.checkBox_6, 5, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.checkBoxOpenProfile = QCheckBox(self.gridLayoutWidget)
        self.checkBoxOpenProfile.setObjectName(u"checkBoxOpenProfile")

        self.gridLayout.addWidget(self.checkBoxOpenProfile, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout.addWidget(self.checkBox_7, 6, 1, 1, 1)

        self.checkBox_8 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout.addWidget(self.checkBox_8, 7, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout.addWidget(self.checkBox_9, 8, 1, 1, 1)

        self.checkBox_10 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout.addWidget(self.checkBox_10, 9, 1, 1, 1)

        self.tabWidget.addTab(self.setting, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Facebook", None))
        self.startButtonAction.setText(QCoreApplication.translate("Form", u"START", None))
        self.stopButtonAction.setText(QCoreApplication.translate("Form", u"STOP / CLOSE", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"User Agent:", None))
        self.userAgentInfo.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), QCoreApplication.translate("Form", u"Home", None))
        self.lineEditUsername.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.addButtonAction.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.rolldel.setPlaceholderText(QCoreApplication.translate("Form", u"Roll. ID", None))
        self.deleteButtonAction.setText(QCoreApplication.translate("Form", u"DELETE", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Roll. ID", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Username", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Password", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile), QCoreApplication.translate("Form", u"Profile", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Watch Story", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Accept Friend", None))
        self.checkBoxScrollTimeLine.setText(QCoreApplication.translate("Form", u"<select>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Scroll Timeline", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Open Profile", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"<select>", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Like Fanspage", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"<select>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Join Group", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Read Messenger", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"<select>", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"<select>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Watch Video", None))
        self.checkBoxOpenProfile.setText(QCoreApplication.translate("Form", u"<select>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Read Notification", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Add Friend", None))
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"<select>", None))
        self.checkBox_8.setText(QCoreApplication.translate("Form", u"<select>", None))
        self.checkBox_9.setText(QCoreApplication.translate("Form", u"<select>", None))
        self.checkBox_10.setText(QCoreApplication.translate("Form", u"<select>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), QCoreApplication.translate("Form", u"Setting", None))
    # retranslateUi

