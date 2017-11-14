"""
1. Создайте список числовых значений от 0 до 100 (через циклы и генераторы)
2. Создайте список квадратов элементов предыдущего списка (через циклы и генераторы)
3. Создайте список, состоящий из четных элементов предыдущего списка (через циклы и генераторы)
4. Вот строка 'rewlkdfsklgjdflkjglkdsfjgkldfsjglkjeroitewuiotujdigjsdfklg;klsdfgkl;jsdfkl;gjldk;sfjgjlk;sdfjlk;gjsdfl;kgl;kdsfjgl;kjsdfl;kgjl;sdfkjg;lkjsdflbvjdfslkglkrewjhtiowerjutioerutopiytuilyhjdsfl;kghjl;sdkf;gjdffffffffflkgjlkdfjglkasjdfoitweigheripjgierglisjdfkjlghsdfkj;l;hgkljasdhfglk;hsdfkjlghlk;sdfhg;kljsdflkgjlk;sdfjgl;ksdfjl;kgjsdfl;kjglk;sdfjgkjsdfl;kgjs;dlkfjgoiw3eujtio34wuytiergoijherjhlgjsdflkjgkl;dfjgkl;sdfjkl;gjsdf;lkjg;lsjeriotuerl;kjdsfkl;jgh;lksdfjg;lksdfjg;lksdfkjg;lkjreopyulidsjfl;kghjs;ldkjg;lkkjr5l;h;kljyhkl;rirtiririiiiiiiiiiiiiierwtsj;kldfjg;lksdfjgl;ksdjfl;gj;lsdfjg;lk' - удалите из нее все повторяющиеся буквы и выведете строку уникальных букв
5. Какая буквенная подпоследовательность одинаковых символов самая длинная
6. Напишите функцию которая будет удалять заданную букву из строки и протестируйте ее на вышеприведенной строчке 
6. Вот список чисел - 2,3,3,45,4,23,43,54,34,5,32,423,4,23542354,3422,243,4,3,3,254,5643,3233,3,3,4,43,2,423,3,3,45,5,43,2,1,4,34234,34,3,342,23,4543,534,32423,23,4,4,4,3,423,3245,23,3,34254,235,234,5,235,4,345,235,23,5523,5,234,52,67,756,76,57,345,23,31,7,8,56,346,345,756,4343,754,674,8,568,9,65,34,3,5474,5687,56,2,3 - вычислите сумму этой последовательности
7. Найдите наибольший/наименьший элемент предыдущего списка
8. Отсортируйте предыдущий список
9. Напишите программу, которая спрашивает е пользователя как много чисел Фибоначчи нужно сгенерировать а затем генерирует их
10. сгенерируйте матрицу как список списков (через циклы и генераторы)
11. Напишите функцию транспонирования матрицы
12. Напишите функцию сложения матриц
13. Напишите функцию умножения матриц
14. Напишите функцию решения системы линейных уравнений методом Гаусса. Коэффициента уравнения задаются матрицей вектор неизвестных - вектором соответственно. [метод Гаусса и как его запрогать можно найти здесь](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%93%D0%B0%D1%83%D1%81%D1%81%D0%B0) (можно не делать если кажется слишком сложным)
"""
import math
import string
import random as r

import conditions_and_cycles as cas

_example_string = 'rewlkdfsklgjdflkjglkdsfjgkldfsjglkjeroitewuiotujdigjsdfklg;klsdfgkl;jsdfkl;gjldk;sfjgjlk;sdfjlk;gjsdfl;kgl;kdsfjgl;kjsdfl;kgjl;sdfkjg;lkjsdflbvjdfslkglkrewjhtiowerjutioerutopiytuilyhjdsfl;kghjl;sdkf;gjdffffffffflkgjlkdfjglkasjdfoitweigheripjgierglisjdfkjlghsdfkj;l;hgkljasdhfglk;hsdfkjlghlk;sdfhg;kljsdflkgjlk;sdfjgl;ksdfjl;kgjsdfl;kjglk;sdfjgkjsdfl;kgjs;dlkfjgoiw3eujtio34wuytiergoijherjhlgjsdflkjgkl;dfjgkl;sdfjkl;gjsdf;lkjg;lsjeriotuerl;kjdsfkl;jgh;lksdfjg;lksdfjg;lksdfkjg;lkjreopyulidsjfl;kghjs;ldkjg;lkkjr5l;h;kljyhkl;rirtiririiiiiiiiiiiiiierwtsj;kldfjg;lksdfjgl;ksdjfl;gj;lsdfjg;lk'
_example_list = [2,3,3,45,4,23,43,54,34,5,32,423,4,23542354,3422,243,4,3,3,254,5643,3233,3,3,4,43,2,423,3,3,45,5,43,2,1,4,34234,34,3,342,23,4543,534,32423,23,4,4,4,3,423,3245,23,3,34254,235,234,5,235,4,345,235,23,5523,5,234,52,67,756,76,57,345,23,31,7,8,56,346,345,756,4343,754,674,8,568,9,65,34,3,5474,5687,56,2,3]


def main():
    """
    print("1. List from 1 to 100:")
    one_to_hundred = [i for i in range(1,101)]
    print(cas.list_to_str(one_to_hundred, '\t', 0, 1, 10) + '\b')
    print("______\n")

    print("2. List of squares:")
    sqr_to_hundred = [i**2 for i in one_to_hundred]
    print(cas.list_to_str(sqr_to_hundred, '\t', 0, 1, 10) + '\b')
    print("______\n")

    print("3. Even elements of previous list:")
    evn_to_hundred = [sqr_to_hundred[i] for i in range(1, len(sqr_to_hundred), 2)]
    print(cas.list_to_str(evn_to_hundred, '\t', 0, 1, 10))
    print("______\n")

    print("4. Unique symbols in string:")
    u_sym = get_unique_symbols(_example_string)
    print(u_sym)
    print("______\n")

    print("5. The longest sequence of same symbols is:")
    mfs = longest_seq(_example_string)
    print(mfs + " - " + str(len(mfs)) + " symbols.")
    print("______\n")


    print("6. Char remover")
    masked_string = mask(_example_string, 'r')#ewlkdfsgjoitu;bvhpya345')
    print(masked_string)

    print("7. Sum of elements in list:")
    lsum = 0
    for i in _example_list:
        lsum += i
    print(str(lsum))
    print("______\n")

    print("8. Minimum and maximum:")
    example_list_sorted = sorted(_example_list)
    print(str(example_list_sorted[0]) + ', ' + str(example_list_sorted[-1]))
    print("\n9. Sorted list:")
    print(cas.list_to_str(example_list_sorted, '\t', 0, 1, 12))
    print("______\n")

    print("10. How many Fibonacci number do you want?")
    n_fib = cas.get_int()
    print(cas.list_to_str(fibonacci_list(n_fib), '\t', 0, 1, 12))
    print("______\n")

    m = matrix_gen()
    k = matrix_gen()
    l = matrix_gen()
    print("11. Matrix:\n" + matrix_str(m) + '\n')
    print("12. Transposed:\n" + matrix_str(matrix_transpose(m)) + '\n')
    print("13. Sum:\n" + matrix_str(k) + "\n    +    \n" + matrix_str(l) + "\n    =    \n" + matrix_str(matrix_sum(k, l)) + '\n')
    print("14. And product:")
    print(matrix_str(k) + "\n    x    \n" + matrix_str(matrix_transpose(l)) + "\n    =    \n" + matrix_str(matrix_multi(k, matrix_transpose(l)), '\t'))
    """

    les = matrix_gen(6, 5)
    print(matrix_str(les, "\t") + '\n') 

    sel = gauss(les)
    print(matrix_str(les, "\t") + '\n') 
    print(cas.list_to_str(list(map(lambda x: round(x, 3), sel)), '\n'))







def get_unique_symbols(string):
    """
    Returns list of unique symbols found in input `string` as a string
    """
    unique_sym = ""
    for char in _example_string:
        if not (unique_sym.find(char) + 1):
            unique_sym += char
    return unique_sym


def longest_seq(string):
    """
    Return string of the longest sequence of equivalent symbols in `string`.
    """
    longest_seq = ""
    seq = ""
    pred_char = ''
    for succ_char in string:
        if succ_char != pred_char:
            if len(longest_seq) <= len(seq):
                longest_seq = seq
            seq = succ_char
        else:
            seq += succ_char
        pred_char = succ_char
    return longest_seq


def mask(string, charset):
    """
    Iteratively removes all symbols in `charset` from `string`.
    """
    result = ""
    if len(charset) < 1:
        result = string
    elif len(charset) == 1:
        for char in string:
            if char != charset:
                result += char
    else:
        result = mask(mask(string, charset[0]), charset[1:])
    print('. ' + result + '\n')
    return result


def fibonacci_list(n_max = 15):
    """
    Returns list of Fibonacci numbers.
    """
    if n_max < 1:
        return [0]
    fiblist = [0, 1]
    for i in range(2, n_max + 1):
        fiblist.append(fiblist[i - 2] + fiblist[i - 1])
    return fiblist


def matrix_gen(rows = 4, cols = 5, lim = 9):
    matrix = []
    for i in range(rows):
        matrix.append([r.randint(0, lim) for j in range(cols)])
    return matrix


def matrix_str(matrix, sep = ' '):
    line = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            line += str(round(matrix[i][j], 2)) + sep
        line += '\b\n'
    return line + '\b'


def matrix_transpose(matrix):
    if not len(matrix):
        return []
    if not len(matrix[0]):
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    t_matrix = []

    for j in range(cols):
        t_matrix.append([matrix[i][j] for i in range(rows)])

    return t_matrix


def matrix_sum(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError
        
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            matrix1[i][j] += matrix2[i][j]
    return matrix1


def matrix_multi(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError
        

    rows = len(matrix1)
    cols = len(matrix2[0])
    run  = len(matrix1[0])
    multi_matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            mm_ij = 0
            for r in range(run):
                mm_ij += matrix1[i][r] * matrix2[r][j]
                #print(str(mm_ij))
            row.append(mm_ij)
        multi_matrix.append(row)
    return multi_matrix


def gauss(matrix):
    """
    coefficients of system of linear equations are stored in `matrix`. *E. g.* for equation

    a11x + a12y + a13z = b1

    a21x + a22y + a23z = b2
    
    the `matrix` must be be:
    
    a11  a12  a13  b1

    a21  a22  a23  b2
    """
    if not len(matrix) or not len(matrix[0]):
        print("Gauss:> an argument recieved is not a matrix!")
        raise ValueError
    #print("Gauss:> solving:\n" + matrix_str(matrix) + '\n')
    n_vars = len(matrix[0]) - 1
    n_rows = len(matrix)
    tr_matrix = matrix_sort(matrix.copy())
    #print("Gauss:> sorted:\n" + matrix_str(tr_matrix) + '\n')
 
    for i in range(n_rows - 1):
        zeroes = 0
        for j in range(n_vars):
            if tr_matrix[i][j] == 0:
                zeroes += 1
            else:
                break
        
        for ii in range(i + 1, n_rows):
            if tr_matrix[ii][zeroes] == 0:
                break
            else:
                c = tr_matrix[ii][zeroes] / tr_matrix[i][zeroes]
            for j in range(zeroes, n_vars + 1):
                tr_matrix[ii][j] -= tr_matrix[i][j] * c
    
    if n_vars > n_rows:
        pass
    elif n_vars < n_rows:
        tr_matrix = tr_matrix[:n_vars]
        n_rows = n_vars
    sol_v = [0 for i in range(n_vars)]
    sol_v[n_vars - 1] = tr_matrix[n_rows - 1][n_vars] / tr_matrix[n_rows - 1][n_vars - 1]
    for i in range(n_vars - 2, -1, -1):
        c = tr_matrix[i][i]
        if c == 0:
            continue
        s = tr_matrix[i][n_vars]
        for j in range(i + 1, n_vars):
            s -= tr_matrix[i][j] * sol_v[j]
        sol_v[i] = s / c

    return sol_v
                

def matrix_sort(matrix):
    """
    rearranges matrix rows:

    0 1 2 0

    1 0 0 1

    to 

    1 0 0 1

    0 1 2 0
    """
    s_matrix = matrix
    swapped = True
    #print("raw:\n" + matrix_str(s_matrix))
    while swapped:
        swapped = False
        for i in range(len(s_matrix) - 1):
            #print('\ni = ' + str(i))
            n_up = 0
            n_dn = 0
            for j in range(len(s_matrix[0])):
                if s_matrix[i][j] == 0:
                    n_up += 1
                else:
                    break
            for j in range(len(s_matrix[0])):
                if s_matrix[i + 1][j] == 0:
                    #print(str(s_matrix[i + 1][j]))
                    n_dn += 1
                else:
                    break
            #print("; " + str(n_up) + " : " + str(n_dn))
            #print(str(s_matrix[i]) + " : " + str(s_matrix[i + 1]))
            if n_up > n_dn:
                swap_line = s_matrix[i]
                s_matrix[i] = matrix[i + 1]
                s_matrix[i + 1] = swap_line
                swapped = True
                #print("\nswap:\n" + matrix_str(s_matrix))
                continue
    else:
        return s_matrix
            




if __name__ == '__main__':
    main()