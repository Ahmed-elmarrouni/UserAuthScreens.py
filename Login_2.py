import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_MainWindow


class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self.Login_btn.clicked.connect(self.Login_click)

    def Login_click(self):
        User_dejafound = False

        file_data = open("UserandPassword.txt", "r")
        file_data = file_data.readlines()

        for i in range(len(file_data)):
            if file_data[i] == (self.Username.text()+"," + self.Password.text()+"\n"):
                User_dejafound = True

        if User_dejafound == True:
            print("User Found")
        else:
            print("User Not Found")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = LoginWindow()
    MainWindow.show()
    sys.exit(app.exec_())
