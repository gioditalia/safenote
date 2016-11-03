# safenote
###### Text editor with AES128 encryption

## About
Safenote was born when a friend of mine showed me that has a file(.doc) with all passwords on a usb stick, I am horrified.
So I explored some alternatives to improve the security of passwords. :thought_balloon:
* Microsoft Word + password: It could be a good idea, but...
  * Needs a MicrosoftWord installation on your computer.
  * MicrosoftWord create a backup and cache file when open a documents, the possible leaks
  * Too many tools for recovery a password.
* TrueCrypt or Veracrypt archive: better than first, but...
  * Many MB used when installed in portable mode.
  * Need Administrator privileges

**Note**:Veracrypt it's the best application for store different kind of data securely

:bowtie: *Than I chosen to write a simple text editor that can encrypt and decrypt text.* :bowtie:

## Why you should choose *safenote* instead other?
  1. **Lightweight** (less than 12MB for Windows, 18MB for Linux)
  2. **Secure** (the sensitive text will be stored only in ram)
  3. **Secure^2** (AES128-CBC)
  4. **Secure^3** (you can not recover the password, so be careful not to lose it)
  
## How to run from code

### Requirements
 * python2.7
 * pyqt4
 * pycrypto
 
### safenote source
Download source

```
git clone https://github.com/gioditalia/safenote.git
cd safenote
python run_safenote.py
```
## Download executeble
  [Windows](https://github.com/gioditalia/safenote/releases/download/v0.3.0/safenote-win32.zip)
  
  [Linux(amd64)](https://github.com/gioditalia/safenote/releases/download/v0.3.0/safenote-linux-amd64.zip)
