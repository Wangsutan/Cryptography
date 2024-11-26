import sys
import argparse
import string
from random import shuffle, randint
from typing import List, Dict, Tuple
from cipher import Cipher, non_alpha_pattern


# Default settings for the Enigma machine
alphabet_default: str = string.ascii_uppercase
input_file_default: str = "input.txt"
output_file_default: str = "output.txt"
reflector_file_default: str = "reflector.txt"
rotor_num_default: int = 3
passwords_file_default: str = "passwords.txt"
rotors_cursor_file_default: str = "rotors_cursor.txt"
plugboard_file_default: str = "plugboard.txt"
reflector_from_default: str = "M"
passwords_from_default: str = "M"
rotors_cursor_from_default: str = "M"


class Rotor:
    """
    Rotor class for Enigma machine
    """

    def __init__(self) -> None:
        """
        Initializes the rotor with an empty order and a cursor set to 0.
        """
        self.order: List[int] = []
        self.cursor: int = 0

    def generate_order(self, alphabet: str):
        """
        The order determines the mapping of letters for encryption.
        """
        self.order = list(range(1, len(alphabet)))
        shuffle(self.order)

    def set_order(self, order: List[int]) -> None:
        self.order = order

    def generate_cursor(self) -> None:
        """
        Sets the cursor to a random position within the order.
        The cursor affects the letter mapping for each encryption step.
        """
        right_edge_of_order = len(self.order) - 1
        self.cursor = randint(0, right_edge_of_order)

    def set_cursor(self, cursor: int) -> None:
        right_edge_of_order = len(self.order) - 1
        if 0 <= cursor <= right_edge_of_order:
            self.cursor = cursor
        else:
            raise ValueError("Invalid cursor position")

    def move_cursor(self):
        """
        Moves the cursor to the next position in the order.
        """
        self.cursor = (self.cursor + 1) % len(self.order)


class Enigma(Cipher):
    """
    This Enigma machine class encapsulates the entire Enigma machine,
    including its reflector, rotors, and plugboard.
    """

    def __init__(
        self,
        alphabet: str = alphabet_default,
        input_file: str = input_file_default,
        output_file: str = output_file_default,
        reflector_file: str = reflector_file_default,
        rotor_num: int = rotor_num_default,
        passwords_file: str = passwords_file_default,
        rotors_cursor_file: str = rotors_cursor_file_default,
        plugboard_file: str = plugboard_file_default,
        reflector_from: str = reflector_from_default,
        passwords_from: str = passwords_from_default,
        rotors_cursor_from: str = rotors_cursor_from_default,
    ) -> None:
        super().__init__(alphabet, input_file, output_file)
        self.reflector_file: str = reflector_file
        self.rotor_num: int = rotor_num
        self.passwords_file: str = passwords_file
        self.rotors_cursor_file: str = rotors_cursor_file
        self.plugboard_file: str = plugboard_file
        self.reflector_from: str = reflector_from
        self.passwords_from: str = passwords_from
        self.rotors_cursor_from: str = rotors_cursor_from

        self.reflector: Dict[str, str] = self.set_reflector(
            self.reflector_from, self.alphabet, self.reflector_file
        )

        self.rotor_list: List[Rotor]
        self.rotor_list = self.set_rotors(
            self.rotor_num,
            self.passwords_file,
            self.rotors_cursor_file,
            self.passwords_from,
            self.rotors_cursor_from,
        )

        self.plugboard: Dict[str, str] = self.set_plugboard(self.plugboard_file)

    # Reflector-related methods
    def set_reflector(
        self, reflector_from: str, alphabet: str, reflector_file: str
    ) -> Dict[str, str]:
        reflector: Dict[str, str] = {}
        if reflector_from == "m":
            reflector = self.create_reflector_from_machine(alphabet, reflector_file)
        if reflector_from == "M":
            reflector = self.set_reflector_from_manual(reflector_file)
        return reflector

    def create_reflector_from_machine(
        self, alphabet: str, reflector_file: str
    ) -> Dict[str, str]:
        reflector: Dict[str, str] = {}

        plugs: List[str] = list(alphabet)
        shuffle(plugs)

        num: int = int(len(plugs) / 2)
        dict1: Dict[str, str] = dict(zip(plugs[:num], plugs[num:]))
        dict2: Dict[str, str] = dict(zip(plugs[num:], plugs[:num]))
        reflector = {**dict1, **dict2}

        with open(reflector_file, "w") as f:
            f.write(str(reflector))

        return reflector

    def set_reflector_from_manual(self, reflector_file: str) -> Dict[str, str]:
        reflector: Dict[str, str] = {}
        with open(reflector_file, "r") as f:
            reflector = eval(f.read())
        return reflector

    # Rotor-related methods
    def set_rotors(
        self,
        rotor_num: int,
        passwords_file: str,
        rotors_cursor_file: str,
        passwords_from: str,
        rotors_cursor_from: str,
    ) -> List[Rotor]:
        rotor_list: List[Rotor] = [Rotor() for _ in range(rotor_num)]
        rotor_list = self.set_passwords(rotor_list, passwords_file, passwords_from)
        rotor_list = self.set_cursors(
            rotor_list, rotors_cursor_file, rotors_cursor_from
        )
        return rotor_list

    # Passwords of rotors
    def set_passwords(
        self, rotor_list: List[Rotor], passwords_file: str, passwords_from: str
    ) -> List[Rotor]:
        if passwords_from == "m":
            rotor_list = self.set_passwords_from_machine(rotor_list, passwords_file)
        if passwords_from == "M":
            rotor_list = self.set_passwords_from_manual(rotor_list, passwords_file)
        return rotor_list

    def set_passwords_from_machine(
        self, rotor_list: List[Rotor], passwords_file: str
    ) -> List[Rotor]:
        with open(passwords_file, "w") as f:
            for rotor in rotor_list:
                rotor.generate_order(self.alphabet)
                f.write(str(rotor.order) + "\n")
        return rotor_list

    def set_passwords_from_manual(
        self, rotor_list: List[Rotor], passwords_file: str
    ) -> List[Rotor]:
        """
        If the numbers of rotors and passwords are not equal,
        it will print an error message and exit the program.
        """
        with open(passwords_file, "r") as f:
            passwords: List[List[int]] = eval(", ".join(f.read().split("\n")))
        if len(passwords) != len(rotor_list):
            print("The numbers of passwords and rotors are not equal.")
            sys.exit(2)
        for i in range(len(rotor_list)):
            rotor_list[i].set_order(passwords[i])
        return rotor_list

    # Cursors of rotors
    def set_cursors(
        self,
        rotor_list: List[Rotor],
        rotors_cursor_file: str,
        rotors_cursor_from: str,
    ) -> List[Rotor]:
        if rotors_cursor_from == "m":
            rotors_list = self.set_cursors_from_machine(rotor_list, rotors_cursor_file)
        if rotors_cursor_from == "M":
            rotors_list = self.set_cursors_from_manual(rotor_list, rotors_cursor_file)
        return rotors_list

    def set_cursors_from_machine(
        self, rotor_list: List[Rotor], rotors_cursor_file: str
    ) -> List[Rotor]:
        with open(rotors_cursor_file, "w") as f:
            for rotor in rotor_list:
                rotor.generate_cursor()
                f.write(str(rotor.cursor) + "\n")
        return rotor_list

    def set_cursors_from_manual(
        self, rotor_list: List[Rotor], rotors_cursor_file: str
    ) -> List[Rotor]:
        """
        If the numbers of cursors and rotors are not equal,
        it will print an error message and exit the program.
        """
        with open(rotors_cursor_file, "r") as f:
            cursors: List[int] = [int(line.strip()) for line in f if line.strip()]
        if len(cursors) != len(rotor_list):
            print("The numbers of cursors and rotors are not equal.")
            sys.exit(2)
        for i in range(len(rotor_list)):
            rotor_list[i].set_cursor(cursors[i])
        return rotor_list

    # Plugboard
    def set_plugboard(self, plugboard_file: str) -> Dict[str, str]:
        """
        Sets up the plugboard by reading the plugboard file.
        """
        plugboard: Dict[str, str] = {}
        with open(plugboard_file, "r") as f:
            for line in f:
                if line.strip() and "-" in line:
                    pair = line.split("-")
                    letter1: str = pair[0].strip().upper()
                    letter2: str = pair[1].strip().upper()
                    temp_dict: Dict = {letter1: letter2, letter2: letter1}
                    plugboard.update(temp_dict)
        return plugboard

    def use_plugboard(self, char: str) -> str:
        if char in self.plugboard:
            char = self.plugboard[char]
        return char

    # Encipher and decipher
    def encrypt(self) -> None:
        for char in self.plain_text:
            char = self.use_plugboard(char)
            char = self.encipher_and_decipher(char, 1)
            char = self.reflector[char]
            char = self.encipher_and_decipher(char, -1)
            char = self.use_plugboard(char)
            self.encrypted_text += char
            self.link_and_move_rotors()

    def encipher_and_decipher(self, char: str, sign: int) -> str:
        for rotor in self.rotor_list:
            method = rotor.order[rotor.cursor] * sign
            index: int = self.alphabet_index[char]
            index_new: int = self.change_index(index, method, len(self.alphabet_index))
            char = self.alphabet[index_new]
        return char

    def link_and_move_rotors(self, i: int = 0) -> None:
        """
        Moves the rotors and updates their cursors after each character is encrypted.
        """
        self.rotor_list[i].move_cursor()
        if self.rotor_list[i].cursor == 0 and i in range(self.rotor_num - 1):
            self.link_and_move_rotors(i + 1)

    # checker
    def check_same_char(self) -> bool:
        """
        Checks if the encrypted text has any characters that match the input text,
        which should not happen with a correct Enigma machine configuration.
        """
        haveSameChar: bool = False
        for i in range(len(self.plain_text)):
            if self.plain_text[i] == self.encrypted_text[i]:
                haveSameChar = True
                break
        if haveSameChar:
            print("It is not true Enigma!")
        return haveSameChar


def get_argvs(argv) -> Tuple:
    """
    Processes command-line arguments for configuring the Enigma machine.

    Encrypt by generating passwords, reflector and cursors:
    > python Enigma.py -i input.txt -o output.txt -n 4 --reflector_from m --passwords_from m --rotors_cursor_from m

    Encrypt with default settings:
    > python Enigma.py -i input.txt -o output.txt

    Decrypt with default settings:
    python Enigma.py -i output.txt -o test.txt

    Set rotor number by -n argument:

    > python Enigma.py -i input.txt -o output.txt -n 4

    Decrypt with certain rotor number:

    > python Enigma.py -i output.txt -o test.txt -n 4

    Set plugboard by plugboard.txt. Each line is a pair of letters.
    """
    parser = argparse.ArgumentParser(description="Process Enigma machine settings.")
    parser.add_argument(
        "-i",
        "--input",
        default=input_file_default,
        help=f"Input text file (default: {input_file_default})",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=output_file_default,
        help=f"Output text file (default: {output_file_default})",
    )
    parser.add_argument(
        "--reflector_file",
        default=reflector_file_default,
        help=f"Reflector file (default: {reflector_file_default})",
    )
    parser.add_argument("-n", type=int, default=3, help="Number of rotors (default: 3)")
    parser.add_argument(
        "--passwords_file",
        default=passwords_file_default,
        help=f"Password file (default: {passwords_file_default})",
    )
    parser.add_argument(
        "--rotors_cursor_file",
        default=rotors_cursor_file_default,
        help=f"Rotors cursor (default: {rotors_cursor_file_default})",
    )
    parser.add_argument(
        "--plugboard_file",
        default=plugboard_file_default,
        help=f"Plugboard file (default: {plugboard_file_default})",
    )
    parser.add_argument(
        "--reflector_from",
        default=reflector_from_default,
        help=f"Machine: 'm', Manual: 'M' (default: {reflector_from_default})",
    )
    parser.add_argument(
        "--passwords_from",
        default=passwords_from_default,
        help=f"Machine: 'm', Manual: 'M' (default: {passwords_from_default})",
    )
    parser.add_argument(
        "--rotors_cursor_from",
        default=rotors_cursor_from_default,
        help=f"Machine: 'm', Manual: 'M' (default: {rotors_cursor_from_default})",
    )

    args = parser.parse_args(argv[1:])

    return (
        args.input,
        args.output,
        args.reflector_file,
        args.n,
        args.passwords_file,
        args.rotors_cursor_file,
        args.plugboard_file,
        args.reflector_from,
        args.passwords_from,
        args.rotors_cursor_from,
    )


if __name__ == "__main__":
    enigma: Enigma = Enigma(alphabet_default, *get_argvs(sys.argv))

    enigma.get_text()
    enigma.clean_text(non_alpha_pattern)
    enigma.encrypt()

    enigma.check_same_char()
    enigma.save_file()
