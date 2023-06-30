# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 19:04:38 2021
"""

import string
from collections import Counter


step = int(input("set step as int:"))
# print("step:", step)

alphabet = list(string.ascii_uppercase)

cipherFile = "cipher_poly.txt"
with open(cipherFile, 'r') as f:
    text = f.read()
text = list(filter(str.isalpha, text))
text = [char.upper() for char in text]

complement = len(text) % step
text += 'A' * complement

charsLists = [[] for i in range(step)]
for startAddr in range(step):
    stepCounter = 0
    index = startAddr + step * stepCounter
    while index < len(text):
        charsLists[startAddr].append(text[index])
        stepCounter += 1
        index = startAddr + step * stepCounter

for i in range(step):
    print("".join(charsLists[i]))

for j in range(len(charsLists)):
    for k in range(len(charsLists[j])):
        charsLists[j][k] = alphabet.index(charsLists[j][k])
# print(charsLists)

charsCounters = [[] for i in range(step)]
for i in range(len(charsLists)):
    charsCounters[i] = Counter(charsLists[i]).most_common(1)
print("charsCounters:", charsCounters)

letterFrequency = "ETAONRISHDLFCMUGYPWBVKJXQZ"
letterFrequencyNum = [alphabet.index(letter) for letter in letterFrequency]

while True:
    correspond = list(map(int, input(f"Set {step} numbers of decoding:").split()))
    plainChars = [[] for i in range(step)]
    for i in range(step):
        distanceIndex = charsCounters[i][0][0] - letterFrequencyNum[correspond[i]]
        for charNum in charsLists[i]:
            plainChars[i].append(alphabet[(charNum - distanceIndex) % 26])
    plainStr = ''
    for index in range(len(plainChars[0])):
        plainStr += plainChars[0][index] + plainChars[1][index] + plainChars[2][index]

    result = plainStr[:-complement] if complement != 0 else plainStr
    print(result)
