# Lesson 9 - If Statements

# Recap 1: Dice Roll Simulator
# Generate and print 3 random numbers between 1 and 6, followed
# by an output of 'True' if all 3 numbers are either even or odd.

# Example:
# 1st number: 6
# 2nd number: 4
# 3rd number: 6
# All numbers are even/odd: True

# 1. Import the 'random' library
# 2. Create 3 variables to hold a random number that is between
#    1 and 6, generated using 'random.randint()'
# 3. Using string concatenation, print the generated number for
#    each of the 3 numbers
# 4. Using the '%' and '==' operator, check if each number is
#    divisible by 2 (remainder = 0)
# 5. Using multiple '==' operators, a new variable 'all_even_odd'
#    should be assigned 'True' if all 3 numbers are either all
#    even or all odd numbers.
# 6. Print if "All numbers are even/odd" is 'True' or 'False'

# import random

# num1 = random.randint(1, 6)
# num2 = random.randint(1, 6)
# num3 = random.randint(1, 6)

# print("number 1 is" +(str(num1)))
# print("number 2 is" +(str(num2)))
# print("number 3 is" +(str(num3)))

# isEven = num1 % 2 == 0
# isEven2 = num2 % 2 == 0
# isEven3 = num3 % 2 == 0 

# all_even_odd = isEven == isEven2 == isEven3
# print("All numbers are even or odd " ,all_even_odd)



# Task 1: Flowchart for Library Reminder
# Draw out the flowchart (on a piece of paper) of a program
# to remind borrowers to return their books

# 1. Ask the user to input the number of days a book has been borrowed
# 2. If the book has been borrowed for more than 25 days:
#     print "Remember to return your book!"

days_borrowed = int(input("number of days the book has been borrowed"))
if days_borrowed > 25:
    print("remember to return your book")

# Task 3: Random Number Guesser I
# **Task 3a**:
# Draw out the flowchart (on a piece of paper) of a program for
# the user to guess a magic number:

# 1. Generate a random integer between 1 to 10
# 2. Ask the user to guess a number
# 3. If the user guesses correctly:
#     print "That's the magic number!"

# **Task 3b**:
# Translate the flowchart that you have drawn (shown on screen)
# into Python code.