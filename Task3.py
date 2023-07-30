"""
Задание №7
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
"""

# Так же взял ваше решение.

import pickle
from pathlib import Path

def print_pickle_str(file_name: Path):
    with open(file_name, "r", newline='', encoding='utf-8') as f_csv:
        print(pickle.dumps(f_csv.read()))


if __name__ == '__main__':
    print_pickle_str(Path("new_user.csv"))
