



# Lesson 4 - Strings

## Recap 1: Sushi Checkout

# You just had a lunch at a sushi restaurant and have to
# calculate the total amount you have spent. Different coloured
# plates costs different as shown below:

# Red = $1
# Blue = $2
# Green = $3

# You have ordered a total of 3 red plates, 5 blue plates, and 4
# green plates.

# Calculate and print the total amount you have spent: -->



red = 1
blue = 2
green = 3
print( (green * 4) + (blue * 5) + (red * 3))

## Task 1: Storing and printing Strings

# **Task 1a**:
# Use the input() function to ask the user for their name and
# store it in a variable. Then print that variable.

# **Task 1b**:
# Ask the user for their favorite colour using input() and
# store the response in a variable. Print the variable.

# **Task 1c**:
# Ask the user for their age using input() and store the answer
# in a variable. Print the variable.




Name = input("What is your name?")
print(Name)

Colour = input("What is your favourite colour?")
print(Colour)

Age = input("What is your age?")
print(Age)


## Task 2: Input & string concatenation

# **Task 2a**:
# Ask the user for their name using input() and store it in a
# variable. 
# Concatenate the name with "Hi, [name]!" and print the
# complete message.

# **Task 2b**:
# Use input() to ask the user for their favorite hobby. Store this
# in a variable.
# Print a message saying "I enjoy [hobby]" using string
# concatenation.

# **Task 2c**:
# Ask the user for their dream vacation destination using input()
# and store it in a variable.
# Concatenate this variable with a phrase like "I would love to
# visit" and print the full sentence.




name = input("what is your name")
print("hi " + name + "!")

hobby = input("what is your hobby")
print("I enjoy " + hobby)

vacation = input("where is your dream vacation")
print("I would love to visit " + vacation)



# **Task 3a**:
# 1. Ask the user for their current age using input(). Convert this
# to an integer.
# 2. Add 1 to their age and convert it back to a string.
# 3. Then print a message saying "Next year, you will be [age+1]
# years old."

# **Task 3b**:
# 1. Use input() to ask the user for a number. Convert this number
# from a string to an integer.
# 2. Double the number and convert it back to a string.
# 3. Print "Double your number is [double the number]".

# **Task 3c**:
# 1. Use input() to ask the user for the year they were born and
# convert it to an integer.
# 2. Subtract the birth year from the current year (assume the
# current year as an integer) to find their age.
# 3. Convert the age back to a string and print "You are [age]
# years old".






birth_year = input("What year were you born? ")
birth_year = int(birth_year)  # Convert to integer
current_year = 2025  # Assume the current year is 2025
age = current_year - birth_year  # Calculate age
print("You are " + str(age) + " years old.")  # Convert to string and print

number = input("Enter a number: ")
number = int(number)  # Convert to integer
double_number = number * 2  # Double the number
print("Double your number is " + str(double_number))  # Convert to string and print



