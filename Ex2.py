#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В основной ветке программы вызывается функция cylinder(), которая вычисляет площадь цилиндра. В теле cylinder()
# определена функция circle(), вычисляющая площадь круга по формуле . В теле cylinder() у пользователя спрашивается,
# хочет ли он получить только площадь боковой поверхности цилиндра, которая вычисляется по формуле , или полную
# площадь цилиндра. В последнем случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
# вычислений функции circle().

import math


def circle(R):
    return R ** 2 * math.pi


def cylinder(R, h, full=True):
    circle(R)

    S_cylinder = 2 * math.pi * R * h

    if full:
        return S_cylinder + 2 * circle(R)
    else:
        return S_cylinder


if __name__ == '__main__':
    r = float(input("R= "))
    h = float(input("h= "))
    c = input("Площадь боковой поверхности S_cylinder или полная площадь full?")
    s = cylinder(r, h, full=(c == 'full'))
    print(s)
