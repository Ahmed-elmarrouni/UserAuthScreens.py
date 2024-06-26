# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 670)
        MainWindow.setStyleSheet("background-color: rgb(20, 11, 90);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(32, 230, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Username.setFont(font)
        self.Username.setStyleSheet("#Username{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(12, 2, 48);\n"
"border: 3px Solid rgb(48, 252, 255);\n"
"border-radius: 18px;\n"
"}\n"
"#Username:hover{\n"
"border: 2px solid rgb(255, 15, 51);\n"
"}\n"
" ")
        self.Username.setText("")
        self.Username.setPlaceholderText("")
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(30, 360, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Password.setFont(font)
        self.Password.setStyleSheet("#Password{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(12, 2, 48);\n"
"border: 3px solid rgb(48, 252, 255);\n"
"border-radius: 18px;\n"
"}\n"
"\n"
"#Password:hover{\n"
"border: 2px solid rgb(255, 15, 51);\n"
"}\n"
"")
        self.Password.setText("")
        self.Password.setObjectName("Password")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 320, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.Login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Login_btn.setGeometry(QtCore.QRect(30, 470, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Login_btn.setFont(font)
        self.Login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Login_btn.setStyleSheet("#Login_btn{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 252, 205);\n"
"border-radius: 18px;\n"
"border: 4px solid rgb(148, 252, 255);\n"
"}\n"
"#Login_btn:hover:pressed{\n"
"background-color: rgb(35, 38, 255);\n"
"}")
        self.Login_btn.setObjectName("Login_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 9, 221, 161))
        font = QtGui.QFont()
        font.setPointSize(75)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
"color: rgb(255, 255, 255);\n"
"border: 4px Solid rgb(48, 252, 255);\n"
"border-radius: 60px;\n"
"}\n"
"#label:hover{\n"
"color: rgb(255, 39, 1);\n"
"border: 4px dotted rgb(3, 255, 19);\n"
"}")
        self.label.setObjectName("label")
        self.New_btn = QtWidgets.QPushButton(self.centralwidget)
        self.New_btn.setGeometry(QtCore.QRect(102, 560, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.New_btn.setFont(font)
        self.New_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.New_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.New_btn.setObjectName("New_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Username :"))
        self.label_3.setText(_translate("MainWindow", "Password :"))
        self.Login_btn.setText(_translate("MainWindow", "Log In"))
        self.label.setText(_translate("MainWindow", ""))
        self.New_btn.setText(_translate("MainWindow", "Creat New account"))

    
    
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
