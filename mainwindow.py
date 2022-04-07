# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 413)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("keyIcon.jpg"))
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

    def connect(self, MainWindow):
        self



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
