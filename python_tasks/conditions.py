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

    print("4. (0 if -1 < 0 else 1) + 1 is " + str((0 if -1 < 0 else 1) + 1))
    print("   (0 if  1 < 0 else 1) + 1 is " + str((0 if 1 < 0 else 1) + 1))
    print("______\n")

    print("5. Nick bought some pies, how much do you think?")
    user_input = input()
    while not is_integer(user_input):
        print("Error: you didn'n type an integer, try again.")
        user_input = input()
    nick_pies = int(user_input)
    print("And Vania has 100.")
    if nick_pies + 100 >= 150:
        print("Condition 1 (all pies >= 150) is matched.")
    if 200 < nick_pies + 100 < 300:
        print("Condition 2 (200 < all < 300) is matched.")
    print("______\n")

    print("6. Now print an integer from 1 to 5:")
    while True:
        user_input = input()
        if is_integer(user_input):
            if int(user_input) == 1:
                print("You entered number 'One'.")
                break
            elif int(user_input) == 2:
                print("You entered number 'Two'.")
                break
            elif int(user_input) == 3:
                print("You entered number 'Three'.")
                break
            elif int(user_input) == 4:
                print("You entered number 'Four'.")
                break
            elif int(user_input) == 5:
                print("You entered number 'Five'.")
                break
            else:
                print("I don't know this number. Try from 1 to 5.")
        else:
            print("Error: you didn'n type an integer, try again.")
    print("______\n")

    print("7. Tables")
    print("AND:\nx\ty\tx and y")
    for x in range(2):
        for y in range(2):
            print(str(bool(x)) + "\t" + str(bool(y)) + "\t" + str(bool(x) and bool(y)))
    print("\nOR:\nx\ty\tx or y")
    for x in range(2):
        for y in range(2):
            print(str(bool(x)) + "\t" + str(bool(y)) + "\t" + str(bool(x) or bool(y)))
    print("\nAND NOT:\nx\ty\tx and not y")
    for x in range(2):
        for y in range(2):
            print(str(bool(x)) + "\t" + str(bool(y)) + "\t" + str(bool(x) and not bool(y)))
    print("\n(x OR z) AND (y OR z):\nx\ty\tz\t(x or z) and (y or z)")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(str(bool(x)) + "\t" + str(bool(y)) + "\t" + str(bool(z)) + "\t" + str((bool(x) or bool(z)) and (bool(y) or bool(z))))
    print("______\n")

    print("8. And now an endless loop:\nwhile True:\n\tx = 0\nTo abort press Ctrl+C")
    while True:
        x = 0


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


def is_integer(s):
    try:
        int(s)
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
