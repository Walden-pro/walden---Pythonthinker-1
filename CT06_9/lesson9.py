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

# days_borrowed = int(input("number of days the book has been borrowed"))
# if days_borrowed > 25:
#     print("remember to return your book")

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

# import random

# number = random.randint(1,10)
# user_guess = int(input("Guess the number between 1 and 10 "))

# if user_guess == number:
#     print("Thats the magic number")


# Task 5: Fruits Shop
# **Task 5a**:
# Draw out the flowchart (on a piece of paper) of a program for
# the fruit shop, "FruitiFresh". FruitiFresh sells 2 fruits,
# Apple & Orange with the following pricing scheme:

# Apple:
# 1 Apple = 60 cents
# If buy more than 5 apples, get 10% discount for all apples

# Orange:
# 1 Orange = 90 cents
# If buy more than 5 oranges, get 10% discount for all oranges

# You want to create a program that:
# 1. Asks the user for the number of apples and oranges they
#    want to buy.
# 2. Print total price of the fruits

# **Task 5b**:
# Translate the flowchart that you have drawn (shown on screen)
# into Python code.

apple_price = 0.60
orange_price = 0.90

apples = int(input("number of apples you want to buy "))
oranges = int(input("number of oranges you want to buy "))

if apples > 5:
    apple_price *= 0.9

if oranges > 5:
    orange_price *= 0.9

total_price = (apples * apple_price) + (oranges * orange_price)
print("$" , total_price)