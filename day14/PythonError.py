#Python Error

# SyntaxError

# PS C:\Users\pc\OneDrive\Desktop\python_code> python
# Python 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:03:56) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print 'hello world'
#   File "<stdin>", line 1
#     print 'hello world'
#     ^^^^^^^^^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?


# NameError

# >>> print(age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'age' is not defined

# lets fix
# >>> age = 22
# >>> print(age)
# 22
# >>> 


# IndexError


# >>> numbers = [1,2,3,4,5]
# >>> numbers[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>>

# In the example above, Python raised an IndexError, because the list has only indexes from 0 to 4 , so it was out of range.


# ModuleNotFoundError


# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'

# In the example above, I added an extra s to math deliberately and ModuleNotFoundError was raised. Lets fix it by removing the extra s from math.

# AttributeError

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

# KeyError

# >>> users = {'name':'Ashuu', 'age':20, 'country':'dubai'}  
# >>> usera['name']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'usera' is not defined. Did you mean: 'users'?
# >>> users['name']
# 'Ashuu'
# >>> users['county'] 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'county'
# >>>


# TypeError


# >>> 4 + '3'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>>


# lets fix

# In the example above, a TypeError is raised because we cannot add a number to a string. First solution would be to convert the string to int or float. Another solution would be converting the number to a string (the result then would be '43'). Let us follow the first fix.

# >>> 4 + int('3')
# 7
# >>> 4 + float('3')
# 7.0
# >>>


# ImportError


# >>> from math import power
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'power' from 'math' (unknown location)
# >>>


# There is no function called power in the math module, it goes with a different name: pow. Let's correct it:

# >>> from math import pow  
# >>> pow(2,3)
# 8.0


# ValueError

# >>> int('12a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '12a'


# In this case we cannot change the given string to a number, because of the 'a' letter in it.

# ZeroDivisionError

# >>> 1/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>>


# We cannot divide a number by zero.

