from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


ENCODING = 'utf-8'
padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()

def aesEncrypt(data):
    key = ''
    iv = ''
    while len(key) != 32:
        key = input('Enter 32 byte key\n').encode(ENCODING)
    while len(iv) != 16:
        iv = input('Enter a 16 byte Initialization Vector\n').encode(ENCODING)
    cypher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cypher.encryptor()
    paddedData = padder.update(data) + padder.finalize()
    encrypted = encryptor.update(paddedData) + encryptor.finalize()
    return encrypted

def aesDecrypt(data):
    key = ''
    iv = ''
    while len(key) != 32:
        key = input('Enter 32 byte key\n').encode(ENCODING)
    while len(iv) != 16:
        iv = input('Enter a 16 byte Initialization Vector\n').encode(ENCODING)
    cypher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cypher.decryptor()
    paddedData = decryptor.update(data) + decryptor.finalize()
    decrypted = unpadder.update(paddedData) + unpadder.finalize()
    return decrypted