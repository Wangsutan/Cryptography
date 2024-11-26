import string
import random
from type import List


def check_crib(string_cipyer: str, crib: str) -> List[int]:
    consistency_index: List[int] = []
    i: int = 0
    while i <= len(string_cipyer) - len(crib):
        is_conflict: bool = False
        j: int = 0
        while j < len(crib):
            if string_cipyer[i + j] == crib[j]:
                is_conflict = True
                break
            j += 1
        if not is_conflict:
            consistency_index.append(i)
        i += 1
    return consistency_index


if __name__ == "__main__":
    string_cipyer: str = "".join(random.choice(string.ascii_uppercase) for _ in range(100))
    crib: str = input("CRIB: ").upper()
    consistency_index: List[int] = check_crib(string_cipyer, crib)
    print(f"{len(consistency_index)} results:\n{consistency_index}")
