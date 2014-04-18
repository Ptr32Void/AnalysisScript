#-------------------------------------------------------------------------------
# Name:        Zelix Klassmaster String Decryptor
# Purpose:     Script used to decrypt strings in .class files obfuscated with
#              Zelix Klassmaster Obfuscator
#
# Author:      Ptr32Void - @Ptr32Void
#
#-------------------------------------------------------------------------------
key = [0x33, 126, 35, 10, 116]
encrypted_strings = [
                        "Y\037UkZZ\021\r~\031C\032Jx",
                        "Y\037Uk\003\023SIk\006\023",
                        "\035\035Ok\007@",
                        "z-l'L\013K\032'E",
                        "}\033TI\030R\rP;ZP\022By\007",
                        "Y\037UkZ@\033@\177\006Z\nZ$5_\022so\006^\027Py\035\\\020"
                    ]

def decrypt(enc):
    print "--------------------\n"
    print "Encrypted: %s\n" % (enc)
    i = 0
    buff = ""

    for c in enc:
        buff += chr(key[i%len(key)] ^ ord(c))
        i += 1
    print "Decrypted: %s\n" % (buff)


def main():
    for s in encrypted_strings:
        decrypt(s)

if __name__ == '__main__':
    main()
