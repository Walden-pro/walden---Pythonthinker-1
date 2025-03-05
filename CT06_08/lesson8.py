# name = input("What is your name? ")
# That is asking for the name and puts it into the variable 'name'
# print("Nice to meet you, "  + name )
# This line prints out the 'nice to meet you + the variable 'name'




start = int(input("Start: "))
# This line stores the input into start variable
end = int(input("End: "))
# This line of code stores the input into the end variable
increment = int(input("Increment: "))
# This line of code stores the input into a increment variable
for i in range(start, end, increment):
# the variables are an integer, i variable is storing the numbers and calculating, start to end increasing by increment
    print(i)
# This line prints the code by the numbers.