# -*- coding: utf-8 -*-
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
#  import slate
from PyQt4 import QtCore, QtGui

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

logger = logging.getLogger(__name__)


class FileHandler:

    def __init__(self, fname):
        self.fname = fname

    def setFileExtention(self, filt):
        #try:

            if filt == "PDF (*.pdf)":
                if not self.fname.endswith("pdf"):
                    self.fname += ".pdf"
            elif filt == "Text file (*.txt)":
                if not self.fname.endswith("txt"):
                    self.fname += ".txt"
            elif filt == "All files (*.*)":
                pass
            else:
                raise ValueError("Extention not available")
        #except:
        #    raise Exception

    def open(self, textEdit):
        try:
            rfile = open(self.fname, "r")
            if self.fname.endswith("pdf") or self.fname.endswith("PDF"):
                textEdit.setPlainText(self.__convert(self.fname)
                                      .encode("utf-8"))
            else:
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
            if self.fname.endswith("pdf") or self.fname.endswith("PDF"):
                logger.debug("Saving as pdf")
                printer = QtGui.QPrinter()
                printer.setOutputFileName(self.fname)
                printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
                printer.setFullPage(False)
                textEdit.print_(printer)
            else:
                logger.debug("Saving as text file")
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

    def __convert(self, fname, pages=None):
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = open(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close
        text = text.split("\n")
        result = ""
        string_old = " "
        for string in text:
            string = string.strip("\n")  # delete \n
            logger.debug("Checking: %s" % (string))
            logger.debug("This \"%s\" not in  \"%s\" ?" % (string_old, string))
            if string_old not in string:
                logger.debug("True ✓")
            logger.debug("%d > 5 ?" % len(string))
            if len(string) > 5:
                logger.debug("True ✓")
            if len(string) > 5 and string_old not in string:
                logger.debug("Insert string")
                string_old = string
                result += string
        return result.strip("\n")
