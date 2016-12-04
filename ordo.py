#!/usr/bin/env python3

"""
Python script to encrypt text file and delete the old plain text file.
It also decrypts the encrypted file.

Usage: python3 ordo.py [OPTION] [FILE]

    -e      Encrypts the plaintext file into a new file and delete the old
            plaintext file.
    -d      Decrypts the ciphertext file into a new file with file extension
            '*.ordo'.
"""

from simplecrypt import encrypt, decrypt
from getpass import getpass
import sys
import os


def ordo_encrypt(filename):
    """Takes a file, encrypts its contents, and replaces the
    old file with the encrypted file.
    """

    plain_file = open(filename, 'r+', encoding='UTF-8')
    plaintext = plain_file.read()
    password = getpass("Enter the password to encrypt: ")
    ciphertext = encrypt(password, plaintext.encode('UTF-8'))
    plain_file.close()
    os.remove(filename)

    new_filename = filename + '.enc'
    encrypted_file = open(new_filename, 'wb')
    encrypted_file.write(ciphertext)
    encrypted_file.close()


def ordo_decrypt(filename):
    """Takes an encrypted file, decrypts its contents, and replaces
    the encrypted file with the decrypted file.
    """

    encrypted_file = open(filename, 'rb')
    ciphertext = encrypted_file.read()
    password = getpass("Enter password for decrypt: ")
    plaintext = decrypt(password, ciphertext)
    encrypted_file.close()
    os.remove(filename)

    new_filename = filename[:-4]
    decrypted_file = open(new_filename, 'w+', encoding='UTF-8')
    decrypted_file.write(plaintext.decode('UTF-8'))
    decrypted_file.close()


def main():
    if sys.argv[1] == '-e':
        ordo_encrypt(sys.argv[2])
    elif sys.argv[1] == '-d':
        ordo_decrypt(sys.argv[2])
    else:
        print("Please specify an option")

if __name__ == '__main__':
    main()
