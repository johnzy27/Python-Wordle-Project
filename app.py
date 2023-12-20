#Calculator Project Test
"""
first_num = float(input("Enter first number "))
second_num = float(input("Enter second number "))

sum = first_num + second_num
print("Sum: " + str(sum))
"""
#String test
"""
course = "Python for beginners"
print(course.upper())
print(course)
print("Python" in course)
"""
#Condition Operators exercise

"""
weight = float(input("Enter Weight:" ))

weight_type = input("(K)g or (L)bs: ")

print("Weight type: " + weight_type)

if (weight_type == "L" or weight_type == "l"):
    Kg = weight *0.45
    print("Weight in Kg: ", Kg )

elif (weight_type == "K" or weight_type == "k"):
    Lbs = weight * 2.2
    print("Weight in Lbs: ", Lbs)

print(" Done")
"""
#while loop exercise
"""
i = 1
while i <=10:
    print( i * " *")
    i = i + 1
"""

#List exercise
"""
names = ["John", "Bob", "Mosh", "Sam", "Mary"]

#How to update an element inside list
#names[0] = "Jon"

#printing a select range of values from list
print(names[0:3])

#list has forward index as well as backward(negative index)
print(names[-2])
print(names[3])

#List Methods
numbers = [1,2,3,4,5]

#Adding element to list
numbers.append(6)

print(numbers)

#Inserting element to list in begining, middle or end
#first we specify what index we are adding to then the value
numbers.insert(0, -1)
print(numbers)

#removing an index from list
numbers.remove(3)
print(numbers)

#search function that returns a boolean. True if found & False if not found.
print( 1 in numbers)

#Function that tells you how many objects in list
print(len(numbers))

#removing all items from list
#numbers.clear()
#print(numbers)

#Iterate over a list using for loops & while loops
numbers = [1,2,3,4,5]

for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

print("done")
"""
#Range function test
#numbers = range(5, 10, 2)
#print(numbers)

"""
for item in range(5):
    print(item)
print("done")
"""

#Tuple Function     (Tuples) Lists [ ]
#numbers = (1,2,3)

#1 Exercise Return max of two numbers 
"""
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))

if (first_num > second_num):
    print(first_num)
else:
    print(second_num)

print("done")
"""

#2 FizzBall function exercise
"""
number = float(input("Enter a number: "))
def fizz_ball(number):
    
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("Returning number: " + str(number))

print("calling function")

fizz_ball(3)
fizz_ball(5)
fizz_ball(15)
fizz_ball(1)
fizz_ball(number)
"""

#3 Checking speed function
"""
def check_speed(speed):
    
    if speed <= 70:
        print("Ok")
    elif speed > 70:
        points = (speed - 70) // 5
        print("Points: " + str(points))
        if points >= 12:
            print("License Suspended")

check_speed(70)
check_speed(80)
check_speed(90)
check_speed(100)
check_speed(110)
check_speed(120)
check_speed(130)
print("done")
"""

#4 Exercise Show Numbers
"""
def show_numbers(limit):

    for item in range(0, limit):
        if (item % 2) == 0:
            print(str(item) + " EVEN")
        else:
            print(str(item) + " ODD")
        
        item = item + 1
    
    print("Done")

show_numbers(3)
"""


#5 Exercise sum of multiples of 3 and 5 between 0 and limit 
"""
def return_sum(limit):

    for item in range(3, limit + 1):
        if item % 3 == 0 or item % 5 == 0:
            print(str(item) + " ", end ="")
        item = item + 1
return_sum(20)
"""
#6 Exercise Write a function called show_stars(rows). If rows is 5, it should print the following
"""
def show_stars(rows):
        
        for item in range(1, rows + 1):

            if rows == 5:
                  print( item * "*")
            else:
                  return
            item = item + 1

print("calling function")
show_stars(2)
show_stars(5)
show_stars(6)
"""

#7 Exercise Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
"""
def print_prime(limit):

    for item in range(2, limit + 1):

        if item % 2 == 0:
            print("Prime: " + str(item))
        else:
            print("Not Prime: " + str(item))
        item = item + 1
    
print_prime(10)
"""

"""
start = int(input("Enter your Start Number: "))
                  
end = int(input("Enter your Last Number: "))

print("Prime numbers between ", start , end)

for i in range( start , end + 1):
    if i > 1:
        
        for j in range(2, i):

            if(i % j) == 0:
                break
            else:
                print(i)
"""

#Word Raider Project
game_title = "Word Raider"

#importing in random library
import random

#Open word file
f = open("words.txt", "r")

#init list
word_list = []
misplaced_letters = []
incorrect_letters = []
max_turns = 5
current_turns = 0

#reading file into list
#word_list = f.readlines()
word_list= [x.strip().lower() for x in f.readlines()]

#random word chosen from list
word = random.choice(word_list)

#printing random word
print(word)

#welcome msg to player
print("Welcome to " + game_title )

#display game state
print("The word has " + str(len(word)), "letters")
print("You have", max_turns - current_turns, "turns left.")

while current_turns < max_turns:

    guess = input("Guess a word: ").lower()

    if len(guess) != len(word) or not guess.isalpha():
        print("Please enter a 5-letter word")
        continue
    
    index = 0
    for item in guess:
        if item == word[index]:
            print(item, end=" ")
            if item in misplaced_letters:
                misplaced_letters.remove(item)
        elif item in word:
            if item not in misplaced_letters:
                    misplaced_letters.append(item)
            print("_", end=" ")
        else:
            if item not in incorrect_letters:
                  incorrect_letters.append(item)
            print("_", end=" ")
        index = index + 1

    print("\n")
    print("Misplaced Letters: ", misplaced_letters)
    print("Incorrect Letters: ", incorrect_letters)

    #increment current turns
    current_turns = current_turns + 1

    #checks if guess is equal to random word. If == then player wins
    if guess == word.lower():
         print("Congratulations you have won!\n")
         break
    #checks if current turns equals max turns then player ran out of turns.
    if current_turns == max_turns:
         print("Sorry, you lost. The word was " + word)
         break
    print("Player you have" , max_turns - current_turns, "turns left.")
             

#close word file
f.close()