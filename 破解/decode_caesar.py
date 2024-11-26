import string
from collections import Counter


def getCipherTextFrom(cipherFile):
    with open(cipherFile, 'r') as f:
        cipherText = f.read()

    cipherText = list(filter(str.isalpha, cipherText))
    cipherChars = [char.upper() for char in cipherText]
    return cipherChars


def counterChars(cipherChars):
    top_num = 1
    charsCounter = Counter(cipherChars).most_common(top_num)
    print("counter(top %d):" % top_num, charsCounter)
    return charsCounter


def decode(alphabet, cipherChars, letterFrequency, charsCounter):
    for letter in letterFrequency:
        distanceIndex = (
            alphabet.index(charsCounter[0][0]) - alphabet.index(letter) + 26
        ) % 26

        plainChars = [
            alphabet[(alphabet.index(char) - distanceIndex + 26) % 26]
            for char in cipherChars
        ]

        print(f"Move {distanceIndex}:")
        print("".join(plainChars))

        if input("\nReally?(`Enter` to continue, q to quit):") != '':
            break


alphabet = list(string.ascii_uppercase)
letterFrequency = "ETAONRISHDLFCMUGYPWBVKJXQZ"
cipherChars = getCipherTextFrom("cipher.txt")
charsCounter = counterChars(cipherChars)

decode(alphabet, cipherChars, letterFrequency, charsCounter)
