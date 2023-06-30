#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:00:32 2021

@author: abc
"""


# Caesar cipher


import string


def findCharIn(target):
    """Find special character in special strings."""
    global cipherText
    plain_num = target.find(char)
    cipher_num = (plain_num + method) % len(target)
    # print(plain_num, cipher_num)
    cipherText += target[cipher_num]


alphabet_u = string.ascii_uppercase
alphabet_l = string.ascii_lowercase

method = 3

plainText = input("Your plaintext:\n")

cipherText = ''

for char in plainText:
    if alphabet_l.find(char) != -1:
        findCharIn(alphabet_l)
    elif alphabet_u.find(char) != -1:
        findCharIn(alphabet_u)
    else:
        cipherText += char

print(cipherText)
