#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
"""func dividing divides element by element 2 lists
Args:
my_list_1 (list): list 1
my_list_2 (list): list 2
list_length (int): no. of elements to divide
Returns:
 new list with all division
"""
new_list = []
for i in range(0, list_length):
try:
divide = my_list_1[i] / my_list_2[i]
except TypeError:
print("wrong type")
divide = 0
except ZeroDivisionError:
print("division by 0")
divide = 0
except IndexError:
print("out of range")
divide = 0
finally:
new_list.append(divide)
return (new_list)
