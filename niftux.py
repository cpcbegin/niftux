import sys, re, signal, math, pyperclip
from niftuxui import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button0.clicked.connect(self.adddigit0)
        self.ui.button1.clicked.connect(self.adddigit1)
        self.ui.button2.clicked.connect(self.adddigit2)
        self.ui.button3.clicked.connect(self.adddigit3)
        self.ui.button4.clicked.connect(self.adddigit4)
        self.ui.button5.clicked.connect(self.adddigit5)
        self.ui.button6.clicked.connect(self.adddigit6)
        self.ui.button7.clicked.connect(self.adddigit7)
        self.ui.button8.clicked.connect(self.adddigit8)
        self.ui.button9.clicked.connect(self.adddigit9)
        self.ui.buttonBackdel.clicked.connect(self.deletedigit)
        self.ui.buttonDel.clicked.connect(self.deleteall)
        self.ui.buttonCopy.clicked.connect(self.copynif)
        self.ui.actionCopiar.triggered.connect(self.copynif)
        self.ui.buttonPaste.clicked.connect(self.pastenif)
        self.ui.actionPegar.triggered.connect(self.pastenif)
        self.ui.actionSalir.triggered.connect(self.exitapp)

    def addletter(self, dni):
        letra = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N",\
                  "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        nif = str(dni)+"-"+letra[dni % 23]
        self.ui.labelNIF.setText(nif.zfill(10))

    def copynif(self):
        pyperclip.copy(self.ui.labelNIF.text())

    def pastenif(self):
        dni = int(re.sub("\D", "", pyperclip.paste()))
        dni = dni % 100000000
        self.addletter(dni)

    def exitapp(self):
        sys.exit(0)

    def deleteall(self):
        self.addletter(0)

    def deletedigit(self):
        dni = int(re.sub("\D", "", self.ui.labelNIF.text()))
        print(dni)
        dni = math.floor(dni / 10)
        self.addletter(dni)

    def adddigit(self, digito):
        dni = int(re.sub("\D", "", self.ui.labelNIF.text()))
        if dni < 10000000:
            dni = dni * 10 + int(digito)
        self.addletter(dni)

    def adddigit0(self):
        print(self.adddigit(0))

    def adddigit1(self):
        print(self.adddigit(1))

    def adddigit2(self):
        print(self.adddigit(2))

    def adddigit3(self):
        print(self.adddigit(3))

    def adddigit4(self):
        print(self.adddigit(4))

    def adddigit5(self):
        print(self.adddigit(5))

    def adddigit6(self):
        print(self.adddigit(6))

    def adddigit7(self):
        print(self.adddigit(7))

    def adddigit8(self):
        print(self.adddigit(8))

    def adddigit9(self):
        print(self.adddigit(9))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
