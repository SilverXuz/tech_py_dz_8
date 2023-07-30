"""
Задание №6
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестирования возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""

# Не решил, взял ваше решение. Разъяснение с лекции послушал.

import pickle
import csv
from pathlib import Path


def pickle_to_csv(file_name: Path):
    with (open(file_name, 'rb') as f_pickle,
          open(f'{file_name.stem}.csv', "w", newline='', encoding='utf-8') as f_csv):
        new_dict = pickle.load(f_pickle)

    csv_write = csv.writer(f_csv, dialect='excel', delimiter=',')
    csv_write.writerow(new_dict.keys())

    n = [str(i).split() for i in new_dict.values()]
    csv_write.writerows(n)

if __name__ == '__main__':
    pickle_to_csv(Path("names.pickle"))
