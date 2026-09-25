with open("plain.txt") as f:
    plain_text = f.read()

print(plain_text)

alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher_text: str = ""
for c in plain_text:
    c_idx: int = alphabet.index(c)
    c_new_idx: int = (c_idx + 3) % 26
    c_new = alphabet[c_new_idx]
    cipher_text += c_new

with open("cipher.txt", "w") as f:
    f.write(cipher_text)
