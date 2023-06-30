#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:03:50 2021

@author: abc
"""


import string


alphabet_u = string.ascii_uppercase
alphabet_l = string.ascii_lowercase

keyword = 'dog'
keyword_num_list = []
for char in keyword:
    keyword_num_list.append(alphabet_l.find(char))
# print(keyword_num_list)

plainText = input("Your plaintext:\n")
cipherText = ''
# talk is cheap, show me the code

for i in range(len(plainText)):
    method = keyword_num_list[i % len(keyword)]
    char = plainText[i]
    if alphabet_l.find(char) != -1:
        orig_index = alphabet_l.find(char)
        new_index = (orig_index + method) % len(alphabet_l)
        cipherText += alphabet_l[new_index]
    elif alphabet_u.find(char) != -1:
        orig_index = alphabet_u.find(char)
        new_index = (orig_index + method) % len(alphabet_u)
        cipherText += alphabet_u[new_index]
    else:
        cipherText += char

print(cipherText)
