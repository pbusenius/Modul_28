import random

from typing import Dict


LENGTH_OF_WORD_LIST = 1000
WORD_LIST_FILE = "passwords.txt"


def to_file(word_list: Dict):
    with open(WORD_LIST_FILE, "w") as file:
        for word in word_list:
            file.write(f"{word}\n")


def main():
    word_list_dict = {}

    while len(word_list_dict) < LENGTH_OF_WORD_LIST:
        random_value = random.randint(111111, 999999)

        word_list_dict[random_value] = True

    to_file(word_list_dict)

if __name__ == "__main__":
    main()