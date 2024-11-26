import argparse
import re
from typing import Dict, List, Tuple, Pattern
from string import ascii_uppercase


non_alpha_pattern: Pattern[str] = re.compile("[^a-zA-Z]")


class Cipher:
    def __init__(
        self,
        alphabet: str,
        input_file: str,
        output_file: str,
        method: int = 3,
        methods: List[int] = [3, 1, 20],
    ) -> None:
        self.alphabet: str = alphabet
        self.method: int = method
        self.methods: List[int] = methods
        self.alphabet_index: Dict[str, int] = {
            letter: index for index, letter in enumerate(self.alphabet)
        }
        self.input_file: str = input_file
        self.output_file: str = output_file
        self.input_text: str = ""
        self.plain_text: str = ""
        self.encrypted_text: str = ""

    def get_text(self) -> None:
        with open(self.input_file, "r") as f:
            self.input_text = f.read()

    def clean_text(self, regex_pattern: Pattern[str]) -> None:
        self.plain_text = regex_pattern.sub("", self.input_text).upper()

    def encrypt(self) -> None:
        for i in range(len(self.plain_text)):
            index_new: int = self.change_index(
                self.alphabet_index[self.plain_text[i]],
                self.method,
                len(self.alphabet_index),
            )
            self.encrypted_text += self.alphabet[index_new]

    def change_index(self, index: int, method: int, alphabet_length: int) -> int:
        return (index + method) % alphabet_length

    def save_file(self) -> None:
        with open(self.output_file, "w") as f:
            f.write(self.encrypted_text)


def get_argvs(argv: List[str]) -> Tuple[int, str, str]:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Encrypt text using Caesar cipher."
    )
    parser.add_argument(
        "-m", "--method", type=int, default=3, help="Integer (default: 3)"
    )
    parser.add_argument(
        "-i",
        "--input",
        default="input_file.txt",
        help="Input text file (default: input_file.txt)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output_file.txt",
        help="Output text file (default: output_file.txt)",
    )

    args = parser.parse_args(argv[1:])
    return args.method, args.input, args.output


if __name__ == "__main__":
    import sys

    method: int
    input_file: str
    output_file: str
    method, input_file, output_file = get_argvs(sys.argv)

    cipher_caesar: Cipher = Cipher(ascii_uppercase, input_file, output_file, method)
    cipher_caesar.get_text()
    cipher_caesar.clean_text(non_alpha_pattern)
    cipher_caesar.encrypt()
    cipher_caesar.save_file()
