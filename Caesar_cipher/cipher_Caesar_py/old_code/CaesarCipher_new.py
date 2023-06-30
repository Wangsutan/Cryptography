#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Caesar cipher
Created on Tue Mar  9 08:00:32 2021
Optimized on Sat Aug  14 08:48:45 2021
@author: abc
"""

import string
import re


def getPlainTextAndCleanIt():
    global plainText
    plainText_orig = input("Type in your text:\n")
    cop = re.compile("[^a-z^A-Z]")
    plainText = cop.sub('', plainText_orig).upper()


def encryptCharInAlphabet():
    alphabet = string.ascii_uppercase
    method = 3
    cipherText = ''

    for char in plainText:
        plain_num = alphabet.find(char)
        cipher_num = (plain_num + method) % len(alphabet)
        cipherText += alphabet[cipher_num]
    print(cipherText)


getPlainTextAndCleanIt()
encryptCharInAlphabet()
