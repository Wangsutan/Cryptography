import sys
import getopt
import string
import re


def getArgvs(argv):
    basicInfo = f"{argv[0]} -m <method> -i <input text file> -o <output text file>"

    try:
        opts, args = getopt.getopt(argv[1:], "hm:i:o:")
    except getopt.GetoptError as err:
        print(f"BASIC USAGE: python {basicInfo}")
        print(f">>>> ERROR: {err}")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h"):
            print("python", basicInfo)
            sys.exit()
        elif opt in ("-m"):
            method = int(arg)
        elif opt in ("-i"):
            inputFile = arg
        elif opt in ("-o"):
            outputFile = arg
    return method, inputFile, outputFile


def getTextFrom(inputFile):
    with open(inputFile, 'r') as f:
        inputText = f.read()
    return inputText


def saveFileFromTo(outputText, outputFile):
    with open(outputFile, 'w') as f:
        f.write(outputText)


def getPlainTextFrom(inputText):
    cop = re.compile("[^a-z^A-Z]")
    plainText = cop.sub('', inputText).upper()
    return plainText


def encryptText(alphabet, method, plainText):
    cipherText = ""
    for char in plainText:
        alphabet_index_orig = alphabet.find(char)
        alphabet_index_new = (alphabet_index_orig + method) % len(alphabet)
        cipherText += alphabet[alphabet_index_new]
    return cipherText


if __name__ == "__main__":
    alphabet = string.ascii_uppercase
    method, inputFile, outputFile = getArgvs(sys.argv)

    inputText = getTextFrom(inputFile)
    plainText = getPlainTextFrom(inputText)

    cipherText = encryptText(alphabet, method, plainText)
    saveFileFromTo(cipherText, outputFile)
