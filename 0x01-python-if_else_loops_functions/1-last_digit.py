#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = int(str(number)[-1])
if int(lastd) > 5:
    print("Last digit of", number, "is", lastd, "and is greater than 5")
elif int(lastd) == 0:
    print("Last digit of", number, "is", lastd, "and is 0")
elif int(lastd) < 6 and lastd != 0:
    print("Last digit of", number, "is", lastd, "and is less than 6 and not 0")
