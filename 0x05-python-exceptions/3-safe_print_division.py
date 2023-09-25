#!/usr/bin/python3
def safe_print_division(a, b):
"""func dividing 2 integers and prints the result
Returns: value of division"""
try:
divide = a / b
except (TypeError, ZeroDivisionError):
divide = None
finally:
print("Inside result: {}".format(divide))
return (divide)
