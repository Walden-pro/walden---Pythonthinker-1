# Lesson 11 - AND OR NOT

# Recap 1: Purchase Advisor
# Create a program that asks the user for the price of an item (px) and
# gives a comment based on the price:

# if:
#     px <= 5: "Sounds good!"
#     px <= 50: "Are you sure you need this?"
#     px <= 500: "Where are you getting this money from?!"
#     px > 500: "Don't even think about it!"
 
px = int(input("The price of the item: "))
if px <= 5:
        print("Sounds good!")
elif px <= 50:
    print("Are you sure you need this?")
elif px <= 500:
    print("Where are you getting this money from?!")
else:
    print("Don't even think about it!")