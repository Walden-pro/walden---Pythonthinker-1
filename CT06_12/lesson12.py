# Lesson 12 - While Loops

# Recap 1: Multiples of 3 and 5
# Create a program to check if a number is both divisible by 3
# and 5.

# 1. Ask the user to input a number
# 2. Using the '%' operator, check if the number is both a
#    multiple of 3 and 5:
#     If true, print "The number is divisible by 3 and 5!"
# 3. Else, print "The number is not divisible by 3 and 5"



# bruh = int(input("What is the number?"))
# if bruh % 3 == 0 and bruh % 5 == 0:
#     print("The number is divisible by 3 and 5!")
# else:
#     print("The number is not divisible by 3 and 5!")


# Task 1: Introduction to while loop
# **Task 1a**:
# Due to a pandemic, the government placed a limit to the number
# of visitors a venue can have.

# Using a 'while' loop, create a program that will increase the
# number of visitors by 1 before printing out the number of
# visitors admitted, until number of visitors reaches 50.

# 1. Create a 'visitors' variable and assign '0' to it
# 2. While there is less than 50 visitors,
#     I. Increase the visitor count by 1
#     II. Print the visitor count

# (For Task 1b & 1c)
# Modify your program to account for the number of visitors
# already present at the venue, and the number of maximum visitors
# allowed for the following:

# **Task 1b**:
# Visitors already present: 18
# Max visitors allowed: 30

# **Task 1c**:
# Visitors already present: 4
# Max visitors allowed: 25



# gyat = 0
# while gyat < 50:
#     gyat += 1
#     print("Number of visitors admitted:", gyat)

# visitors = 18
# mvs = 30
# while visitors < mvs:
#     visitors += 1
#     print("Number of visitors admitted:", visitors)

# visitors = 4
# max_visitors = 25
# while visitors < max_visitors:
#     visitors += 1
#     print("Number of visitors admitted:", visitors)



# Task 2: while... break
# A restaurant used to have a max capacity of 50. However, due to
# the worsening of the pandemic, the government has restricted the
# max capacity of the restaurant to 30.

# Using an 'if' condition and 'break' within the 'while' loop,
# modify your answer for Task 1a to terminate the 'while' loop when
# number of visitors is 30.


# gyat = 0
# while gyat < 50:
#     gyat += 1
#     if gyat == 30:
#         break


# Task 3: Order taking using while loop
# Using what you have learnt so far, code a program to take a
# customer's order.

# Declare a variable called 'order' and assign an empty string
# variable "" to it.

# Using a 'while' loop:
# 1. Ask the user to enter their order
# 2. For each order entered, concatenate to the 'order' variable.
# 3. Exit the 'while' loop if the user enters "end"
# 4. On program end, print out the customer's order.

# **Bonus**
# 1. Modify your code to remove the comma (",") that appears
#    either at the start or end of your sentence

# order = ""
# while True:
#     oi = input("What is your order? ")
#     if oi == "end":
#         break
#     order += oi + ", "
# print("Your order is: " + order[0:-2])



# Task 5: Math Question
# **Task 5a**:
# Create a program to test the user on their math skills! The
# program will continue generating new questions until the user
# get the correct answer.

# 1. Using a 'while' loop, 
# 2. Generate 2 random numbers between 1 and 10 (import 'random'
#    and use 'random.randint()')
# 3. Ask the user to add the 2 numbers together in the following
#    format:
#     "What is 3 + 5?"
# 4. If the user gets the correct answer:
#     Print "That's correct!
# 5. Else:
#     print "Wrong! Try again"
#     End the 'while' loop
    
# **Bonus**
# Some ideas to improve on the above program:
# 1. Print the user's score once the game is over
# 2. Randomly choose an operator for each question: + - *

# **Task 5b**:
# Modify your answer from Task 5a to keep asking a new
# question until the user get 5 correct answers.

# **Bonus**
# Some ideas to improve on the above program:
# 1. Add a score system (+2 for right answer, -1 for wrong answer)
# 2. Add an ability for users to skip by saying "skip"
# 3. Disqualify user when they have gotten the wrong answer or
#    skipped more than 5 times


# while True:
#     import random
#     num1 = random.randint(1,10)
#     num2 = random.randint(1,10)
#     bruhh = input("What is " + str(num1) + " + " + str(num2) + "? ")
#     if bruhh == str(num1 + num2):
#         print("Correct!")
#     else:
#         print("WRONG!")
#         break







# Task 6: Dice Roll till 4
# Using 'while' loop and the 'random.randint()' function from the
# 'random' library, constantly print a random number between 1 and
# 6 until the random number generated is 4.

# 1. Import the 'random' library
# 2. Create 'num' variable and assign it '0'
# 3. While 'num' variable is not '4',
#     a. Using 'random.randint()', assign 'num' variable a random
#        number between 1 and 6.
#     b. Print the random number generated.

# **Bonus**
# Some ideas to improve on the above program:
# 1. Add a counter variable and announce the number of tries it
#    took before rolling a '4'.
# 2. Add the ability for the user to determine which number to roll
#    until (instead of '4' all the time).
# 3. Break out of the 'while' loop if counter variable reaches 10
#    and print "You have won the jackpot!"


# import random
# num = 0
# counter = 0
# while num != 4 and counter < 10:
#     num = random.randint(1, 6)
#     print(num)
#     counter += 1
#     if num == 4:
#         print("You rolled 4!!")
#     elif counter == 10:
#         print("Bruhhhhhhhhhhh aaaaaaaauuuuuuggggggggghhhhhhhhhhhh You won the jacketpot!")

