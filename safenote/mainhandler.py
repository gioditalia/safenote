"""
    safenote.
    Copyright (C) 2016  Giovanni D'Italia

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import webbrowser
import logging
import ui_mainwindow
import filehandler
import AES
from PyQt4 import QtCore, QtGui

logger = logging.getLogger(__name__)


class MainHandler(ui_mainwindow.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

    def __setTriggers(self):
        logger.debug("setup triggers...")
        self.actionNew.triggered.connect(self.new)
        self.actionOpen.triggered.connect(self.open)
        self.actionSave.triggered.connect(self.save)
        self.actionPrint.triggered.connect(self.fprint)
        self.actionUndo.triggered.connect(self.plainTextEdit.undo)
        self.actionRedo.triggered.connect(self.plainTextEdit.redo)
        self.actionFind.triggered.connect(self.find)
        self.actionFind_next.triggered.connect(self.find_next)
        self.actionEncrypt.triggered.connect(self.encrypt)
        self.actionDecrypt.triggered.connect(self.decrypt)
        self.actionOnline_help.triggered.connect(self.online)
        self.actionAbout.triggered.connect(self.about)

    def setupUi(self, MainWindow):
        logger.debug("setup MainHandler...")
        super(self.__class__, self).setupUi(MainWindow)
        self.__setTriggers()
        self.MainWindow = MainWindow

    def new(self):
        if self.plainTextEdit.toPlainText() != "":
            ans = QtGui.QMessageBox.question(self.MainWindow, "Message",
                                             "You will lose any unsaved "
                                             "changes, ok?",
                                             QtGui.QMessageBox.Yes |
                                             QtGui.QMessageBox.No,
                                             QtGui.QMessageBox.Yes)
            if ans == QtGui.QMessageBox.Yes:
                self.plainTextEdit.clear()
                return True
            else:
                return False
        return True

    def open(self):
        fname = QtGui.QFileDialog.getOpenFileName(self.MainWindow, "Open file",
                                                  "",
                                                  "All files "
                                                  "(*.*)")
        fname = str(fname)
        if fname is not "":
            if self.new():
                try:
                    filehandler.FileHandler(fname).open(self.plainTextEdit)

                except UnicodeError:
                    QtGui.QMessageBox.critical(self.MainWindow, "Message",
                                               "Cannot open this kind of"
                                               "files")

                except IOError:
                    QtGui.QMessageBox.critical(self.MainWindow, "Message",
                                               "Cannot open this file")

    def save(self):
        fname = QtGui.QFileDialog.getSaveFileName(self.MainWindow,
                                                  "Save file",
                                                  "",
                                                  "All files "
                                                  "(*.*)")
        fname = str(fname)
        if fname is not "":
            try:
                filehandler.FileHandler(fname).save(self.plainTextEdit)

            except UnicodeError:
                QtGui.QMessageBox.critical(self.MainWindow, "Message",
                                           "Cannot save this file, use only"
                                           " ascii characters")

            except IOError:
                QtGui.QMessageBox.critical(self.MainWindow, "Message",
                                           "Cannot write this file")

    def fprint(self):
        # Open printing dialog
        dialog = QtGui.QPrintDialog()

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.plainTextEdit.document().print_(dialog.printer())
            logger.debug("Printing...")

    def find(self):
        self.text, ok = QtGui.QInputDialog.getText(self.MainWindow, "Search",
                                                   "Search:")
        if ok:
            self.findFlag = False
            self.find_next()

    def find_next(self):
        if not self.plainTextEdit.find(self.text):
            logger.debug("Not found any other occurence for '%s'"
                         % (self.text))
            if self.findFlag is False:
                logger.debug("Set cursor position on start")
                cursor = self.plainTextEdit.textCursor()
                cursor.setPosition(0)
                self.plainTextEdit.setTextCursor(cursor)
                self.findFlag = True
                self.find_next()
            else:
                QtGui.QMessageBox.information(self.MainWindow, "Message",
                                              "No result found for '%s'"
                                              % (self.text))
        else:
            logger.debug("Found '%s' in position %d" %
                         (self.text,
                          (self.plainTextEdit.textCursor().position() -
                           len(self.text))
                          )
                         )
            self.findFlag = False

    def encrypt(self):
        password, ok = QtGui.QInputDialog.getText(self.MainWindow, "Encrypt",
                                                  "Password:",
                                                  QtGui.QLineEdit.
                                                  Password)
        if ok:
            try:
                AES_machine = AES.AESCipher(password)
                # encrypt
                ciphertext = AES_machine.encrypt(self.plainTextEdit.
                                                 toPlainText())
                self.plainTextEdit.setPlainText(ciphertext.encode("utf-8"))

            except UnicodeError as error:
                logger.error(error)
                QtGui.QMessageBox.critical(self.MainWindow, "Message",
                                           "I can encrypt only ascii"
                                           " characters")
            except Exception as error:
                logger.error(error)
                QtGui.QMessageBox.critical(self.MainWindow, "Message",
                                           str(error))

    def decrypt(self):
        password, ok = QtGui.QInputDialog.getText(self.MainWindow, "Decrypt",
                                                  "Password:",
                                                  QtGui.QLineEdit.
                                                  Password)
        if ok:
            try:
                AES_machine = AES.AESCipher(password)
                # decrypt
                ciphertext = AES_machine.decrypt(self.plainTextEdit.
                                                 toPlainText())
                self.plainTextEdit.setPlainText(ciphertext.encode("utf-8"))

            except UnicodeError as error:
                logger.error(error)
                QtGui.QMessageBox.critical(self.MainWindow, "Message",
                                           "Wrong password!")
                self.decrypt()

            except Exception as error:
                logger.error(error)
                QtGui.QMessageBox.critical(self.MainWindow, "Message",
                                           str(error))

    def online(self):
        webbrowser.open("http://gioditalia.github.io/safenote")

    def about(self):
        logger.warning("not implemented")