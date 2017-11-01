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

    """
    # 1. Prime numbers
    print("1. Enter some integer:")
    user_int = get_int()
    print("Number " + str(user_int) + " is" + ("" if is_prime(user_int) else " not") + " prime.")
    print("______\n")
    print(str(int(True)) + " " + str(int(False)))
    """
    # 2. Primes in interval
    print("2. Enter begin of prime range:")
    u_begin = get_int()
    print("   Enter end of prime range:")
    u_end  = get_int()
    print("Primes here are:\n" + list_to_str(prime_interval(u_begin, u_end)))


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
    if number < 0:
        number *= -1
    for divisor in range(2,int(pow(number,0.5) + 1)):
        if number % divisor == 0:
            return False
    return True


def prime_interval(begin = 2, end = 100000):
    prime_list = []
    if (begin > end) or (begin < 2 and end < 2):
        return prime_list
    if begin < 2 and end >= 2:
        begin = 2
    for i in range(begin,end+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


def list_to_str(ls, row_len = 20):
    out_s = ""
    for i in range(len(ls)):
        out_s += str(ls[i])
        if i < len(ls) - 1:
            out_s += "\t"
        if i % row_len == row_len - 1:
            out_s += "\n"
    return out_s
    

if __name__ == '__main__':
    main()