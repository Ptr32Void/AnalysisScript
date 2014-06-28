#-------------------------------------------------------------------------------
# Name:        RTF Object extractor
# Purpose:     Script used to extract embedded objects (eg.: MZ/DOC) from
#              an RTF file.
#
# Author:      Ptr32Void - @Ptr32Void
#-------------------------------------------------------------------------------

import os
import re
import sys
import string
import binascii

transition_table = string.maketrans('', '')

def is_rtf(fh):
    buff = fh.read(5)
    if (buff.startswith('{\\rtf')):
        return True
    else:
        return False

def save_payload(fh, start_pos, end_pos):
    fname = 'payload_%x-%x' % (start_pos, end_pos)
    fhw = open(fname, 'wb')
    fh.seek(start_pos)
    size = end_pos - start_pos
    payload = fh.read(size)
    payload = payload.translate(transition_table, ' \v\f\t\r\n')
    fhw.write(binascii.unhexlify(payload))
    fhw.close()

def identify_packages(fh):
    fh.seek(0)
    buf = fh.read()

    position = 0
    while 1:
        package_pos = buf.find('objclass Package', position)
        if (package_pos == -1):
            break

        position = buf.find('*\\objdata', package_pos)
        position += 9
        fh.seek(position)

        end_position = buf.find('}', position)
        save_payload(fh, position, end_position-1)
        position = end_position

def main():

    if (len(sys.argv) != 2):
        print '[!] python %s <doc.rtf>' % (sys.argv[0])
        sys.exit(1)

    fh = open(sys.argv[1], 'rb')

    if (is_rtf(fh) == False):
        print '[-] Not an RTF'
        sys.exit(1)

    identify_packages(fh)

if __name__ == '__main__':
    main()
