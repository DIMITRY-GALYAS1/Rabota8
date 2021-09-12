#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    school = {'1а': 20, '1б': 21, '2а': 15, '2б': 33, '3a': 29, '3б': 23, '4а': 25, "4б": 33}
    print('1 - Изменилось количество учеников:')
    print('2 - В школе появился новый класс')
    print('3 - В школе был расформирован класс')
    print('4 - Выгрузка данных')
    print('5 - Выход')

    while True:
        n = int(input('Введите номер операции >>> '))
        if n == 1:
            school.update({input(f'Название изменяемого класса: '): int(input(f'Новое количество учеников:'))})
        elif n == 2:
            school.update({input(f'Название класса №: '): int(input(f'Количество учеников класса №: '))})
        elif n == 3:
            del school[input(f'Название расформировываемого класса: ')]
        elif n == 4:
            print(school)
        elif n == 5:
            break
        else:
            print(f"Неизвестная команда", file=sys.stderr)
            break
