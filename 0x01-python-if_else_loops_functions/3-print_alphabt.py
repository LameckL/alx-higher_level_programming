#!/usr/bin/python3
for alph in range(97, 123):
    if chr(alph) is not 'e' and chr(alph) is not 'q':
        print("{}".format(chr(alph)), end="")
