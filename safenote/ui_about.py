# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../forms/about.ui'
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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(419, 328)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/icons/safenote.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(About)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(98, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtGui.QLabel(About)
        self.label.setMaximumSize(QtCore.QSize(128, 128))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("images/icons/safenote.ico")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(98, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(About)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(About)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(About)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_6 = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "About", None))
        self.label_2.setText(_translate("About", "safenote", None))
        self.label_3.setText(_translate("About", "0.1.0", None))
        self.label_4.setText(_translate("About", "safenote is a small text editor with AES128 encryption", None))
        self.label_5.setText(_translate("About", "Copyright © 2016 - Giovanni D\'Italia", None))
        self.label_6.setText(_translate("About", "This program comes with absolutely no warranty.", None))
        self.label_7.setText(_translate("About", "See the <a href=\'https://www.gnu.org/licenses/gpl-3.0.en.html\'> GNU General Public License, version 3</a> for details.", None))
