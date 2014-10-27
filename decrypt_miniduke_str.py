#-------------------------------------------------------------------------------
# Name:        Miniduke strings decryptor
# Purpose:     Script used to decrypt strings in Backdoor.Miniduke!gen4 files.
#              Eg.: MD5: c8eb6040fd02d77660d19057a38ff769
#
# Author:      Ptr32Void
#
# Date:        20/10/2014
#-------------------------------------------------------------------------------
import re
import idc
import string

def decrypt_string(key, offset_string, size_encrypted_string):
	buff = ''
	enc_len = offset_string + size_encrypted_string
	while offset_string < enc_len:
		buff += chr(Byte(offset_string) ^ key)
		offset_string += 1
	return buff


ea = 0x1001D8D0
while (ea < 0x1001D910):
	offset = GetDisasm(ea)
	pos = offset.find('_') + 1
	encrypted_string_offset = int(offset[pos:], 16)
	key_encrypted_string = Byte(encrypted_string_offset)
	size_encrypted_string = Word(encrypted_string_offset + 1)
	offset_encrypted_string = encrypted_string_offset + 3
	print 'Size: %x' % size_encrypted_string
	print 'Key: %x' % key_encrypted_string
	print 'Offset String: %x' % offset_encrypted_string
	offset_comment = offset_encrypted_string
	decrypted = decrypt_string(key_encrypted_string, offset_encrypted_string, size_encrypted_string)
	MakeComm(ea, 'decrypted string: %s' % (decrypted))
	ea += 4
