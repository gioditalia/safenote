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

import logging
from PyQt4 import QtGui

logger = logging.getLogger(__name__)


class FileHandler:

    def __init__(self, fname):
        self.fname = fname
        self.encryption = False

    def open(self, textEdit):
        try:
            rfile = open(self.fname, "r")
            textEdit.setPlainText(rfile.read().encode("utf-8"))
            rfile.close()
            logger.debug("Opened %s" % (self.fname))

        except UnicodeError as error:
            logger.error("Cannot open %s - %s" % (self.fname, error))
            raise

        except IOError as error:
            logger.error("Cannot read %s - %s" % (self.fname, error))
            raise

    def save(self, textEdit):
        try:
            wfile = open(self.fname, "w")
            wfile.write(str(textEdit.toPlainText())
                        .encode("utf-8"))
            wfile.close()
            logger.debug("Saved %s" % (self.fname))

        except UnicodeError as error:
            logger.error("Cannot save %s - %s" % (self.fname, error))
            raise

        except IOError as error:
            logger.error("Cannot write %s - %s" % (self.fname, error))
            raise
