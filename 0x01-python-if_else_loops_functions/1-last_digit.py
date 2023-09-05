#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strnumber = str(number)
if int(strnumber) > 5:
    print("Last digit of", number, "is", strnumber[-1], "and is greater than 5")
elif int(strnumber) == 0:
    print("Last digit of", number, "is", strnumber[-1], "and is 0")
elif int(strnumber) < 6 and strnumber != 0:
    print("Last digit of", number, "is", strnumber[-1], "and is less than 6 and not 0")
