#-------------------------------------------------------------------------------
# Name:        ZbotStringsDecryptor
# Purpose:     I have been working with different Zbot samples and different unpacked files
#              uses the same decryption algorithm to decrypt the strings.
#              The following IDA Script is used to decrypt those strings
#              The script expects:
#              - enc_str_start_addr: this is the address of the encrypted string table
#              that can be found looking the string TAB in IDA
#              - enc_str_end_addr: this is the end address of the encrypted string table
#
#              The decrypted strings are added as a comment in the string table
#
# Author:      Ptr32Void - @Ptr32Void
#-------------------------------------------------------------------------------
import idc
import string

enc_str_start_addr = 0x00404D10
enc_str_end_addr = 0x004056C8

def decrypt(encrypted_str_address, key, size):
    buff = ""
    size = size + encrypted_str_address
    idx = 0
    while encrypted_str_address < size:
        enc_byte = Byte(encrypted_str_address)
        b = enc_byte ^ key
        b = b ^ idx
        encrypted_str_address += 1
        idx += 1
        buff += chr(b)
    return buff


while (enc_str_start_addr < enc_str_end_addr):
    address_of_key_len = Dword(enc_str_start_addr)
    size = (address_of_key_len & 0x00FF0000) >> 0x10
    enc_str_start_addr += 4
    address_of_comment = enc_str_start_addr
    address_of_string = Dword(enc_str_start_addr)
    enc_str_start_addr += 4
    key = address_of_key_len & 0x000000FF
    print "[DBG] String Address: 0x%x - Size: 0x%x" % (address_of_string, size)
    dec_string = decrypt(address_of_string, key, size)
    MakeComm(address_of_comment, dec_string)
    print "[DBG] String: %s" % (dec_string)

