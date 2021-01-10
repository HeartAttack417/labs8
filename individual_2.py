#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys


# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение


def add(trains, name, number, time):
    train = {
        'name': name,
        'number': number,
        'time': time,
    }

    trains.append(train)
    if len(trains) > 1:
        trains.sort(key=lambda item: item.get('name', ''))


def list(trains):
    table = []
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 25,
        '-' * 20,
        '-' * 20
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^25} | {:^20} | {:^20} |'.format(
            "№",
            "Пункт назначения",
            "Номер поезда",
            "Время отправления"
        )
    )
    table.append(line)

    for idx, train in enumerate(trains, 1):
        table.append(
            '| {:>4} | {:<25} | {:<20} | {:>20} |'.format(
                idx,
                train.get('name', ''),
                train.get('number', 0),
                train.get('time', 0)
            )
        )

    table.append(line)

    return '\n'.join(table)


def select(number):
    count = 0
    for train in trains:
        if number == train.get('number', ''):
            count += 1
            print(
                '{:>4}: Пункт назначения - {}, время отправления - {}'.format(count, train.get('name', ''),
                                                                              train.get('time', '')
                                                                              )
            )
        if count == 0:
            print("Поездов с таким номером  не найдено.")


def load(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def save(trains, filename):
    with open(filename, 'w') as f:
        json.dump(trains, f)


if __name__ == '__main__':
    trains = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Введите пункт назначения  ")
            number = input("Введите номер поезда ")
            time = input("Введите время отправления ")
            add(trains, name, number, time)

        elif command == 'list':
            print(list(trains))

        elif command.startswith('select '):
            parts = command.split(maxsplit=1)
            select(parts[1])

        elif command.startswith('load '):
            parts = command.split(maxsplit=1)
            trains = load(parts[1])

        elif command.startswith('save '):
            parts = command.split(maxsplit=1)
            save(trains, parts[1])

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - Добавить данные;")
            print("list - Вывести данные;")
            print("select <номер> - Вывести всю информацию по поезду с введенным номером;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
