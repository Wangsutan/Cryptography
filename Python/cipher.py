import argparse
import re
from typing import Dict, List, Tuple, Pattern
from string import ascii_uppercase
import concurrent.futures
import timeit


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
        try:
            with open(self.input_file, "r") as f:
                self.input_text = f.read()
        except FileNotFoundError:
            print(f"Error: The file {self.input_file} does not exist.")
            exit(1)

    def clean_text(self, regex_pattern: Pattern[str]) -> None:
        self.plain_text = regex_pattern.sub("", self.input_text).upper()

    def change_index(self, index: int, method: int, alphabet_length: int) -> int:
        return (index + method) % alphabet_length

    def encrypt_char(self, char: str) -> str:
        index_new: int = self.change_index(
            self.alphabet_index[char],
            self.method,
            len(self.alphabet_index),
        )
        return self.alphabet[index_new]

    def encrypt(self) -> None:
        self.encrypted_text = "".join(
            self.encrypt_char(char) for char in self.plain_text
        )

    def encrypt_in_parallel(self) -> None:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            self.encrypted_text = "".join(
                executor.map(self.encrypt_char, self.plain_text)
            )

    def save_file(self) -> None:
        try:
            with open(self.output_file, "w") as f:
                f.write(self.encrypted_text)
        except IOError:
            print(f"Error: Unable to write to file {self.output_file}.")
            exit(1)


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

    # Measure the time for serial encryption
    serial_time = timeit.timeit(lambda: cipher_caesar.encrypt(), number=10000)
    print(f"Serial encryption time: {serial_time / 10:.4f} seconds")

    cipher_caesar.encrypted_text = ""

    # Measure the time for parallel encryption
    parallel_time = timeit.timeit(
        lambda: cipher_caesar.encrypt_in_parallel(), number=10000
    )
    print(f"Parallel encryption time: {parallel_time / 10:.4f} seconds")

    # Save the encrypted text from parallel encryption
    cipher_caesar.encrypt()
    cipher_caesar.save_file()
