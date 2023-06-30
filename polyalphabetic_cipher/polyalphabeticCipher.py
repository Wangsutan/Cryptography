#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:03:50 2021
Optimized on Sat Aug  14 08:48:45 2021
Optimized on Sat Jun  3 20:05:36 2023
@author: abc
"""

import sys
import getopt
import string
import re


def getArgvs(argv):
    basicInfo = f"{argv[0]} -k <method> -i <input text file> -o <output text file>"

    try:
        opts, args = getopt.getopt(argv[1:], "hk:i:o:")
    except getopt.GetoptError as err:
        print(f"BASIC USAGE: python {basicInfo}")
        print(f">>>> ERROR: {err}")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h"):
            print("python", basicInfo)
            sys.exit()
        elif opt in ("-k"):
            keyword = arg
        elif opt in ("-i"):
            inputFile = arg
        elif opt in ("-o"):
            outputFile = arg
    return keyword, inputFile, outputFile


def getTextFrom(inputFile):
    with open(inputFile, 'r') as f:
        inputText = f.read()
    return inputText


def saveFileFromTo(outputText, outputFile):
    with open(outputFile, 'w') as f:
        f.write(outputText)


def getMethods(alphabet, keyword):
    keyword = keyword.upper()
    methods = [alphabet.find(char) for char in keyword]
    return methods


def getPlainTextFrom(inputText):
    cop = re.compile("[^a-z^A-Z]")
    plainText = cop.sub('', inputText).upper()
    return plainText


def encryptText(alphabet, methods, plainText):
    cipherText = ""
    for i in range(len(plainText)):
        alphabet_index_orig = alphabet.find(plainText[i])
        alphabet_index_new = (
            alphabet_index_orig + methods[i % len(methods)]
        ) % len(alphabet)
        cipherText += alphabet[alphabet_index_new]
    return cipherText


if __name__ == "__main__":
    alphabet = string.ascii_uppercase
    keyword, inputFile, outputFile = getArgvs(sys.argv)
    methods = getMethods(alphabet, keyword)

    inputText = getTextFrom(inputFile)
    plainText = getPlainTextFrom(inputText)

    cipherText = encryptText(alphabet, methods, plainText)
    saveFileFromTo(cipherText, outputFile)
