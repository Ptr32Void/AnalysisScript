#-------------------------------------------------------------------------------
# Name:        Trojan.Netweird logged keys Decryptor
# Purpose:     Decryptor for encrypted data (keylog data) related to Trojan.Netweird 
#              Log files are encrypted and normally added in the form:
#              %APPDATA%\Logs\dd-mm-yyyyy
# MD5:         78ff589aa5e8e174ce66db4bf8c19d84
#
# Author:      Ptr32Void - @Ptr32Void
#-------------------------------------------------------------------------------

import string
import struct

def main():
    fh = open('dd-mm-yyyy', 'r')

    buff = ''
    while 1:
        b = fh.read(1)
        if len(b) == 0:
            break

        ch = ord(b)
        buff += chr( ((ch - 0x24) ^ 0xFFFFFF9D) & 0x000000FF)

    print buff

if __name__ == '__main__':
    main()

