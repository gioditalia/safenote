# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../forms/mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/icons/safenote.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Sans"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(7, 7, 7, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionOnline_help = QtGui.QAction(MainWindow)
        self.actionOnline_help.setObjectName(_fromUtf8("actionOnline_help"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionFind_next = QtGui.QAction(MainWindow)
        self.actionFind_next.setObjectName(_fromUtf8("actionFind_next"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionOpen_and_Decrypt = QtGui.QAction(MainWindow)
        self.actionOpen_and_Decrypt.setObjectName(_fromUtf8("actionOpen_and_Decrypt"))
        self.actionEncrypt_and_Save = QtGui.QAction(MainWindow)
        self.actionEncrypt_and_Save.setObjectName(_fromUtf8("actionEncrypt_and_Save"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen_and_Decrypt)
        self.menuFile.addAction(self.actionEncrypt_and_Save)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuAbout.addAction(self.actionOnline_help)
        self.menuAbout.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFind_next)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "safenote", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Help", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionPrint.setText(_translate("MainWindow", "Print", None))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.actionOnline_help.setText(_translate("MainWindow", "Online help", None))
        self.actionOnline_help.setShortcut(_translate("MainWindow", "F1", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionFind.setText(_translate("MainWindow", "Find", None))
        self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionFind_next.setText(_translate("MainWindow", "Find next", None))
        self.actionFind_next.setShortcut(_translate("MainWindow", "Ctrl+Shift+F", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z", None))
        self.actionOpen_and_Decrypt.setText(_translate("MainWindow", "Open and Decrypt", None))
        self.actionOpen_and_Decrypt.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionEncrypt_and_Save.setText(_translate("MainWindow", "Encrypt and Save", None))
        self.actionEncrypt_and_Save.setShortcut(_translate("MainWindow", "Ctrl+S", None))
