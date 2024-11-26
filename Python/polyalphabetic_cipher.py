import argparse
from string import ascii_uppercase
from typing import List, Tuple
from cipher import Cipher, non_alpha_pattern


class PolyalphabeticCipher(Cipher):
    def __init__(
        self,
        alphabet: str,
        keyword: str,
        input_file: str,
        output_file: str,
        is_decrypt: bool = False,
    ):
        super().__init__(alphabet, input_file, output_file)
        self.keyword: str = keyword
        self.methods: List[int] = self.translate_keyword_to_methods()
        self.is_decrypt: bool = is_decrypt

    def translate_keyword_to_methods(self) -> List[int]:
        return [self.alphabet.find(char) + 1 for char in self.keyword]

    def encrypt(self) -> None:
        sign: int = 1 if not self.is_decrypt else -1
        for i in range(len(self.plain_text)):
            index_new: int = self.change_index(
                self.alphabet_index[self.plain_text[i]],
                self.methods[i % len(self.methods)] * sign,
                len(self.alphabet_index),
            )
            self.encrypted_text += self.alphabet[index_new]


def get_argvs(argv: List[str]) -> Tuple:
    parser = argparse.ArgumentParser(
        description="Encrypt text using Polyalphabetic cipher."
    )
    parser.add_argument("-k", "--keyword", required=True, help="Select a keyword")
    parser.add_argument("-i", "--input", required=True, help="Input text file")
    parser.add_argument("-o", "--output", required=True, help="Output text file")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt text")

    args = parser.parse_args(argv[1:])
    return args.keyword.upper(), args.input, args.output, args.decrypt


if __name__ == "__main__":
    import sys

    keyword: str
    input_file: str
    output_file: str
    keyword, input_file, output_file, is_decrypt = get_argvs(sys.argv)

    polyalphabetic_cipher: PolyalphabeticCipher = PolyalphabeticCipher(
        ascii_uppercase, keyword, input_file, output_file, is_decrypt
    )
    polyalphabetic_cipher.get_text()
    polyalphabetic_cipher.clean_text(non_alpha_pattern)
    polyalphabetic_cipher.encrypt()
    polyalphabetic_cipher.save_file()
