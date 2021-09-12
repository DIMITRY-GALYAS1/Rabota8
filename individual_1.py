#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    print("Список команд:")
    print("add - добавить студента;")
    print("list - вывести список студентов, имеющих оценку 2;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

    students = []
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия и инициалы? ")
            number = input("Номер группы? ")
            z = str(input("Успеваемость? "))

            student = {
                'name': name,
                'number': number,
                'z': z,
            }

            students.append(student)
            if len(student) > 1:
                students.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            count = 0
            for student in students:
                if "2" in student.get('z', ''):
                    count += 1
                    print(
                        student.get('name', ''),
                        student.get('number', '')
                        )
                if count == 0:
                    print("Таких студентов нет")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
            break
