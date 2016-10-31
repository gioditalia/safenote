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

import sys
import logging
import argparse
import mainhandler
from PyQt4 import QtGui


class SafeNote:

    def __init__(self):
        parser = argparse.ArgumentParser(description="Text editor with AES128"
                                         "encryption")
        parser.add_argument("-d", "--debug", help="enable log",
                            action="store_true")
        args = parser.parse_args()

        if args.debug:
            logging.basicConfig(level=logging.DEBUG)

        logger = logging.getLogger(__name__)

        try:
            app = QtGui.QApplication(sys.argv)
            logger.debug("start application...")

            MainWindow = QtGui.QMainWindow()
            About = QtGui.QWidget()

            ui = mainhandler.MainHandler()
            ui.setupUi([MainWindow, About])

            MainWindow.show()
            sys.exit(app.exec_())

        except Exception as error:
            logger.critical(error)
