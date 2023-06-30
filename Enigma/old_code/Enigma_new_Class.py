#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:31:03 2021
Optimized on Sat Aug  14 08:48:45 2021
@author: abc
"""

import string
from random import shuffle
import copy
import re


class Rotor:
    order, orderOrig = [], []
    rotorList = []

    def __init__(self):
        self.rotorList.append(self)

    def setAndBackupOrder(self):
        order = list(range(26))
        shuffle(order)
        self.order, self.orderOrig = order, copy.copy(order)


def setFiles():
    global passwordsFile, plugboradFile, plainTextFile, cipherTextFile
    passwordsFile = "passwords.txt"
    plugboradFile = 'plugboard.txt'
    plainTextFile = "plainText.txt"
    cipherTextFile = "cipherText.txt"


def getPasswords():
    """You do better create passwords through machine first."""
    global through, passwords
    # through = input("get passwords through: Machine(M) or manual(m)")
    through = 'M'
    if through == 'M':
        setPasswordsFromMachine()
    if through == 'm':
        setPasswordsFromManual()
    showPasswordsInConsole()


def setPasswordsFromMachine():
    global passwords
    passwords = []
    for rotor in Rotor.rotorList:
        rotor.setAndBackupOrder()
        passwords.append(rotor.order)
    writePasswords()


def setPasswordsFromManual():
    readPasswords()
    for i in range(len(Rotor.rotorList)):
        Rotor.rotorList[i].order = copy.copy(passwords[i])
        Rotor.rotorList[i].orderOrig = copy.copy(passwords[i])


def writePasswords():
    with open(passwordsFile, 'w') as f:
        f.write(str(passwords))


def readPasswords():
    global passwords
    with open(passwordsFile, 'r') as f:
        passwords = eval(f.read())


def showPasswordsInConsole():
    print('Passwords:')
    for rotor in Rotor.rotorList:
        print(rotor.orderOrig)


def getPlugboard():
    if through == 'M':
        creatPlugboardByMachine()
        writePlugboardToFile()
    if through == 'm':
        readPlugboardFromFile()
    print("Plugboard:\n", plugboard)


def creatPlugboardByMachine():
    global plugboard
    plugs = list(string.ascii_uppercase)
    shuffle(plugs)

    num = int(len(plugs) / 2)
    plugboard = dict(
        dict(zip(plugs[:num], plugs[num:])),
        **dict(zip(plugs[num:], plugs[:num])))


def writePlugboardToFile():
    with open(plugboradFile, 'w') as f:
        f.write(str(plugboard))


def readPlugboardFromFile():
    global plugboard
    with open(plugboradFile, 'r') as f:
        plugboard = eval(f.read())


def changeCharByPlugboard():
    global char
    char = plugboard[char]


def getPlainText():
    global plainText
    with open(plainTextFile, 'r') as f:
        plainText = f.read()
    cleanText()


def cleanText():
    global plainText
    cop = re.compile("[^a-z^A-Z]")
    plainText = cop.sub('', plainText).upper()


def getCipherText():
    global char, cipherText
    cipherText = ''
    for char in plainText:
        encipherAndDecipher(Rotor.rotorList, 1)
        changeCharByPlugboard()
        encipherAndDecipher(Rotor.rotorList, -1)
        cipherText += char
        linkAndMoveRotors(Rotor.rotorList, 0)


def encipherAndDecipher(rotorList, sign):
    global char
    alphabet = string.ascii_uppercase
    i = 0
    for rotor in rotorList:
        orig_index = alphabet.find(char)
        change_index = rotor.order[i % len(alphabet)] * sign
        new_index = (orig_index + change_index) % len(alphabet)
        char = alphabet[new_index]
        i += 1


def linkAndMoveRotors(rotorList, counter):
    """Characters' number can not beyond 26  ** the number of rotors."""
    move(rotorList[counter])
    if rotorList[counter].order == rotorList[counter].orderOrig:
        # print("move", counter + 1)
        linkAndMoveRotors(rotorList, counter + 1)


def move(rotor):
    first_char = rotor.order.pop(0)
    rotor.order.append(first_char)


def saveCipherTextToFile():
    with open(cipherTextFile, 'w') as f:
        f.write(cipherText)
    print("cipherText Saved!")


setFiles()
rotor0, rotor1, rotor2 = Rotor(), Rotor(), Rotor()
getPasswords()
getPlugboard()
getPlainText()
getCipherText()
saveCipherTextToFile()
