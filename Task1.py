"""
Задание №5
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""

import os
import json
import pickle
from pathlib import Path

def convert_json_to_pickle(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            json_file_path = os.path.join(directory_path, filename)
            pickle_file_path = os.path.join(directory_path, filename.replace(".json", ".pickle"))

            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)

            with open(pickle_file_path, 'wb') as pickle_file:
                pickle.dump(data, pickle_file)

if __name__ == '__main__':
    convert_json_to_pickle(Path.cwd())
