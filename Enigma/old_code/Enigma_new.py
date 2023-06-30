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


def main():
    global char, cipherText, i
    getPlainText()
    cipherText = ''

    for i in range(len(plainText)):
        char = plainText[i]
        encipherAndDecipher(rotor0, 1)
        encipherAndDecipher(rotor1, 1)
        encipherAndDecipher(rotor2, 1)

        char = plugboard[char]

        encipherAndDecipher(rotor0, -1)
        encipherAndDecipher(rotor1, -1)
        encipherAndDecipher(rotor2, -1)
        cipherText += char

        rotorsLinksAndMove(rotor0, rotor1, rotor2)
    print(cipherText)


def getPlainText():
    global plainText
    plainTextOrig = input("Type in your text:\n")
    cop = re.compile("[^a-z^A-Z]")
    plainText = cop.sub('', plainTextOrig).upper()


def getRotorAndBackup():
    Rotor = list(range(26))
    shuffle(Rotor)
    return Rotor, copy.copy(Rotor)


def encipherAndDecipher(rotor, sign):
    global char
    alphabet = string.ascii_uppercase

    orig_index = alphabet.find(char)
    change_index = rotor[i % len(alphabet)] * sign
    new_index = (orig_index + change_index) % len(alphabet)

    char = alphabet[new_index]


def setPlugboard():
    global plugboard
    plugs = list(string.ascii_uppercase)
    shuffle(plugs)

    plugboard = dict(
        dict(zip(plugs[:13], plugs[13:])),
        **dict(zip(plugs[13:], plugs[:13])))
    print("Plugboard:\n", plugboard)


def rotorsLinksAndMove(zeroth, first, second):
    moveRotor(zeroth)
    if zeroth == rotorOrig0:
        moveRotor(first)
        if first == rotorOrig1:
            moveRotor(second)


def moveRotor(rotor):
    first_char = rotor.pop(0)
    rotor.append(first_char)


setPlugboard()

rotor0, rotorOrig0 = getRotorAndBackup()
rotor1, rotorOrig1 = getRotorAndBackup()
rotor2, rotorOrig2 = getRotorAndBackup()
print('Original rotors:\n', rotorOrig0, rotorOrig1, rotorOrig2)

main()

# test and decrypt
rotor0 = copy.copy(rotorOrig0)
rotor1 = copy.copy(rotorOrig1)
rotor2 = copy.copy(rotorOrig2)

plainText = cipherText

main()
