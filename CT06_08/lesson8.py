# name = input("What is your name? ")
# That is asking for the name and puts it into the variable 'name'
# print("Nice to meet you, "  + name )
# This line prints out the 'nice to meet you + the variable 'name'




start = input("Start")
# This line stores the input into start variable
end = int(input("End"))
# This line of code stores the input into the end variable
increment = int(input("Increment"))
# This line of code stores the input into a increment variable
for i in range(start, end, increment):
    print(i)