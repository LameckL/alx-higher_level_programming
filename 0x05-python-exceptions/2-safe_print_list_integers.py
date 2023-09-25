#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
  """func printing first x elements of a list and only integers
  Args:
    my_list (list): list to print elements from
    x (int): The number of elements of my_list to print
  Returns:
    no. of elements printed
  """
  el = 0
  for i in range(0, x):
    try:
      print("{:d}".format(my_list[i]), end="")
      el += 1
    except (ValueError, TypeError):
      continue
  print("")
  return (el)
