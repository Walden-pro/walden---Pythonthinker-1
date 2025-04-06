# Lesson 11 - AND OR NOT

# Recap 1: Purchase Advisor
# Create a program that asks the user for the price of an item (px) and
# gives a comment based on the price:

# if:
#     px <= 5: "Sounds good!"
#     px <= 50: "Are you sure you need this?"
#     px <= 500: "Where are you getting this money from?!"
#     px > 500: "Don't even think about it!"
 
# px = int(input("The price of the item: $"))
# if px <= 5:
#         print("Sounds good!")
# elif px <= 50:
#     print("Are you sure you need this?")
# elif px <= 500:
#     print("Where are you getting this money from?!")
# else:
#     print("Don't even think about it!")



# Task 1: AND Operator in Simple Conditions (AND)
# You are writing a program for an amusement park that needs to check
# if both riders of a ride are above the height of 120cm. Use the 'and'
# operator to determine if value of both 'rider1' and 'rider2' are
# greater than 120.

# 'rider1' = 125
# 'rider2' = 150
# rider1 = 125
# rider2 = 150

# result = rider1 > 120 and rider2 > 120
# print(result)


# Task 2: Multiples of 3 and 7 (AND)
# Create a program to check if a number is both divisible by 3 and 7

# 1. Ask the user to input a number
# 2. If the number is both a multiple of 3 and a multiple of 7:
#     print "The number is divisible by 3 and 7!"

# number = int(input("What is the number?"))
# if number % 3 == 0 and number % 7 == 0:
#     print("The number can be divided by 3 and 7.")

# Task 3: Identity Identifier (AND)
# Create a program that asks for user's first and last name and checks
# if it matches "James" and "Leong" respectively and print "YOU ARE
# WANTED" if true.

# Fn = (input("First name "))
# ln = (input("Last name "))
# if Fn == "James" and ln == "Leong":
#     print("YOU ARE WANTED")



# Task 4: 'or' Operator in Conditional Statements (OR)
# You run a go-kart business and need a program to check if at least
# 1 occupant of a 2-person go-kart is at least 18 years old.

# Use the 'or' operator to determine if value of either 'rider1' or
# 'rider2' is equal to or greater than 18.

# 'rider1' = 25
# 'rider2' = 6

# rider1 = 25
# rider2 = 6
# if rider1 >= 18 or rider2 >= 18:
#     print("You can ride!")



# Task 5: Ticket Pricing Machine (OR)
# Create a program that will decide on the price of a ticket based on
# user's age. Original ticket price costs $20 per person. However,
# children below the age of 12 and elderly above the age of 65 can buy
# the ticket for just $15.

# 1. Ask user for their age
# 2. Use the 'or' operator to determine if user's age is less than 12 or
#    more than 65. If true, print "Ticket price: $15"
# 3. Else, print "Ticket price: $20"

age = int(input("What is your age?"))
if age > 65 or age < 12:
    print("Ticket price: $15")
else:
    print("Ticket price: $20")



# Task 6: Input Validator (OR)
# Using the 'or' operator, create a program that prints "Valid Input"
# if the user has entered "M" or "Male" as an input. Or else, print
# "Invalid Input" instead

# 1. Ask user for input
# 2. If user input is "M" OR "Male", print "Valid Input"
# 3. Else, print "Invalid Input"


Gender = (input("input")) # dont need to convert to string. by default, input gives string
if Gender == "M" or Gender == "Male":
    print("Valid Input")
else:
    print("Invalid Input")


# Task 7: Colour filter (NOT)
# Create a program that will ask the user for a colour and print
# "Try again" if the input of the user is not "Green".

# 1. Ask user for a colour
# 2. Using the 'not' operator, check if input is not "Green".
#    If true, print "Try again"

colour = input("What is the colour??")
