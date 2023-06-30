# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 09:09:56 2021
"""

import string
import random


def check_crib(string_cipyer, crib):
    consistency_index = []
    i = 0
    while i <= len(string_cipyer) - len(crib):
        conflict = False
        j = 0
        while j < len(crib):
            if string_cipyer[i + j] == crib[j]:
                conflict = True
            j += 1
        if not conflict:
            consistency_index.append(i)
        i += 1
    return consistency_index


charsList = [random.choice(string.ascii_uppercase) for i in range(100)]
string_cipyer = ''.join(charsList)

if __name__ == "__main__":
    crib = input("CRIB: ").upper()
    consistency_index = check_crib(string_cipyer, crib)
    print(f"{len(consistency_index)} results:\n{consistency_index}")
