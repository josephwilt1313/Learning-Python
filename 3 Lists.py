#WHAT IS A LIST?
#A list is one of the many built in data structures that allows us to work with a collection of data in a sequential order
#Suppose we want to make a list of the heights of students in a class
#Noelle is 61 in tall, Ava is 70 in, Sam is 67 in, Mia is 64 in.
#we can create a variable called heights to store these integers into a list:
#example:

heights = [61, 70, 67, 64]

#A list begins and ends with square brackets.
#Each item is separated by a comma
#It is considered good practice to enter a space after each comma.

#adding a height

heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]



#WHAT CAN A LIST CONTAIN?
#Instead of storing each student's height, we can make a list that contains their names:

names = ["Noelle", "Ava", "Sam", "Mia"]

#We can even combine multiple data types in one list.
#Example, This list contains a string and an integer:

mixed_list_string_number = ["Noelle", 61]

#Lists can contain any data type in Python!
#For example, this list contains a string, integer, boolean, and float:

mixed_list_common = ["Mia", 27, False, 0.5]



#EMPTY LISTS
#A list doesn't have to contain anything.
#Example:

empty_list = []

#Usually one is created in order to fill it up later based on another input



#LIST METHODS
#In Python, for any specific data-type, there is a built in functionality that we can use to create, manipulaate, and even delete our data.
#We call this built in functionality a method.
#For lists, methods will follow the form of list_name.method()
#Some methods will require an input value that will go between the parenthesis of the method ()
#An example of a popular list method is .append(), which allows us to add an element to the end of a list
#Example:

append_example = ['This', 'is', 'an', 'example']
append_example.append('list')
print(append_example)



#GROWING A LIST: APPEND
#We can add a single element to a list using the .append() Python method

garden = []

#We can add the element "Tomatoes" by using the .append() method

garden.append("Tomatoes")
print(garden)

#When we use .append() on a list that already has elements, our new element is added to the END of the list:

garden.append("Grapes")
print(garden)



#GROWING A LIST: PLUS (+)
#When we want to add multiple items to a list, we can use + to combine two lists, aka concatenation