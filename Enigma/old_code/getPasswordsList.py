#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:26:21 2021

@author: wst
"""
from random import shuffle

num = 5
passwords = []

for i in range(num):
    order = list(range(26))
    shuffle(order)
    passwords.append(order)

passwordsFile = "passwords.txt"
with open(passwordsFile, 'w') as f:
    f.write(str(passwords))
