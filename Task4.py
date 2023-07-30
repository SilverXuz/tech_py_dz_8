"""
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.
"""

# Использовал решение с семинара. =( 

import os
import json
import csv
import pickle
from pathlib import Path


def get_directory_size(directory_path):
    total_size = 0
    for dir_path, dir_name, file_name in os.walk(directory_path):
        for filename in file_name:
            filepath = os.path.join(dir_path, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def collection(directory_path):
    result = []
    for dir_path, dir_name, file_name in os.listdir(directory_path):
        for name in dir_name:
            little_path = os.path.join(dir_path, name)
            size = get_directory_size(little_path)
            result.append({
                "name": name,
                "type": 'directory',
                "size": size,
                "parent_directory": dir_path
            })
        for name in file_name:
            filepath = os.path.join(dir_path, name)
            size = os.path.getsize(filepath)
            result.append({
                "name": name,
                "type": 'directory',
                "size": size,
                "parent_directory": dir_path
            })

    with (open('directory_data.json', 'w') as json_file,
          open('derectory_data_csv', 'w', newline='') as csv_file,
          open('directory_data.pickle', 'wb') as pickle_file):

        json.dump(result, json_file, indent=2)

        filenames = ['name', 'type', 'size', 'parent_directory']
        writer = csv.DictWriter(csv_file, fieldnames=filenames)
        writer.writeheader()
        writer.writerows(result)

        pickle.dump(result, pickle_file)

if __name__ == '__main__':
    collection(Path.cwd())
