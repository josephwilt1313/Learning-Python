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
#Below, we have a list of items sold at a bakery called items_sold

items_sold = ["cake", "cookie", "bread"]

#Suppose the bakery wants to start selling "biscuit" and "tart"

items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)



#ACCESSING LIST ELEMENTS
#We are interviewing candidates for a job.
#We will call each candidate in order, represented by a Python list:

calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]

#First we'll call "Juan", then "Zofia", etc.
#In Python, we call the location of an element in a list its index
#Python lists are zero-indexed. This means the first element in a list has index 0 instead of 1
#We can select a single element from a list by using square brackets and the index of the list item.
#If we wanted to select the third element from thee list, we'd use calls[2]:

print(calls[2])

#When accessing elements of a list, you must use an int as the index. If you use a float, you will get an error.
#This can be especially tricky when using division.
#For example print(calls[4/2]) will result in an error, because 4/2 gets evaluated to the float 2.0
#To solve this problem, you can force the result of your division to be an int by using the int() function.
#For example , int(5.9) and int(5.0) will both become 5
#Therefore, calls[int(4/2)] will result in the same value as calls[2]



#ACCESSING LIST ELEMENTS: NEGATIVE INDEX
#What if we want to select the last element of a list?
#We can use the index -1 to select the last item of a list, even when we dont know how many elements are in a list
#example:

pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]

#If we select the -1 index, we get the final element, "love"

print(pancake_recipe[-1])

#Lets return to the garden.

garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]

#Unfortunately, we forgot to water our cauliflower and we don't think it is going to recover.
#Thankfully we got strawberry seeds to replace the cauliflower.
#We need to modify the list to accommodate the change to our garden list. 

garden[2] = "Strawberries"
print(garden)

#Negative indices will work as well

garden[-1] = "Raspberries"
print(garden)



#SHRINKING A LIST: REMOVE
#We can remove elements in a list using the .remove() python method
#Suppose we have a filled list called shopping_line that represents a grocery store

shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]

#We could remove "Chris" by using the .remove() method

shopping_line.remove("Chris")
print(shopping_line)

#We can also use .remove() on a list that has duplicate elements.
#Only the first instance of the matching element is removed:

shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
shopping_line.remove("Chris")
print(shopping_line)



#TWO-DIMENSIONAL (2D) LISTS