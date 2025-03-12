# Lesson 8 - Importing Libraries, Boolean & Conditions

## Recap 1: Product of 5 numbers

# Write a program to calculate the product (multiplication) of 5
# numbers.

# 1. Using a for loop, ask the user for 5 numbers one at a time.
# 2. Calculate the multiplication for these 5 numbers and print it out.


# Product = 1 # accumulator variable
# for i in range(1 , 6):
#     Product = Product * int(input("What is number " + str(i) + " ? "))
# print("Product of the 5 numbers is " , Product)





# Task 1: 'time' library

# **Task 1a**:
# Import the 'time' library and make use of the 'time.sleep()'
# function to create a 10 seconds countdown timer that counts
# to 1, printing the number of seconds remaining every second.

# **Task 1b**:
# Modify your code from Task 1a to include an 'input()' function
# asking the user for the number to countdown from, before
# counting down every second from the number given by the user.

# import time

# # range(stop)
# # range(start, stop)
# # range(start, stop, step)
# bruh = int(input("number to count down from "))
# for i in range(bruh,0, -1):
#     time.sleep(1)
#     print(i)




## Task 2: 'random' library

# **Task 2a**:
# Import the 'random' library and create a program that randomly
# output a number between 1 to 6

# **Task 2b**:
# Using the 'random' library, create 20 numbers between 0 and
# 9999 randomly.

import random
bruhh = random.randint(68)
print(bruhh)