#-------------------------------------------------------------------------------
# Name:        UpatreIconExtractor
#              Icon Extractor For
#              Symantec  : Downloader.Upatre
#              Microsoft : TrojanDownloader:Win32/Upatre.A
#              TrendMicro: TROJ_UPATRE.SMZ3
#
# Note:        This is just a PoC and has been developed only for testing
#
# Purpose:     The following script should be copied inside a directory
#              containing a list of samples (Upatre). It will extract the
#              icon from all the samples, saving them into the "icon" directory.
#              The icon is within the resource directory of the samples
#              and have the following characteristics:
#              - resource type RT_ICON (0x3)
#              - language 1033 (ENG - US)
#
#              I have been doing some research on Upatre samples and I found out
#              that lots of them shares the same icon (PDF, WORD, MediaPlayer).
#              The extracted icons are very similar and can be used (in conjunction
#              with other methods) to identify Upatre samples. Example:
#              After extracting the icons from 99 Upatre samples and generating
#              their MD5s, I have identified that 76.77% of the samples have the same
#              icon.
#
#              Moreover, among these icons, some of them are similar and might
#              be possible to identify them with fuzzy hashing or other technques.
#              This last idea has not been tested.
#
# Author:      Ptr32Void - @Ptr32Void - ptr32void@gmail.com
#-------------------------------------------------------------------------------
import os
import sys
import pefile
import hashlib

def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), ""):
            hash.update(block)
    return hash.hexdigest()

def create_icon_header(icon_size):
    icon_header =    [
                            0x00,
                            0x00, #WORD        idReserved;
                            0x01,
                            0x00, #WORD        idType;
                            0x01,
                            0x00, #WORD        idCount;
                            0x30, #BYTE        bWidth;
                            0x30, #BYTE        bHeight;
                            0x00, #BYTE        bColorCount;
                            0x00, #BYTE        bReserved;
                            0x01,
                            0x00, #WORD        wPlanes;
                            0x08,
                            0x00, #WORD        wBitCount;
                            0xA8,
                            0x0E,
                            0x00,
                            0x00, #DWORD       dwBytesInRes;
                            0x16,
                            0x00,
                            0x00,
                            0x00  #DWORD       dwImageOffset;
                        ]

    icon_size = "%08x" % icon_size
    high = int(icon_size[0:2], 16)
    low_high = int(icon_size[2:4], 16)
    high_low = int(icon_size[4:6], 16)
    low = int(icon_size[6:8], 16)
    icon_header[17] = high
    icon_header[16] = low_high
    icon_header[15] = high_low
    icon_header[14] = low
    str_header = ''.join(chr(c) for c in icon_header)
    return str_header

def save_icon(md5, header, data):
    filename = "icons\\%s.ico" % md5
    fh = open(filename, "wb")
    fh.write(header)
    fh.write(data)
    fh.close()

def extract_icon(pe, md5hash):
    if hasattr(pe, 'DIRECTORY_ENTRY_RESOURCE'):
        for resource_type in pe.DIRECTORY_ENTRY_RESOURCE.entries:
            # icon type must be 3 RT_ICON
            if ( (hasattr(resource_type, 'directory')) and (resource_type.id == 3) ):
                for resource_id in resource_type.directory.entries:
                    if hasattr(resource_id, 'directory'):
                        for resources in resource_id.directory.entries:
                            # LANG is 1033
                            if (resources.id == 1033):
                                data = pe.get_data(resources.data.struct.OffsetToData, resources.data.struct.Size)
                                header = create_icon_header(len(data))
                                save_icon(md5hash, header, data)
def main():
    for fn in os.listdir("."):
        if(os.path.isfile(fn) == False):
            continue
        print "Parsing %s (%s)" % (fn, md5sum(fn))
        try:
            pe = pefile.PE(fn)
            extract_icon(pe, md5sum(fn))
        except:
            print "[-] Not a PE"
            continue

if __name__ == '__main__':
    main()
