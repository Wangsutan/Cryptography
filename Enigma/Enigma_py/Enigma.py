#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:31:03 2021
Optimized on Sat Aug  14 08:48:45 2021
Optimized on Sun Jun  4 16:26:11 2023
@author: wst
"""

import sys
import getopt
import string
from random import shuffle
import copy
import re


class Rotor:
    def __init__(self):
        # print("Set Rotor OK!")
        self.order = []
        self.cursor = 0

    def setOrder(self):
        self.order = list(range(1, len(alphabet)))
        shuffle(self.order)

    def moveCursor(self):
        self.cursor = (self.cursor + 1) % len(self.order)


def getArgvs(argv):
    """
    Important arguments are defined here.
    Machine(m) or Manual(M)
    """
    rotorsNum = 3

    passwordFrom = 'm'
    passwordsFile = "passwords.txt"

    plugboardFrom = 'm'
    plugboardFile = "plugboard.txt"

    inputFile = "plainText.txt"
    outputFile = "cipherText.txt"

    basicInfo = f"""{argv[0]}
    [-n 3]
    [--password passwords.txt]
    [--plugboard plugboard.txt]
    [-i plainText.txt]
    [-o cipherText.txt]"""

    try:
        opts, args = getopt.getopt(argv[1:], "hn:i:o:", [
                                   "password=", "plugboard="])
    except getopt.GetoptError as err:
        print(f"BASIC USAGE: {basicInfo}")
        print(f">>>> ERROR: {err}")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h"):
            print("python", basicInfo)
            sys.exit()
        elif opt in ("-n"):
            rotorsNum = int(arg)
        elif opt in ("--password"):
            passwordFrom = 'M'
            passwordsFile = arg
        elif opt in ("--plugboard"):
            plugboardFrom = 'M'
            plugboardFile = arg
        elif opt in ("-i"):
            inputFile = arg
        elif opt in ("-o"):
            outputFile = arg
    return rotorsNum, passwordFrom, passwordsFile, plugboardFrom, plugboardFile, inputFile, outputFile


def setRotors(rotorNum):
    rotorList = [Rotor() for i in range(rotorNum)]
    return rotorList


def setPasswords(through):
    """
    You do better generate a passwords file etc through machine first.
    """
    if through == 'm':
        return setPasswordsFromMachine()
    if through == 'M':
        return setPasswordsFromManual()


def setPasswordsFromMachine():
    passwords = []
    for rotor in rotorList:
        rotor.setOrder()
        passwords.append(rotor.order)

    with open(passwordsFile, 'w') as f:
        f.write(str(passwords))
    return passwords


def setPasswordsFromManual():
    with open(passwordsFile, 'r') as f:
        passwords = eval(f.read())
    if len(passwords) != len(rotorList):
        print("The numbers of passwords and rotors are not equal.")
        sys.exit(2)

    for i in range(len(rotorList)):
        rotorList[i].order = copy.copy(passwords[i])
    return passwords


def setPlugboard(through):
    if through == 'm':
        plugboard = creatPlugboardByMachineFrom(alphabet)
        with open(plugboardFile, 'w') as f:
            f.write(str(plugboard))
    if through == 'M':
        with open(plugboardFile, 'r') as f:
            plugboard = eval(f.read())
    return plugboard


def creatPlugboardByMachineFrom(alphabet):
    plugs = list(alphabet)
    shuffle(plugs)

    num = int(len(plugs) / 2)
    plugboard = dict(
        dict(zip(plugs[:num], plugs[num:])),
        **dict(zip(plugs[num:], plugs[:num])))
    return plugboard


def getPlainTextFrom(plainTextFile):
    with open(plainTextFile, 'r') as f:
        plainText = f.read()

    cop = re.compile("[^a-z^A-Z]")
    plainText = cop.sub('', plainText).upper()
    return plainText


def getCipherText(plugboard, rotorsNum, rotorList):
    cipherText = ""
    for char in plainText:
        char = encipherAndDecipher(char, rotorList, 1)
        char = plugboard[char]
        char = encipherAndDecipher(char, rotorList, -1)
        cipherText += char
        linkAndMoveRotors(rotorsNum, rotorList, 0)
    return cipherText


def encipherAndDecipher(char, rotorList, sign):
    for rotor in rotorList:
        index_orig = alphabet.find(char)
        index_change = rotor.order[rotor.cursor] * sign
        index_new = (index_orig + index_change) % len(alphabet)
        char = alphabet[index_new]
    return char


def linkAndMoveRotors(rotorsNum, rotorList, i):
    rotorList[i].moveCursor()
    if rotorList[i].cursor == 0 and i in range(rotorsNum - 1):
        linkAndMoveRotors(rotorsNum, rotorList, i + 1)


def checkSameChar(plainText, cipherText):
    haveSameChar = False
    for i in range(len(plainText)):
        if plainText[i] == cipherText[i]:
            haveSameChar = True
            print(f'{i}: {plainText[i]}')
    if haveSameChar:
        print("It is not true Enigma!")


alphabet = string.ascii_uppercase

rotorsNum, passwordFrom, passwordsFile, plugboardFrom, plugboardFile, plainTextFile, cipherTextFile = getArgvs(sys.argv)

rotorList = setRotors(rotorsNum)
passwords = setPasswords(passwordFrom)
plugboard = setPlugboard(plugboardFrom)
plainText = getPlainTextFrom(plainTextFile)
cipherText = getCipherText(plugboard, rotorsNum, rotorList)
checkSameChar(plainText, cipherText)

with open(cipherTextFile, 'w') as f:
    f.write(cipherText)
