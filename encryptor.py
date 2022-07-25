import argparse
import os
from AES import aesEncrypt, aesDecrypt
from DES import desEncrypt, desDecrypt
from Caesar import caesarEncrypt, caesarDecrypt
from Substitution import substitutionEncrypt, substitutionDecrypt 

ENCODING = 'utf-8'
parser = argparse.ArgumentParser(description='Encrypt a file')

# to encrypt or decrypt
parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Encrypt the file')
# selected file
parser.add_argument('file', help='File to encrypt')
# type of encryption
parser.add_argument('type', choices=['c', 's', 'd', 'a'], help='Encryption type: caesar, substitution, DES. or AES')
args = parser.parse_args()

if not os.path.isfile(args.file):
    print('File does not exist')
    exit()

if args.action == 'encrypt':
    with open(args.file, 'rb') as file:
        try:
            data = file.read()
        except Exception as e:
            print('error reading file: {}'.format(e))
            exit(1)
    if args.type == 'c':
        encrypted = caesarEncrypt(data.decode(ENCODING))
    elif args.type == 's':
        encrypted = substitutionEncrypt(data.decode(ENCODING))
    elif args.type == 'd':
        encrypted = desEncrypt(data)    
    elif args.type == 'a':
        encrypted = aesEncrypt(data)    
    with open(args.file, 'wb') as file:
        if type(encrypted) is str:
            encrypted = encrypted.encode(ENCODING)
        file.write(encrypted)
    os.rename(args.file, args.file + '.enc')
    print('encrypted')

if args.action == 'decrypt':
    with open(args.file, 'rb') as file:
        try:
            data = file.read()
        except Exception as e:
            print('error reading file: {}'.format(e))
            exit(1)
    if args.type == 'c':
        decrypted = caesarDecrypt(data.decode(ENCODING))
    elif args.type == 's':
        decrypted = substitutionDecrypt(data.decode(ENCODING))
    elif args.type == 'd':
        decrypted = desDecrypt(data)
    elif args.type == 'a':
        decrypted = aesDecrypt(data)
    with open(args.file, 'wb') as file:
        if type(decrypted) is str:
            decrypted = decrypted.encode(ENCODING)
        file.write(decrypted)
    outpath = args.file.replace('.enc', '')
    os.rename(args.file, outpath)
    print('decrypted')
