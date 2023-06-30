"""
用户需要考虑的数据

- rotors num
- passwords: m or M
- plugboard: m or M
- plain text
- cipher text

"""

import sys
import getopt


def getArgvs(argv):
    rotorsNum = 3
    passwordfrom = 'm'
    plugboardfrom = 'm'
    inputFile = "plainText.txt"
    outputFile = "cipherText.txt"

    basicInfo = f"{argv[0]} --rottorsnum=4 --passwordfrom=M --plugboardfrom=M -i plainText.txt -o cipherText.txt"

    try:
        opts, args = getopt.getopt(argv[1:], "h:n:i:o:", ["rottorsnum", "passwordfrom", "plugboardfrom"])
    except getopt.GetoptError as err:
        print(f"BASIC USAGE: python {basicInfo}")
        print(f">>>> ERROR: {err}")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h"):
            print("python", basicInfo)
            sys.exit()
        elif opt in ("-n", "--rottorsnum"):
            rotorsNum = arg
        elif opt in ("--passwordfrom"):
            passwordfrom = arg
        elif opt in ("--plugboardfrom"):
            plugboardfrom = arg
        elif opt in ("-i"):
            inputFile = arg
        elif opt in ("-o"):
            outputFile = arg
    return rotorsNum, passwordfrom, plugboardfrom, inputFile, outputFile

rotorsNum, passwordfrom, plugboardfrom, inputFile, outputFile = getArgvs(sys.argv)