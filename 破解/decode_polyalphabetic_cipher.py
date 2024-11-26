import string
from collections import Counter
from typing import List


ALPHABET: str = string.ascii_uppercase
LETTER_FREQUENCY: str = "ETAONRISHDLFCMUGYPWBVKJXQZ"


def get_cipher_text(cipherFile: str) -> str:
    with open(cipherFile, "r") as f:
        return "".join(char.upper() for char in f.read() if str.isalpha(char))


def count_text_by_step(cipher_text: str, step: int) -> List[str]:
    chars_most_common_by_step: List[str] = []
    for s in range(step):
        cipher_chars_by_step: List[str] = [
            cipher_text[i] for i in range(s, len(cipher_text), step)
        ]
        char_most_common: str = Counter(cipher_chars_by_step).most_common(1)[0][0]
        chars_most_common_by_step.append(char_most_common)
    return chars_most_common_by_step


def is_belong(begin: int, end: int, step: int, idx: int) -> bool:
    return idx in range(begin, end, step)


def decrypt_char(alphabet: str, cipher_char: str, distance: int) -> str:
    return alphabet[(alphabet.index(cipher_char) - distance + 26) % 26]


step: int = int(input("set step (such as 3): "))
cipher_text: str = get_cipher_text("cipher_poly.txt")
chars_most_common_by_step: List[str] = count_text_by_step(cipher_text, step)

while True:
    input_str: str = input("Input keys such as `0 0 0` to continue or `q` to quit: ")
    if input_str == "q":
        break
    keys: List[int] = list(map(int, input_str.split()))

    plain_text: str = ""
    for idx in range(len(cipher_text)):
        for s in range(step):
            if is_belong(s, len(cipher_text), step, idx):
                char_most_common_idx: int = ALPHABET.index(chars_most_common_by_step[s])
                char_frequency_idx: int = ALPHABET.index(LETTER_FREQUENCY[keys[s]])
                distance: int = char_most_common_idx - char_frequency_idx
                plain_text += decrypt_char(ALPHABET, cipher_text[idx], distance)
                break
    print(plain_text)
