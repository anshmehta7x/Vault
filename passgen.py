
import random

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_genWindow(object):
    def setupUi(self, genWindow):
        genWindow.setObjectName("genWindow")
        genWindow.resize(544, 450)
        self.lengthSlider = QtWidgets.QSlider(genWindow)
        self.lengthSlider.setGeometry(QtCore.QRect(250, 100, 271, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lengthSlider.setFont(font)
        self.lengthSlider.setAutoFillBackground(False)
        self.lengthSlider.setMinimum(6)
        self.lengthSlider.setMaximum(16)
        self.lengthSlider.setSliderPosition(8)
        self.lengthSlider.setTracking(True)
        self.lengthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.lengthSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.lengthSlider.setTickInterval(1)
        self.lengthSlider.setObjectName("lengthSlider")
        self.titleLabel = QtWidgets.QLabel(genWindow)
        self.titleLabel.setGeometry(QtCore.QRect(80, 30, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(26)
        self.titleLabel.setFont(font)
        self.titleLabel.setTextFormat(QtCore.Qt.PlainText)
        self.titleLabel.setScaledContents(True)
        self.titleLabel.setObjectName("titleLabel")
        self.lengthLabel = QtWidgets.QLabel(genWindow)
        self.lengthLabel.setGeometry(QtCore.QRect(20, 90, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.lengthLabel.setFont(font)
        self.lengthLabel.setObjectName("lengthLabel")
        self.CapitalLettersBox = QtWidgets.QCheckBox(genWindow)
        self.CapitalLettersBox.setGeometry(QtCore.QRect(10, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.CapitalLettersBox.setFont(font)
        self.CapitalLettersBox.setObjectName("CapitalLettersBox")
        self.numberBox = QtWidgets.QCheckBox(genWindow)
        self.numberBox.setGeometry(QtCore.QRect(10, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.numberBox.setFont(font)
        self.numberBox.setObjectName("numberBox")
        self.specialcharactersBox = QtWidgets.QCheckBox(genWindow)
        self.specialcharactersBox.setGeometry(QtCore.QRect(10, 240, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.specialcharactersBox.setFont(font)
        self.specialcharactersBox.setObjectName("specialcharactersBox")
        self.label = QtWidgets.QLabel(genWindow)
        self.label.setGeometry(QtCore.QRect(250, 140, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.generateButton = QtWidgets.QCommandLinkButton(genWindow)
        self.generateButton.setGeometry(QtCore.QRect(270, 200, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        self.generateButton.setFont(font)
        self.generateButton.setAutoFillBackground(False)
        self.generateButton.setIconSize(QtCore.QSize(100, 100))
        self.generateButton.setShortcut("")
        self.generateButton.setObjectName("generateButton")
        self.output = QtWidgets.QLabel(genWindow)
        self.output.setGeometry(QtCore.QRect(30, 310, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.output.setFont(font)
        self.output.setObjectName("output")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(genWindow)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 330, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit.setPlaceholderText("")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(genWindow)
        QtCore.QMetaObject.connectSlotsByName(genWindow)
        self.connections(genWindow)

    def retranslateUi(self, genWindow):
        _translate = QtCore.QCoreApplication.translate
        genWindow.setWindowTitle(_translate("genWindow", "Password Generator"))
        self.titleLabel.setText(_translate("genWindow", "Password Generator"))
        self.lengthLabel.setText(_translate("genWindow", "Password Length :"))
        self.CapitalLettersBox.setText(_translate("genWindow", "Capital Letters"))
        self.numberBox.setText(_translate("genWindow", "Numbers"))
        self.specialcharactersBox.setText(_translate("genWindow", "Special Characters \n"
" (@,%,$,&..)"))
        self.label.setText(_translate("genWindow", "6     7     8    9   10  11  12  13  14  15  16"))
        self.generateButton.setText(_translate("genWindow", "Generate"))
        self.output.setText(_translate("genWindow", "Password:"))
        self.plainTextEdit.setPlainText(_translate("genWindow", "\n"
""))
    def connections(self, genWindow):
        length = self.lengthSlider.value()
        self.generateButton.clicked.connect(self.gen)
    
    def gen(self, genWindow):
        length = self.lengthSlider.value()
        
        capital = self.CapitalLettersBox.isChecked()

        numbers = self.numberBox.isChecked()

        special = self.specialcharactersBox.isChecked()
        
        pword = Password(length, capital, numbers, special)
        pp = pword.make()
        self.plainTextEdit.setPlainText(pp)



class Password():

    def __init__(self, length, capital, numbers, special):
        self.l = length
        self.c = capital
        self.n = numbers
        self.s = special
        self.lists()


    def lists(self):
        self.small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.digits = list(range(0,10))
        self.spec = ['!', '#', '$', '%', '&','*', '+', '.' ,'?', '@','~']
    
    def make(self):
        self.pool = self.small

        if self.c == True:
            self.pool.extend(self.cap)
        
        if self.n == True:
            #add to pool twice to increase weightage of numbers compared to alphabets
            self.pool.extend(self.digits)
            self.pool.extend(self.digits)

        if self.s == True:

            #add to pool twice to increase weightage of special characters compared to alphabets
            self.pool.extend(self.spec)
            self.pool.extend(self.spec)

        random.shuffle(self.pool)
        finstring = ""
        for i in range(self.l):
            
            finstring += str(self.pool[i])

        return finstring

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    genWindow = QtWidgets.QWidget()
    ui = Ui_genWindow()
    ui.setupUi(genWindow)
    genWindow.show()
    sys.exit(app.exec_())
