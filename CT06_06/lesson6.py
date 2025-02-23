print("Hello from lesson 6")


start = int(input("Starting number "))
stop = int(input("Stopping number "))
if start > stop:
    for count in range(start, stop -1 , -1 ):
       print(count)
else:
    for count in range(start, stop+1):
        print(count)




for i in range(10, 1 - 1, -1):
    print(i)