import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def substitutionEncrypt(text):
    key = ''
    while checkKey(key) is False:
        key = input('Enter 26 ALPHA key (leave blank for random key): ')
        if key == '':
            key = getRandomKey()
        if checkKey(key) is False:
            print('There is an error in the key or symbol set.')
    translated = translateMessage(text, key, 'E')
    print('Using key: %s' % (key))
    return translated

def substitutionDecrypt(text):
    key = ''
    while checkKey(key) is False:
        key = input('Enter 26 ALPHA key: ')
        if checkKey(key) is False:
            print('There is an error in the key or symbol set.')    
    translated = translateMessage(text, key, 'D')
    print('Using key: %s' % (key))
    return translated
    
# Store the key into list, sort it, convert back, compare to alphabet.
def checkKey(key):
   keyString = ''.join(sorted(list(key)))
   return keyString == LETTERS

def translateMessage(text, key, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    # If decrypt mode is detected, swap A and B
    if mode == 'D':
        charsA, charsB = charsB, charsA
    for char in text:
        if char.upper() in charsA:
            index = charsA.find(char.upper())
            if char.isupper():
                translated += charsB[index].upper()
            elif char.islower():
                translated += charsB[index].lower()
        else:
            translated += char
    return translated
   
def getRandomKey():
   randomList = list(LETTERS)
   random.shuffle(randomList)
   return ''.join(randomList)
