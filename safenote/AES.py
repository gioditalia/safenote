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
from Crypto.Cipher import AES
from Crypto import Random

logger = logging.getLogger(__name__)
BS = 16


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpad(s):
    return s[:-ord(s[-1])]


class AESCipher:

    def __init__(self, key):
        """
        Keys padding
        """
        logger.debug("Padding key...")
        self.key = pad(str(key))

    def encrypt(self, raw):
        """
        Returns hex encoded encrypted value!
        """
        try:
            raw = pad(str(raw))
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            logger.debug("Encryption...")
            return (iv + cipher.encrypt(raw)).encode("hex")
        except:
            raise Exception("Cannot encrypt")

    def decrypt(self, enc):
        """
        Requires hex encoded param to decrypt
        """
        try:
            enc = str(enc).decode("hex")
            iv = enc[:16]
            enc = enc[16:]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            logger.debug("Decryption...")
            return unpad(cipher.decrypt(enc))
        except:
            raise Exception("Cannot decrypt")
