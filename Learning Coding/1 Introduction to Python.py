# Introduction to Python

## print("") command. Prints whatever is in the quotes

from calendar import c


print("Welcome To Python")
print("Python")
print("Time")

## You can add new abilites to Python by use of libraries
## One of those programs, named turtle, gives your program new superpowers

my_name = "Joseph"
print("Hello and Welcome to Codecademy " + my_name + "!")

# Python interprets anything after a # as a comment and therefore will not run anything after it.
# Can provide context for why something is written the way it is.
# Helps other people reading the code understand it faster.
# can be put befoe a line of code to see how the program will run without it.

#PRINT
#the print() function is used to tell a computer to talk.
#example from Mary Shelley's Frankenstein
print("There is something at work in my soul, which I do not understand")



#STRINGS
#Programmers refer to blocks of text as 'strings'
#You can use double or single quotes



#VARIABLES
#A variable is used to store data that will be used later by the program
#The '=' sign is what is used to assign a variable

#We've defined the variable "meal" here to the name of the food we ate for breakfast'
meal = "An english muffin"

#Printing out breakfast
print("Breakfast:")
print(meal)

#now update meal to be lunch
meal = "Lunch"

#Printing out lunch
print("Lunch:")
print(meal)

#Now update "meal" to be dinner
meal = "dinner"

#Printing out Lunch
print("Dinner:")
print(meal)



#ERRORS
#Python refers to mistakes as errors and will point to the location where an error occurred with a ^ character
#Fixing the errors is called debugging
#Two Common Errors:
#SyntaxError: Means there is something wrong with the way your program is written - a punctuation does not belong, a command where it is not expected,
# or a missing parenthesis
#NameError: Occurs when the Python interpreter sees a word it does not recognize.



#NUMBERS
#Integer, or int, is a whole number. It has no decimal point and contains all counting numbers as well as their negative counterparts
#A floating point number, or a float, is a decimal number. Can represent fractions or precise measurements.
#Can be defined by an_int or a_float
#example:
an_int = 2
a_float = 2.1

print(an_int + 3)

#example 2
release_year = 1998
runtime = 120
rating_out_of_10 = 8.2



#CALCULATIONS
#Python performs addition, subtraction, multiplication, and division
#+, -, *, /

#Example
print(573 - 74 + 1)
print(25 * 2)
print(10 / 5)

#Python converts all ints to floats before performing division
#Python can throw its own special error: ZeroDivisionError when attempting do divide by 0



#CHANGING NUMBERS
#Variables that are assigned numerical values can be treated the same as the numbers themselves.
#You can only update variables by using the = sign
#Example:

coffee_price = 1.50
number_of_coffees = 4

print(coffee_price * number_of_coffees)
print(coffee_price)
print(number_of_coffees)

coffee_price = 2

print(coffee_price * number_of_coffees)
print(coffee_price)
print(number_of_coffees)



#EXPONENTS
#Exponents are written as **
#Example:

print(2 ** 10)
print(8 ** 2)
print(9 ** 3)
print(4 ** 0.5)



#MODULO
#Python offers a companion to the division operator called the modulo operator.
#The modulo operator is indicated by % and gives the remainder of a divsion calculaton.
#If the number is divisible, then the result of the modulo operator
#Example:
#Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
print(32 % 3)
print(44 % 2)



#CONCATENATION
#The + operator doesn't just add two numbers, it can also "add" two strings.
#The process of combining two strings is called string concatenation.
#Performing string concatenation creates a brand new string comprised of the first string's contents
#followed by the second string's contents(without any added space between)

greeting_text = "Hey There! "
question_text = "How are you doing?"
full_text = greeting_text + question_text

print(full_text)

#If you want to concatenate a string with a number you will still need to make the number a string first.
#use the str() function
#if you're trying to print() a numeric variable you can use commas to pass it as a different argument rather than converting it to a string.
#example:
birthday_string = "I am "
age = 24
birthday_string2 = " years old today"
#concatenating an integer with strings is possible if we turn the integar into a string first
full_birthday_string = birthday_string + str(age) + birthday_string2
#prints "I am 10 years old today!"
print(full_birthday_string)
#If we just want to print an integer
#we can pass a variable as an argument to
#print() regardless of whether
#it is a string
#This also prints "I am 10 years old today"
print(birthday_string, age, birthday_string2)



#PLUS EQUALS
#Python offers a shorthand for updating variables. When you have a number saved in a variable and want
#to add to the current value, you can use the += operator
#Example:
    #First we have a variaable with a number saved
number_of_miles_hiked = 12
    #Then we need to update that variable
    #Let's say we hike another two miles today
number_of_miles_hiked += 2
    #The new value is the old value
    #Plus the number after the plus-equals
print(number_of_miles_hiked)
    #prints 14
#The plus-equals operator also can be used for string concatenation, like so:
hike_caption = "What an amazing time to walk through nature!"
hike_caption += " #nofilter"
hike_caption += " #blessed"
print(hike_caption)



#MULTI-LINE STRINGS
#Python offers multi line strings by using three quote marks (''' or """) instead of one.
#The string is useful if the string being defined contains a lot of quotation marks and we want to be sure we don't close it prematurely.



#USER INPUT
#The input() function requires a prompt message, which it will print out for the user before they enter the new information.
#example:

likes_snakes = input("Do you like snakes? ")
favorite_flightless_bird = input("What is your favorite flightless bird? ")
