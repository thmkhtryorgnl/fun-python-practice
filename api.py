#!/bin/python3
#This code to show persian poems from Ganjoor API json in qt mainwindow uses PySide6(Qt6)
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import requests
import json
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow): #style class
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 137)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(500, 10, 341, 41))
        font = QFont()
        font.setFamilies([u"Vazirmatn Medium"])
        font.setPointSize(16)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.shaer = QLabel(self.centralwidget)
        self.shaer.setObjectName(u"shaer")
        self.shaer.setGeometry(QRect(100, 60, 55, 15))
        font1 = QFont()
        font1.setFamilies([u"Vazirmatn Light"])
        self.shaer.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 341, 41))
        self.label_2.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 811, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", f"{poem_dict['m1']}", None)) # set part 1 of poem from api
        self.shaer.setText(QCoreApplication.translate("MainWindow", f"{poem_dict['poet']}", None))# set poet from api 
        self.label_2.setText(QCoreApplication.translate("MainWindow", f"{poem_dict['m2']}", None))# set part 2 of poem from api
    # retranslateUi
if __name__ =="__main__":
    poem =requests.get("https://c.ganjoor.net/beyt-json.php") #request get to api of ganjoor.net
    poem_dict=json.loads(poem.text) #convert to dict
    app = QApplication(sys.argv) #load app
    MainWindow = QMainWindow() #open main window
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) #set ui to our class
    MainWindow.show() #show
    sys.exit(app.exec())
