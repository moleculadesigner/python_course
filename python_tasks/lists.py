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
    """

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

if __name__ == '__main__':
    main()