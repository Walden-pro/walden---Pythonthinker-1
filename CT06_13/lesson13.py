


# Task 1: List of groceries
# **Task 1a**:
# Create a list of 8 groceries you need to buy:
# 1. Apples
# 2. Bread
# 3. Carrots
# 4. Dates
# 5. Eggs
# 6. Flour
# 7. Grapes
# 8. Honey

# **Task 1b**:
# You have decided to get "Herbs" instead of "Honey".
# Rename "Honey" to "Herbs"

# **Task 1c**:
# 1. You have just ran out of Ice. Add "Ice" into the list.
# 2. Insert "Bananas" between "Apples" and "Bread".

# **Task 1d**:
# You no longer want any bread. Delete "Bread" from the list.


# Task 1: List of groceries
# **Task 1a**:
# Create a list of 8 groceries you need to buy:
# 1. Apples
# 2. Bread
# 3. Carrots
# 4. Dates
# 5. Eggs
# 6. Flour
# 7. Grapes
# 8. Honey

# **Task 1b**:
# You have decided to get "Herbs" instead of "Honey".
# Rename "Honey" to "Herbs"

# **Task 1c**:
# 1. You have just ran out of Ice. Add "Ice" into the list.
# 2. Insert "Bananas" between "Apples" and "Bread".

# **Task 1d**:
# You no longer want any bread. Delete "Bread" from the list.





# groceries = ["Apples" , "Bread" , "Carrots" , "Dates" , "Eggs" , "Flour" , "Grapes" , "Honey"]
# groceries[7] = "herbs"
# groceries.append("Ice")
# groceries.insert(1, "Banans")
# groceries.pop(2)
# # print(groceries)




# Task 2: List of groceries (part 2)
# 1. Use a 'for' loop and print out all the groceries on your list
# 2. If grocery == "Apples", print ": I need 5 of these"
# 3. If grocery == "Carrots", print ": I need 3 of
#    these"
# 4. If name == "Grapes", print ": Get the FarmFresh
#    brand"

# for aaugh in groceries:
#     if aaugh == "Apples":
#         print(aaugh + ": i need 5 ohhhh")
#     elif aaugh == "Carrots":
#         print(aaugh + ": aaahh i neeed 3 bruhuh")
#     elif aaugh == "Grapes":
#         print(aaugh + ": GET OUT and get the farmFreash brandd")
#     else:
#         print(aaugh)


# Task 3: Grocery shopping
# Write a program to keep track of the groceries you have placed
# into the basket.

# 1. Use a 'while' loop to ask "What item have you added to your
#    basket?"
# 2. Add the grocery into a list.
# 3. If the user types "end", exit the loop
# 4. Print all the groceries in the list in this format:
#     a. "I have bought Apples"
#     b. "I have bought Bananas"
#     c. "I have bought Carrots"
#     d. etc...
# groceries = []
# while True:
#     user = input("What item have you added to your basket???")
#     if user == "end":
#         break
#     groceries.append(user)
# for bruhh in groceries:
#     print("YUU have bought " + bruhh)


# Task 4: Online Catalogue
# **Task 4a**:
# Write a program to create an online catalogue(list) for a grocery store.

# 1. Using a 'while' loop, ask the user (grocery store manager) to
#    input the items their online catalogue should have.
# 3. Add each item into the catalogue list
# 4. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the grocery store manager, do the
# following:

# 1. Imagine a customer browsing the website of the grocery store.
#    Ask the customer: "What are you looking for?"
# 2. If the item is in the list, say "Yes we sell that."
# 3. Else, say "Sorry, we don't have that."

# catalogue = []
# while True:
#     item = input("input the items their online catalogue should have.")
#     if item == "end":
#         break
#     catalogue.append(item)

# while True:
#     items = input("What are you looking for?")
#     if items in catalogue:
#         print("Yes we sell that.")
#     else:
#         print("Sorry, we don't have that.")
        


# Task 5: Lucky draw number generator
# Create a lucky draw number generator that generates 10 numbers
# between 1 to 9999.

# 1. Import the 'random' library
# 2. Using the 'random.randint()' function and a 'for' loop, add 10
#    random numbers into a list
# 3. Using another loop, announce the winners in the following format:
#     a. Winner #1: 5426
#     b. Winner #2: 3241
#     c. Etc...



# import random
# for i in range(1):
#     luck = []
#     luck.append(random.randint(1, 9999))
# for i in range(1,11):
#     luckk = random.randint(1, 9999)
#     print("winner" , (i) , "is" , str(luckk))





# Task 6: Pizza Topping
# Create a program that asks the user what pizza topping they want

# 1. Create a list of pizza toppings
# 2. Print out the list of pizza toppings with an index number next
#    to each of them in this format:
#     "1. Mushrooms"
#     "2. Pepperoni"
#     "3. Pineapple"
#     ...
# 3. In a 'while' loop, ask the user which pizza topping they want
#    (By index)
# 4. Exit the 'while' loop only when the user enters "end"
# 5. Print the toppings that the user has selected

oh = 1
ohhhhs = ["mushrooms", "pepperroni", "pineapples"]
for ohhhh in ohhhhs:
    print(str(oh) + ". " + ohhhh)
    oh += 1
while True:
    brhh = input("What pizza topping DO YOU WANT?!?!?!")
    if brhh == "end":
        break
    print("You have selected " + str(brhh))

# 13.6 Teacher solution
# Step 1: Create a list of pizza toppings
# pizza_toppings = ["Mushrooms", "Pepperoni", "Pineapple", "Onions", "Sausage", "Bacon", "Extra cheese", "Black olives", "Green peppers", "Fresh garlic"]
# user_toppings = []

# # Step 2: Use a 'for' loop to print the list of pizza toppings without using len() or enumerate()
# print("Available pizza toppings:")
# i = 1  # Manually track the index
# for topping in pizza_toppings:
#     print(str(i) + ". " + topping)
#     i += 1  # Increment the index manually

# # Step 3: Ask the user which pizza topping they want (By index)

# while True:
#     user_choice = input("Please choose your pizza topping by number: ")
#     if user_choice == "end":
#         break
#     else:
#         user_toppings.append(pizza_toppings[int(user_choice) - 1])

# for i in user_toppings:
#     print(i)

