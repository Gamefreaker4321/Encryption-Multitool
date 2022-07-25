def caesarEncrypt(text):
    offset = int(input('Please enter an offset between 1 and 25\n'))
    while (offset > 25 or offset < 1):
        offset = int(input('Invalid offset.\nPlease enter an offset between 1 and 25\n'))
    result = ''
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Ignore non alpha characters 
        if (not char.isalpha()):
            result += char
        # Encrypt uppercase characters in plain text
        elif (char.isupper()):
            result += chr((ord(char) + offset - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + offset - 97) % 26 + 97)
    return result

def caesarDecrypt(text):
    offset = int(input('Please enter an offset between 1 and 25\n'))
    while (offset > 25 or offset < 1):
        offset = int(input('Invalid offset.\nPlease enter an offset between 1 and 25\n'))
    result = ''
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Ignore non alpha characters 
        if (not char.isalpha()):
            result += char
        # decrypt uppercase characters in plain text
        elif (char.isupper()):
            result += chr((ord(char) - offset - 65) % 26 + 65)
        # decrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - offset - 97) % 26 + 97)
    return result
