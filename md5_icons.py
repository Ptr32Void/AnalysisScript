#-------------------------------------------------------------------------------
# Name:        MD5 generator for extracted Upatre icons
#
# Purpose:     Identify how many icons are shared among Upatre samples.
#
# Author:      Ptr32Void - @Ptr32Void - ptr32void@gmail.com
#-------------------------------------------------------------------------------
import os
import sys
import hashlib
import string

md5list = []

def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), ""):
            hash.update(block)
    return hash.hexdigest()

def main():
    for fn in os.listdir("."):
        if (fn.find(".ico")!=-1):
            md5file = md5sum(fn)
            if (md5file in md5list):
                continue
            else:
                md5list.append(md5file)

    for md5 in md5list:
        print md5

if __name__ == '__main__':
    main()