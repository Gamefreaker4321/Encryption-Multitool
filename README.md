# Python 3 Encryption Multitool
This provides a command line tool for encryption and decryption of documents with an assortment of encryption methods implemented in Python 3.
The aim of this tool is to provide interesting and useful cryptographic options with educational benefit.
Currently it supports the following methods of encryption:
- Caesar cypher
- Substitution cypher
- DES encryption
- AES encryption

## Installation
To use the tool, you need only to pip install the requirements.txt file.
```bash
$ pip install -r requirements.txt
```

## Usage

```bash
encryptor.py {'encrypt' | 'decrypt'} FILENAME {'a' | 'c' | 's' | 'd'}
```
"encrypt" or "decrypt" specifies the action on the selected file.
"a", "c", "s", "d" refer to the encryption options: AES, caesar, substitution, or DES respectively.
**Encrypting a file changes the original, it does not create a copy**

After selecting an encryption type, you will be prompted for a key based on the method chosen.
- Caesar cypher uses an int value from 1-25.
- Substitution cypher uses a string of alphabetical characters to substitute the alphabet, which must contain all alphabetical characters.
ex: ```ONABJFYVMCLEKRZPIGTDWHQXUS```
It can also be left blank to generate a random key.
- DES uses an 8 byte key for encryption.
- AES uses a 32 byte key for encryption and a 16 byte initialization vector.


The decryption methods all request the same information.