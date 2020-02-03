# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from db import MysqlConnect


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 490)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(420, 20, 201, 361))
        self.listView.setObjectName("listView")

        self.add_item()

        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(430, 390, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.Label1 = QtWidgets.QLabel(self.centralwidget)
        self.Label1.setGeometry(QtCore.QRect(10, 390, 201, 41))
        self.Label1.setObjectName("Label1")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 31))
        self.label.setObjectName("label")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 210, 391, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 391, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 260, 391, 121))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 391, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 160, 391, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(320, 390, 81, 31))
        self.Button1.setObjectName("Button1")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSave_2)
        self.menuEdit.addAction(self.actionEdit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionNew.triggered.connect(lambda: self.clicked("New was clicked"))

        #Примечание

        self.Button1.clicked.connect(self.set_note)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setStatusTip(_translate("MainWindow", "Save a file"))
        self.label.setText(_translate("MainWindow", "Simple ToDo"))

        self.lineEdit_4.setText(_translate("MainWindow", "примечание"))
        self.lineEdit_2.setText(_translate("MainWindow", "цена"))
        self.Label1.setText(_translate("MainWindow", "Hello World"))
        self.lineEdit.setText(_translate("MainWindow", "название"))
        self.lineEdit_3.setText(_translate("MainWindow", "ссылка"))

        self.Button1.setText(_translate("MainWindow", "Press Me"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))

        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSave_2.setText(_translate("MainWindow", "Copy"))
        self.actionSave_2.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionEdit.setShortcut(_translate("MainWindow", "Ctrl+R"))

    def clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()

    def set_note(self):
        v1 = self.lineEdit_4.text()
        v2 = self.lineEdit_2.text()
        v3 = self.lineEdit.text()
        v4 = self.lineEdit_3.text()
        print("you are: " + str(v1) + str(v2) + str(v3) + str(v4))
        note = {'title': v3, 'price': v2, 'link': v4, 'descript': v1}
        mc.add_to_db(note)

    def add_item(self):
        entries = mc.item_to_list()
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        res = [sub['title'] for sub in entries]
        for i in res:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)


if __name__ == "__main__":
    import sys
    mc = MysqlConnect()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
