import pyDes

ENCODING = 'utf-8'

def desEncrypt(data):
    key = input('Enter an 8 byte key\n').encode(ENCODING)
    while len(key) != 8:
        key = input('Invalid key. \nEnter an 8 byte key\n').encode(ENCODING)
    k = pyDes.des(key, pyDes.CBC, b'\0\0\0\0\0\0\0\0', pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted = k.encrypt(data)
    return encrypted

def desDecrypt(data):
    key = input('Enter the 8 byte key to decrypt the file\n').encode(ENCODING)
    while len(key) != 8:
        key = input('Invalid key. \nEnter an 8 byte key\n').encode(ENCODING)
    k = pyDes.des(key, pyDes.CBC, b'\0\0\0\0\0\0\0\0', pad=None, padmode=pyDes.PAD_PKCS5)
    decrypted = k.decrypt(data)
    return decrypted
