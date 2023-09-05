#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """this function prints numbers from 1 to 100 separated by a space
    For multiples of 3 print Fizz not  num, multiples of 5 print Buzz
    For numbers which are multiples of both three and five print FizzBuzz

    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(num), end="")
