"""
## Циклы + Условные операторы

1. Напишите проверку число на простату (число является простым, если оно делится нацело только на себя и единицу)
2. Выведете все простые числа для заданного интервала
3. Выведете все числа в заданном интервале, позиция которых четна/нечетна (режим работы должен определятся из некоторой переменной которая при значении True должны выводить числа стоящие на четной позиции и наоборот).
4. Запустите вечный цикл при этом на каждом шаге цикла просите ввести некоторое значение пользователя (команда input(...)), если пользователь ввел букву q то ваша программа должна завершаться
5. Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
6. Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
7. Найдите все тройки пифагора для заданного интервала

Выполнил Д. Яковлев
"""

import math
import random

def main():
    print("Enter some integer:")
    user_int = get_int()
    print(str(is_prime(user_int)))


def get_int():
    """
    Iteratively gets integer from std_in
    """
    user_data = input()
    while not is_integer(user_data):
        print("This is not an integer, try again:")
        user_data = input()
    return int(user_data)


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_prime(number = 2):
    for divisor in range(2,int(pow(number,0.5))):
        if number % divisor == 0:
            return False
    return True


if __name__ == '__main__':
    main()