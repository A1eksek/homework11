# f = open('text.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()

'''Первая задача'''
def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())


# read_last(3, 'text.txt')
'''Вторая задача'''

import os


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)


# print_docs('C:\Program Files')

'''Третья задача'''


def longest_words(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


# print(longest_words('text.txt'))