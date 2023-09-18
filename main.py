"""2. Написать функцию, которая принимает три целых числа x, a, b и с помощью генераторного выражения создает и возвращает новый список длинной x случайных чисел от a до b.
Для решения данного задания рекомендуется использовать
функцию random.randint()."""

import random


def main():
    print("Введите длинну списка X и его диапазон A,B")
    x = int(input())
    a = int(input())
    b = int(input())
    numbers = []

    for i in range(x):
        numbers.append(random.randint(a, b))

    print(numbers)


main()
