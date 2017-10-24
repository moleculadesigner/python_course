"""
python_tasks/cycles.py

Solution of basic tasks concerning cycles.

Author:
Danila Iakovlev
"""
import math as m

def main():
    print("1. Sequence from 1 to 10")
    int_seq(10)
    print("______\n")

    print("2. Sequence of natural squares from 1 to 10")
    sqr_seq(10)
    print("______\n")

    print("3. Backward sequence from 133 to 112")
    backward_seq(133,112)
    print("______\n")
    
    print("4. Fibonacci's sequence, first 14 members.")
    fibonacci(1,0,14)
    print("______\n")

    print("5, 6. Geometric progression")
    burst(1,2,15)
    print("______\n")


def int_seq(lim):
    """
    Returns natural numbers up to lim.
    """

    out_seq_str = "For:\t"
    for i in range(lim):
        out_seq_str += (str(i + 1))
        if (i + 1) != lim:
            out_seq_str += ", "
       
    print(out_seq_str)

    out_seq_str = "While:\t"
    i = 0
    while i < lim:
        i += 1
        out_seq_str += str(i)
        if i != lim:
            out_seq_str += ", "

    print(out_seq_str)
  

def sqr_seq(lim):
    """
    Prints sequence of natural squares up to lim.
    """

    out_seq_str = "For:\t"
    for i in range(1,lim + 1,1):
        out_seq_str += str(pow(i,2))
        if i < lim:
            out_seq_str += ", "
    print(out_seq_str)

    out_seq_str = "While:\t"
    i = 0
    while i < lim:
        i += 1
        out_seq_str += str(i*i)
        if i < lim:
            out_seq_str += ", "
    print(out_seq_str)


def backward_seq(max_num,min_num):
    """
    Prints backward cequence from max_num to min_num.
    """
    if max_num <= min_num:
        print("Exception: invalid range.")
        return "Exception: invalid range."

    out_seq_str = "For:\t"
    for i in range(max_num,min_num - 1,-1):
        out_seq_str += str(i)
        if i > min_num:
            out_seq_str += ", "
    print(out_seq_str)

    out_seq_str = "While:\t"
    j = max_num
    while j >= min_num:
        out_seq_str += str(j)
        if j > min_num:
            out_seq_str += ", "
        j -= 1
    print(out_seq_str)


def fibonacci(base_1, base_2, length):
    """
    Returns Fibonacci's sequence up to length'th member.
    """

    if length < 3:
        print("Error: sequence is too short (<3), it's useless!")
        return "Error: too short sequence."
    if base_1 != base_2:
        l_num = min(base_1,base_2)
        g_num = max(base_1,base_2)
    else:
        l_num = base_1
        g_num = base_1

    swap = 0
    out_seq_str = "Fibonacci: " + str(l_num) + ", " + str(g_num) + ", "
    for i in range(3, length + 1):
        swap = g_num
        g_num += l_num
        l_num = swap
        out_seq_str += str(g_num)
        if i < length:
            out_seq_str += ", "

    print(out_seq_str)


def burst(base, step, length):
    """
    Prints geometric progression and its sum
    """

    if length < 2:
        print("Error: invalid length!")
        return "Error: invalid length"
    
    burst_sum = base
    out_seq_str = "Geometric burst: " + str(base) + ", "
    while length > 1:
        base *= step
        burst_sum += base
        out_seq_str += str(base)
        if length > 2:
            out_seq_str += ", "
        length -= 1

    out_seq_str += ("\n            Sum: " + str(burst_sum))
    print(out_seq_str)
    


if __name__ == '__main__':
    main()
