#!/usr/bin/python
import math
import conditions_and_cycles as cas
import string as s

def main():
    """
    ## Функции
    
    1. Напишите функцию не принимающую никаких аргументов, выводящую приветствие с вашим именем
    
    2. Напишите функцию принимающую один аргумент строка, выводящую эту строку
    
    3. Напишите функцию возводящую число в квадрат, возвращающее полученное значение
    
    4. Напишите функцию вычисляющую факториал числа, возвращающее полученное значение
    
    5. Напишите функцию вычисляющую N-ое число последовательности Фибоначчи
    
    6. Напишите функцию вычисляющую N-ое число арифметической последовательности, шаг последовательности должен передаваться дополнительным аргументов (по умолчанию этот аргумент должен быть равен 1)
    
    7. Определите функцию вычисляющую площадь треугольника при этом в качестве параметров должны передаваться значение высоты и основания
    
    8. Определите функцию, которая принимает значение коэффициентов квадратного уравнения и выводит значение корней или предупреждение, что уравнение не имеет корней (в случае если детерминант оказался отрицательным)
    
    9. Напишите функцию, которая для заданного параметров интервала, выводит значение, некоторой математической функции (например: sin, cos ... для этого не забудьте подключить модуль math: `import math`)
    
    10. Напишите функцию, которая для заданного в аргументах списка, возвращает как результат перевернутый список
    
    11. Перепешите функцию для вычисления чисел фибоначи в рекурсивной форме
    
    12. Напишите функцию вычисляющую N-ое число арифметической последовательности в рекурсивной форме
    
    13. Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,  которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.    Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
    """

    print(" 1. function \"hw\"")
    hw()
    print("______\n")

    print(" 2. Function `echo`. Enter some text:")
    s = cas.get_str()
    print("> " + s)
    print("______\n")

    print(" 3. Function square:")
    print(str(square(cas.get_num())))
    print("______\n")

    print(" 4. Factorial of (print an integer):")
    f = cas.get_int()
    print(str(f) + "! = " + str(factorial(f)))
    print("______\n")

    print(" 5. " + str(f) + "-th number of Fibonacci sequence is " + str(cas.binet_fibonacci(f)))
    print("______\n")

    print(" 6. Arythmetical sequence: 10th member with step 3 and offset 0:")
    print(str(arythmetical(10,3)))

    print(" 7. Area of triamgle with base = 34.56, height = 12.7:\nS = " + str(t_area(34.56, 12.7)))
    print("______\n")

    print(" 8. Now I can solve square equations, for example 5x^2 - 4.5x + 1 = 0:")
    square_eq_solve(5, -4.5, 1)
    print("______\n")

    print(" 9. Natural logarythms of all integers in interval 12.45676 .. 45.654:")
    loga(12.45676, 45.654)
    print("______\n")  

    print("10. Function reverse(list): list from tail to head:")
    our_list = "String is a list, actually."
    print(" ==> " + our_list)  
    print("<==  " + cas.list_to_str(reverse(our_list), '', 0, 1, 100))
    print("_____\n")

    print("11. Recursive Fibonacci function. Very slow, be patient...")
    for i in range(31):
        print(str(i) + "\t:\t" + str(fibonacci_recursive(i)))
    print("______\n")

    print("12. Arythmetic sequence recursive:")
    seq = ""
    for i in range(11):
        seq += " " + (str(arythmetical_r(i, 10, -3)))
    print(seq + "\n______\n")

    print("13. And now a weak cipher algorithm. Please enter a line to cipher:")
    u_message = input()
    print("Coded with default key:    " + xor_cipher(u_message))
    print("Decoded with the same key: " + xor_cipher(xor_cipher(u_message)))


def xor_cipher_table():
    t = "x   " + s.ascii_letters + "\n"
    for a in s.ascii_letters:
        t += a + " > "
        for b in s.ascii_letters:
            c = chr(ord(a) ^ ord(b))
            if s.printable[:-5].find(c) + 1:
                t += c
            else:
                t += ' '
        t += "\n"
    print(t)
    return t



def xor_cipher(message = "I am the message.", key = "password"):
    """
    Returns xor'ed string `message` ^ `key`.

    If `key` is empty, return unciphered string.
    """
    if key:
        code = ""
        L = len(message)
        l = len(key)
        chunks = []
        n_chunks = 1 + L // l
        for i in range(n_chunks):
            chunks.append(message[i * l : (i + 1) * l])

        for chunk in chunks:
            for c,k in zip(chunk, key[:len(chunk)]):
                code += chr(ord(c) ^ ord(k))
        return code   
    else:
        return message


def hw():
    print("\tHi, my name is Danila!")


def echo(s):
    """
    Takes string `s` and prints it into *std_out*
    """
    print(str(s))


def square(number):
    """
    Returns `number ** 2`
    """
    return number ** 2


def factorial(n = 100):
    """
    Returns *n*!
    """
    if n < 2:
        return 1
    else:
        F = 1
        for i in range(2, n+1):
            F *= i
        return F


def arythmetical(n, step = 1, offset = 0):
    """
    Return `n`-th number of arythmetical sequence with coreesponding `offset` and `step`.

    a.(n) = a.(n - 1) + `step`

    a_n = `offset + n * step`
    """
    return offset + n * step


def t_area(base = 1, height = 1):
    """
    Area of triangle S = 1/2 hb
    """
    return (base * height)/2


def square_eq_solve(a = 1, b = -1, c = 0):
    """
    Prints roots of an equation `a`x^2 + `b`x + `c` = 0 or error message in case D < 0.
    """
    D = b * b - 4 * a * c
    if D < 0:
        print("Error: this equation have no real roots!")
    else:
        print(str((-b - pow(D, 1/2))/2))
        print(str((-b + pow(D, 1/2))/2))


def loga(begin = 1, end = 10):
    for i in range(math.ceil(begin), math.floor(end) + 1):
        print(str(i) + " -->\t" + str(round(math.log(i),7)))


def reverse(s_list):
    """
    Returns `list` elements in backward order unless it's empty.
    """
    r_list = []
    if s_list:
        for i in range(len(s_list) - 1, -1, -1):
            r_list.append(s_list[i])
    return r_list


def fibonacci_recursive(n_max):
    if n_max < 0:
        #print("-")
        return 0
    elif n_max == 0:
        #print("0")
        return 0
    elif n_max == 1:
        #print("1")
        return 1
    else:
        #print(str(n_max))
        return fibonacci_recursive(n_max - 1) + fibonacci_recursive(n_max - 2)


def arythmetical_r(n, step = 1, offset = 0):
    if n <= 0:
        return offset
    else:
        return arythmetical_r(n - 1, step, offset) + step


if __name__ == "__main__":
    main()