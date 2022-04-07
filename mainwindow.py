
from PyQt5 import QtCore, QtGui, QtWidgets

from passgen import Ui_genWindow
from addpass import Ui_addpassWin

import webbrowser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 413)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/keyIconEdited.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 391, 131))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.newpassButton = QtWidgets.QPushButton(self.centralwidget)
        self.newpassButton.setGeometry(QtCore.QRect(120, 140, 371, 61))
        self.newpassButton.setObjectName("newpassButton")
        self.editpassButton = QtWidgets.QPushButton(self.centralwidget)
        self.editpassButton.setGeometry(QtCore.QRect(120, 210, 371, 61))
        self.editpassButton.setObjectName("editpassButton")
        self.generatepassButton = QtWidgets.QPushButton(self.centralwidget)
        self.generatepassButton.setGeometry(QtCore.QRect(120, 280, 371, 71))
        self.generatepassButton.setObjectName("generatepassButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 26))
        self.menubar.setObjectName("menubar")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.menuTheme.addAction(self.actionDark)
        self.menuTheme.addAction(self.actionLight)
        self.menubar.addAction(self.menuTheme.menuAction())

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.actionGithub = QtWidgets.QAction(MainWindow)
        self.menuHelp.addAction(self.actionGithub)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionDark.setObjectName("actionGithub")
        MainWindow.setStyleSheet(open('styles/mainwindark.css').read())
        self.style = 'd'
        self.con(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Vault"))
        self.newpassButton.setText(_translate("MainWindow", "Add new password to vault"))
        self.editpassButton.setText(_translate("MainWindow", "Edit or remove password from vault"))
        self.generatepassButton.setText(_translate("MainWindow", "Generate strong passwords"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionGithub.setText(_translate("MainWindow", "Github"))
        

    
        
    def con(self, MainWindow):
        self.generatepassButton.clicked.connect(self.generatepass)
        self.newpassButton.clicked.connect(self.addpass)
        self.actionGithub.triggered.connect(self.ghub)
        self.actionDark.triggered.connect(self.dark)
        self.actionLight.triggered.connect(self.light)

    def generatepass(self):
        self.genWindow = QtWidgets.QWidget()
        self.ui = Ui_genWindow()
        self.ui.setupUi(self.genWindow)
        if self.style == 'l':
            self.genWindow.setStyleSheet(open('styles/mainwinlight.css').read())
        else:
            self.genWindow.setStyleSheet(open('styles/mainwindark.css').read())

        self.genWindow.show()

    def addpass(self):
        self.addpassWin = QtWidgets.QWidget()
        self.ui = Ui_addpassWin()
        self.ui.setupUi(self.addpassWin)
        if self.style == 'l':
            self.addpassWin.setStyleSheet(open('styles/mainwinlight.css').read())
        else:
            self.addpassWin.setStyleSheet(open('styles/mainwindark.css').read())
        self.addpassWin.show()

    def ghub(self):
        webbrowser.open('https://github.com/anshmehta7x/Vault')

    def light(self):
        
        MainWindow.setStyleSheet(open('styles/mainwinlight.css').read())
        self.style = 'l'

    def dark(self):
        MainWindow.setStyleSheet(open('styles/mainwindark.css').read())
        self.style = 'd'

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
