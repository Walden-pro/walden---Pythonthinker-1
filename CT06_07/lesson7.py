


# Lesson 7 - For Loop (Part 2)

## Recap 1: Debugging Average Score Program

### There is a total of 3 bugs in the following program.
### Identify and fix the bugs:

score_one = 80
score_two = 90
score_three = 75

total = score_one + score_two  + score_three

average_score = total / 3

student_name = "Alex"

print("Average score for " + student_name + " is: " , average_score)





## Task 1: For Loop: 1 to 10 using range(start, stop)

#Use a 'for' loop to print numbers from 1 to 10.


for i in range(1, 10 + 1, 1):
    print(i)

## Task 2: Even Numbers 2-20 Loop using
##         range(start, stop, step)

#Print all even numbers between 2 and 20 using a 'for' loop and
#range().

for i in range(2, 20, 2):
    print(i)

## Task 3: Countdown From 10 For Loop

#Use a 'for' loop and range() to count down from 10 to 1.

for i in range(10, 1, -1):
    print(i)


## Task 4: Word Repetition Input Loop

#Ask the user for a word and a number n. Print the word repeated
#n times (on separate lines).

#Example:
#What word would you like to repeat? <>
#How many times would you like to repeat? << 3 >>

#output:
#burger
#burger
#burger



word = input("What word would you like to repeat? ")

n = int(input("How many times would you like to repeat? "))

for _ in range(n):
    print(word)


## Task 5: Personalized Greeting Loop

#Ask for a user's name and an integer n, then print a
#personalized greeting n times.

#Example:
#What is your name? <>
#How many times would you like to repeat? << 3 >>

#output:
#Nice to meet you, burger
#Nice to meet you, burger
#Nice to meet you, burger





input(int("What is your name?"))
n = input
for i in range(3):
    print("Nice to meet you, " + name )
