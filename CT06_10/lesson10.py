# Task 1: Positive or Negative Numbers
# Write a program that will let the user know if the number they
# have entered is positive or negative.

# 1. Ask the user to input a number
# 2. Using an 'if' statement, check if the number is greater than 0
#         If it is, print "{number} is positive."
# 3. Use an 'else' statement for when the number is not greater than 0.
#         In this case, print "{number} is negative."

# Bruh = int(input("Input a number"))
# if Bruh > 0:
#     print("Positive")
# else:
#     print("Negative")

# Task 2: Random Number Guesser III
# Create a Random Number Guesser program

# 1. Generate a random integer between 1 to 10
# 2. Ask the user to guess a number
# 3. If the user guesses correctly:
#     print "Congratulations!! You did it!"
# 4. If the user guesses wrongly: 
#     print "Oops, better luck next time!"

# import random
# bruh = random.randint(1,10)
# aah = int(input("guess from 1 to 10 "))
# if aah == bruh:
#     print("Congratulations you got it correct!")
# else:
#     print("Congratulations you got it wrong!")


# Task 3: Password Checker
# Code a password checker to protect your code!

# 1. Assign a password to a variable
# 2. Ask the user to enter a password
# 3. If the password matches, print "Login Successful"
# 4. If the password does not match, print "Password Incorrect"

# bruh = "bruhh"
# hehe = (input("What is my passwordi "))
# if hehe == bruh:
#     print("Congratulation you got bruhh")
# else:
#     print("Congratulations you got it wrong bruhh")

# Task 4: Even or Odd?
# Code a program to tell the user if a number is even or odd

# 1. Ask the user to input a number
# 2. Using the '%' operator, find out if a number is divisible by 2
#    (A number that is divisible by 2 will leave no remainder when
#    divided by 2)
# 3. If the number is even, print "This number is even"
# 4. If the number is odd, print "This number is odd"


# Num = int(input("number"))
# if Num % 2:
#     print("Its a odd number.")
# else:
#     print("Its an even number.")


# Task 5: Simple Age Checker (nested if..else)
# Using nested if..else condition, write a program that categorizes
# a person's age as 'Child', 'Teen', or 'Adult'.

# 1. Initialize an 'age' variable and ask user for their age.
# 2. Use an 'if' statement to check if the age is less than 13.
#         If true, print "Child"
# 3. Within the 'else' statement of the 1st 'if' statement, use
#    another 'if' statement to check if the age is between 13 and 19.
#         If true, print "Teen"
# 4. Else:
#         Print "Adult"

ez = int(input("GIVMME YUR AGE NOW"))
if ez < 13:
    print("Child")
else: # ez is definitely >= 13
    if ez < 20:
        print("Teenage bruhh guy")
    else:
        if ez < 21:
            print("minor")
        else:
            if ez < 60:
                print("adult")
            else:
                if ez > 60:
                    print("Old man bruhh")



ez = int(input("GIVMME YUR AGE NOW"))
if ez < 13:
    print("Child")
elif ez < 20:
    print("Teenage bruhh guy")
elif ez < 21:
    print("minor")
elif ez < 60:
    print("adult")
elif ez > 60:
    print("Old man bruhh")



# Task 6: Activity Advisor (nested if..else)
# Using nested 'if..else' statements, write a program that suggests
# an activity based on the temperature:
# 1. Suggest reading indoors if temperature is below 20 degrees
# 2. Suggest cycling if temperature is between 20 and 30 degrees
# 3. Suggest swimming if temperature is above 30 degrees

# 1. Initialize a 'temperature' variable and ask user for temperature
# 2. Use an 'if' statement to check if the temperature is below 20
#    degrees.
#         If true, print "Consider reading indoors."
# 3. Within the else statement of the 1st 'if' statement, use another
#    'if' statement to check if the temperature is between
#    20 and 30 degrees.
#         If true, print "It's a great day for cycling"
# 4. Else:
#         Print "How about a swimming session?"
tempbruh = int(input("What is the temperature outside bruhh")) 
if tempbruh < 21:
    print("AYO READ INDOORS NOW")
else:
    if tempbruh > 20:
        print("PLS go cycling NOW")
    else:
        if tempbruh > 29:
            print("Go swimming BRUHHHHHH")