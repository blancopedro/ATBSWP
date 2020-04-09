# Ch 03 Practice Questions

# 1) Why are functions advantageous to have in your programs?
# A function is a like a program that you can built in order to solve your own problems.

# 2) When does the code in a function execute: when the function is defined or when the function is call?
# The function is execute when the function is call. We can define our function but not call it

# 3) What statement creates a function?
# def. For example def hello():

# 4) What is the difference between a function and a function call?
# A function is a block of code that perform some calculation and return something. Instead, a function call invoke or call (sorry for the repetition) the block of code we define before.

# 5) How many global scopes are there in a Python program? How many local scopes?


# 6) What happens to variable in a local scope when the function call returns?
# The local variable is destroyed and there is no longer a variable

# 7) What is a return value? Can a return value be part of an expression?
#  Return is used to end the execution and return the value to the caller. For example:

# 8) If a functions does not have a return statement, what is the return value of a call to that function?
# Return nothing, the return value will be None.


# 9) How can you force a variable in a function to refer to the global variable?
# With the global statement. Form example
"""
x = "Pedro"
def name():
    global x
    print("Mi nombre es " + x)
"""

# 10) What is the data type of None?
# NoneType. Is a value without a value


# 11) What does the import areallyourpetsnamederic statement do?
# Is the name of a module. With it you can use functions from other modules

# 12) If you had a function named bacon() in a module named spam, how would yo ucall it after importing spam?
# We need to use spam.bacon()

# 13) How can you prevent a program from chashing when it gets and error?
# Using the try and except code. For example
# def spam(divideBy):
#   return 10 / divideBy
# try:
#   print(spam(0)
# except ZeroDivisionError:
#   print("Error: Invalid argument.")
#
#

# 14) What goes in the try clause? What goes in the except clause?
# When try result in an error the program will goes to except in order to return it
