# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addpass.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from passgen import Password

class Ui_addpassWin(object):
    def setupUi(self, addpassWin):
        addpassWin.setObjectName("addpassWin")
        addpassWin.setEnabled(True)
        addpassWin.resize(728, 592)
        addpassWin.setToolTipDuration(11)
        self.titleLabel = QtWidgets.QLabel(addpassWin)
        self.titleLabel.setGeometry(QtCore.QRect(100, 10, 561, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.nameLabel = QtWidgets.QLabel(addpassWin)
        self.nameLabel.setGeometry(QtCore.QRect(60, 90, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLine = QtWidgets.QLineEdit(addpassWin)
        self.nameLine.setGeometry(QtCore.QRect(230, 90, 431, 41))
        self.nameLine.setObjectName("nameLine")
        self.urlLine = QtWidgets.QLineEdit(addpassWin)
        self.urlLine.setGeometry(QtCore.QRect(230, 170, 431, 41))
        self.urlLine.setObjectName("urlLine")
        self.urlLabel = QtWidgets.QLabel(addpassWin)
        self.urlLabel.setGeometry(QtCore.QRect(50, 150, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName("urlLabel")
        self.passwordLine = QtWidgets.QLineEdit(addpassWin)
        self.passwordLine.setGeometry(QtCore.QRect(230, 330, 431, 41))
        self.passwordLine.setObjectName("passwordLine")
        self.nameLabel_2 = QtWidgets.QLabel(addpassWin)
        self.nameLabel_2.setGeometry(QtCore.QRect(50, 330, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.nameLabel_2.setFont(font)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.generateButton = QtWidgets.QPushButton(addpassWin)
        self.generateButton.setGeometry(QtCore.QRect(230, 380, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.generateButton.setFont(font)
        self.generateButton.setObjectName("generateButton")
        self.usernameLine = QtWidgets.QLineEdit(addpassWin)
        self.usernameLine.setGeometry(QtCore.QRect(230, 250, 431, 41))
        self.usernameLine.setObjectName("usernameLine")
        self.usernameLabel = QtWidgets.QLabel(addpassWin)
        self.usernameLabel.setGeometry(QtCore.QRect(50, 240, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.nameLabel_3 = QtWidgets.QLabel(addpassWin)
        self.nameLabel_3.setGeometry(QtCore.QRect(50, 440, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.nameLabel_3.setFont(font)
        self.nameLabel_3.setObjectName("nameLabel_3")
        self.comboBox = QtWidgets.QComboBox(addpassWin)
        self.comboBox.setGeometry(QtCore.QRect(380, 450, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.addButton = QtWidgets.QPushButton(addpassWin)
        self.addButton.setGeometry(QtCore.QRect(250, 500, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.requiredLabel = QtWidgets.QLabel(addpassWin)
        self.requiredLabel.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.requiredLabel.setFont(font)
        self.requiredLabel.setObjectName("requiredLabel")

        self.retranslateUi(addpassWin)
        QtCore.QMetaObject.connectSlotsByName(addpassWin)
        self.connections(addpassWin)

    def retranslateUi(self, addpassWin):
        _translate = QtCore.QCoreApplication.translate
        addpassWin.setWindowTitle(_translate("addpassWin", "Add password"))
        self.titleLabel.setText(_translate("addpassWin", "Add password to encrypt and store"))
        self.nameLabel.setText(_translate("addpassWin", "Name*"))
        self.urlLabel.setText(_translate("addpassWin", "Website/ \n"
" application"))
        self.nameLabel_2.setText(_translate("addpassWin", "Password*"))
        self.generateButton.setText(_translate("addpassWin", "Generate a strong password instead"))
        self.usernameLabel.setText(_translate("addpassWin", "Username/ \n"
" Email*"))
        self.nameLabel_3.setText(_translate("addpassWin", "Encryption Strength"))
        self.comboBox.setItemText(0, _translate("addpassWin", "Weak (faster)"))
        self.comboBox.setItemText(1, _translate("addpassWin", "Strong (slower)"))
        self.addButton.setText(_translate("addpassWin", "Add"))
        self.requiredLabel.setText(_translate("addpassWin", "*required"))

    def connections(self, addpassWin):
        self.generateButton.clicked.connect(self.passgen)
    
    def passgen(self, addpassWin):
        p = Password(10, True, True, True)
        z = p.make()
        self.passwordLine.setText(z)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addpassWin = QtWidgets.QWidget()
    ui = Ui_addpassWin()
    ui.setupUi(addpassWin)
    addpassWin.show()
    sys.exit(app.exec_())
