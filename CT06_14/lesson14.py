
# Task 1: Creating a window
# **Task 1a**:
# By importing the 'turtle' library and using the following functions,
# create a blank window that stays:
# 1. turtle.Screen()
# 2. .mainloop()

# **Task 1b**:
# Modify your code to create a window that is 600 in width and 400 in
# height

# Hint:
# ???.setup(width=???, height=???)

# import turtle
# window = turtle.Screen()
# window.setup(width=600, height=400)
# t = turtle.Turtle()
# window.mainloop()




# Task 2: Creating a Turtle
# By modifying the code you have done previously, create the
# following agents:

# **Your new code must be between the turtle.screen() and .mainloop()
# function**

# **Task 2a**:
# Create an orange turtle

# 1. Using 'import', import the 'turtle' library
# 2. Using the 'turtle.Turtle()' function, create an agent called "turtle"
# 3. Using the '.shape()' function, set the shape of the "turtle" agent
#    to a turtle
# 4. Using the '.fillcolor()' function, turn "turtle" orange

# **Task 2b**:
# Create a green square

# 1. Using 'import', import the 'turtle' library
# 2. Using the 'turtle.Turtle()' function, create an agent called "square"
# 3. Using the '.shape' function, set the shape of the "square" agent
#    to a square
# 4. Using the '.fillcolor()' function, turn "square" green


# import turtle
# window = turtle.Screen()
# window.setup(width=600, height=400)
# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("orange")
# window.mainloop()

# import turtle
# window = turtle.Screen()
# window.setup(width=600, height=400)
# s = turtle.Turtle()
# s.shape("square")
# s.fillcolor("green")
# window.mainloop()



# Task 3: Drawing
# Given the number of sides and each interior angle, draw each of the
# following shapes using a loop and the following functions:
#     .seth()
#     .up()
#     .down()
#     .forward()
#     .backward()
#     .left()
#     .right()

# **Task 3c**: Draw a square
# Number of sides: 4
# Interior angle: 90

# **Task 3d**: Draw a pentagon
# Number of sides: 5
# Interior angle: 72

# **Task 3e**: Draw a hexagon
# Number of sides: 6
# Interior angle: 60

# **Task 3f**: Draw a circle
# Number of sides: 360
# Interior angle: 1


#SQUARE
# import turtle
# window = turtle.Screen()
# window.setup(width=600, height=400)
# t = turtle.Turtle()
# t.down()
# t.seth(0)
# for i in range(4):
#     t.forward(100)
#     t.left(90)
# window.mainloop()

#PENTAGON
# import turtle
# window = turtle.Screen()
# window.setup(width=600, height=400)
# t = turtle.Turtle()
# t.down()
# t.seth(0)
# for i in range(5):
#     t.forward(100)
#     t.left(72)
# window.mainloop()

# import turtle
# window = turtle.Screen()
# window.setup(width=600, height=400)
# t = turtle.Turtle()
# t.down()
# t.seth(0)
# for i in range(6):
#     t.forward(100)
#     t.left(60)
# window.mainloop()


import turtle
window = turtle.Screen()
window.setup(width=600, height=400)
t = turtle.Turtle()
t.down()
t.seth(0)
for i in range(360):
    t.forward(0.69)
    t.left(1)
window.mainloop()
