#!/usr/bin/python3
import sys
def safe_function(fct, *args):
"""this func executes a function safely
Args:
fct: function being executed
args: func arguments
Returns:
function results
Otherwise - none
"""
try:
result = fct(*args)
return (result)
except:
print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
return (None)
