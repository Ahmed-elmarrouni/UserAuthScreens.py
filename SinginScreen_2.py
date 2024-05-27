import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from SinginScreen import Ui_MainWindow


class SignInWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(SignInWindow, self).__init__()
        self.setupUi(self)

    # SING IN BUTTON "ADD ITEM IN LIST.TXT"
        self.Singin_btn.clicked.connect(self.Singin_click)

    def Singin_click(self):
        with open("UserandPassword.txt", "a") as file_data:
            file_data.write(self.Username.text() + "," +
                            self.Password.text() + "\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = SignInWindow()
    main_window.show()
    sys.exit(app.exec_())
