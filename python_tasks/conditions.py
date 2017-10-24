#!/usr/bin/python
"""
conditions.py

Solution of tasks concerning "if .. else" constructions.

Author:
Danila Iakovlev
"""

def main():
    print("1. Is 200 greater than 100 and less then 300? (By tho ways)")
    print("Logic: " + str(triple_comp_logic(100, 200, 300)))
    print("Chain: " + str(triple_comp_chain(100, 200, 300)))
    print("______\n")

    print("Now input a number: ")
    user_input = input()
    while not is_number(user_input):
        print("Error: you didn'n type a number, try again.")
        user_input = input()

    out = "\n2. Number " + user_input + " is "
    user_num = float(user_input)
    if more_than_10(user_num):
        out += "greater than 10."
    else:
        out += "less than 10."
    print(out)
    print("______\n")

    out = "3. Number " + str(int(user_num)) + " is "
    if is_even(int(user_num)):
        out += "even."
    else:
        out += "odd."
    print(out)
    print("______\n")


def triple_comp_chain(left, check, right):
    if check > left:
        if check < right:
            return True
    return False


def triple_comp_logic(left, check, right):
    if (left < check) and (check < right):
        return True
    return False


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def more_than_10(num):
    if num > 10:
        return True
    return False


def is_even(num):
    if num % 2 == 0:
        return True
    return False



if __name__ == '__main__':
    main()
