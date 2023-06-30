#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 20:18:42 2023

@author: abc
"""

import string
from collections import Counter
import sys


def getTextFrom(cipherFile):
    with open(cipherFile, 'r') as f:
        text = f.read()
    text = list(filter(str.isalpha, text))
    text = [char.upper() for char in text]
    return text


alphabet = list(string.ascii_uppercase)
step = int(input("set step as int: "))
text = getTextFrom("cipher_poly.txt")
charsLists = [alphabet.index(char) for char in text]

charsCounters = []
for s in range(step):
    split_chars = [charsLists[i] for i in range(s, len(charsLists), step)]
    charsCounters.append(Counter(split_chars).most_common(1)[0][0])
print("charsCounters:", charsCounters)

letterFrequency = "ETAONRISHDLFCMUGYPWBVKJXQZ"
letterFrequencyNum = [alphabet.index(letter) for letter in letterFrequency]

while input("`Enter` to continue or `q` to quit: ") != 'q':
    correspond = list(map(int, input(f"Set {step} numbers: ").split()))
    plainChars = ""
    for i in range(len(charsLists)):
        for s in range(step):
            if i in range(s, len(charsLists), step):
                distanceIndex = charsCounters[s] - letterFrequencyNum[correspond[s]]
                plainChars += alphabet[(charsLists[i] - distanceIndex + 26) % 26]
    print(plainChars)
