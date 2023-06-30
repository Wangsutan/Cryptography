#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:31:03 2021

@author: abc
"""

import string
from random import shuffle
import copy
import re


def getPassword():
    normal_list = [x for x in range(26)]
    shuffle(normal_list)
    password = normal_list
    orig_list = copy.copy(password)
    return password, orig_list


def encipher(password):
    global char
    orig_index = alphabet_u.find(char)
    new_index = (
        orig_index + password[i % len(alphabet_u)]
    ) % len(alphabet_u)
    char = alphabet_u[new_index]


def rotorMove(password):
    first_char = password.pop(0)
    password.append(first_char)


alphabet_u = string.ascii_uppercase

password0, orig_list0 = getPassword()
password1, orig_list1 = getPassword()
password2, orig_list2 = getPassword()

plainText_orig = '''
If your computer or network is protected by a firewall or proxy,
make sure that Firefox is permitted to access the Web'
'''
cop = re.compile("[^a-z^A-Z]")
plainText = cop.sub('', plainText_orig).upper()
cipherText = ''

for i in range(len(plainText)):
    char = plainText[i]
    encipher(password0)
    encipher(password1)
    encipher(password2)
    cipherText += char

    rotorMove(password0)
    if password0 == orig_list0:
        rotorMove(password1)
        print("Rotor1 run.")
        if password1 == orig_list1:
            rotorMove(password2)
            print("Rotor2 run.")

print(plainText, cipherText)
for i in range(len(plainText)):
    if plainText[i] == cipherText[i]:
        print('wow')
print(orig_list0, orig_list1, orig_list2)
