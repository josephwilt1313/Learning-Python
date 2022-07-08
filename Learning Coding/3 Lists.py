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



#TWO DIMENSIONAL (2D) LISTS
#Once more, let's look at a class height example.
#Noelle is 61 inches tall, Ava is 70 inches tall, Sam is 67 inches tall, Mia is 64 inches tall.
#Previously, we saw that we could create a list representing both Noelle's name and height:

noelle = ["Noelle", 61]

#We can put several of these lists into one list, such that each entry in the list represents a student and their height:

heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

#We will often find that a two-dimensional list is a very good structure for representing grids such as games like tic-tac-toe.
#A 2d list with three lists in each of the indices. 
tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
]

#Two-dimensional lists can be accessed similar to their one-dimensional counterpart.
#Instead of providing a single pair of brackets, we will use an additional set for each dimension past the first.
#If we wanted to access "Noelle"'s height:

#Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)

#We can also use .remove() on a list that has duplicate elements.
#Only the first instance of the matching element is removed:

shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
shopping_line.remove("Chris")
print(shopping_line)

#MODIFYING 2D LISTS
#Now that we know how to access two-dimensional lists, modifying the elemenets should come naturally
#Lets return to a classroom example, but now instead of heights or tests scores, our list stores
#the student's favorite hobby

class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

#Jenny changed her mind and ins now more interested in meditation
#We will need to modify the list to accommodate the change to our class_name_hobbies list.
#To change a value in a 2D list, reassign the value using the specific index

#The list of Jenny is at index 0. The hobby is at index 1.

class_name_hobbies[0][1] = "Meditiation"
print(class_name_hobbies)


#Lets practice these skills
#Maria is entering customer data for her web store business. We're going to help her organize her data
#Start by turning this list of customer first names into a list called first_names
#Ainsley, Ben, Chani, Depak

first_names = ["Ainsley", "Ben", "Chani", "Depak"]

#Maria wants to track all customer's preferred sizes for her clothing.
#Create a list called preferred_size
#Fill the new list with the following sizes: Small, Large, Medium

preferred_size = ["Small", "Large", "Medium"]

#Oh no! WE forgot to add Depak's size, his size is medium. Use .append() to add his size

preferred_size.append("Medium")
print(preferred_size)

#Maria is having a hard time visualizing which customer is associated with each size. Lets
#restructure our two lists into a two dimensional list to help Maria
#In addition to the already available values, she is adding a third value for each customer
#that reflects if they want expedited shipping on their orders
#This will be reflected using a boolean value
#True, False, True, False

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

#Chani reachedf out to Maria, she requested to switch to regular shipping
#Change the data value to false

customer_data[2][2] = False
print(customer_data)

#Ben reached out to Maria asking to remove his shipping option because he is not sure what type he wants
#use the .remove() method to delete the shipping value from the sublist

customer_data[1].remove(False)
print(customer_data)

#One last thing, Maria recieved new customers, Amit and Karim.
#Add it to the end of customer data
#Amit, Large, True
#Karim, X-Large, False

new_customer_data = [["Amit", "Large", True], ["Karim", "X-Large", False]]
customer_data_final = customer_data + new_customer_data
print(customer_data_final)



#WORKING WITH LISTS
#Python List Methods That Will Be Discussed
#.count() Count the number of occurrences of an element in a list
#.insert() Insert an element into a specific index
#.pop() Remove an element from a specifi index or at the end of a list
#range() Built in python function to create a sequence of integers
#len() Built in python function to get the length of a list
#.sort() / sorted() A method and built in function to sort a list


#ADDING BY INDEX: INSERT
# .insert() allows us to add an element to a specific index in a list.
# takes two inputs:
# the index you want to insert to and the element you want to insert at the specified index
# .insert() method will handle shifting over elements and can be used with negative indices
# To see it in action let's imagine we have a list representing a line at a store:

store_line = ["Karla", "Maxium", "Martim", "Isabella"]

#Maxim saved a spot for his friend Viktor and we need to adjust the list to add him into the line
#For this example, we can assume Karla is the front of the line and the rest of the elements are behind her
#Here is how we would use the .insert() method to insert Viktor:

store_line.insert(2, "Vikor")

#The order and number of the inputs is important. The .insert() method expects two inputs, 
#the first being a numerical index, followed by any value as the second input.
#When we insert an element into a list, 
#all elements from the specified index and up to the last index are shifted one index to the right.

#Example problem:
#Starting code:
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

front_display_list.insert(0, "Pineapple")
print(front_display_list)


#REMOVING BY INDEX: POP
#Python gives us a method to remove elements at a specific index using a method called .pop().
#The .pop() method takes an optional single input:
#The index for the element you want to remove.

#To see it in action, let’s consider a list called cs_topics 
# that stores a collection of topics one might study in a computer science program.

cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]

#Two of these topics don’t look like they belong, let’s see how we remove them using .pop().

removed_element = cs_topics.pop()
print(cs_topics)
print(removed_element)

#The method can be called without a specific index.
#Using .pop() without an index will remove whatever the last element of the list is.
#.pop() is unique in that it will return the value that was removed. 
#If we wanted to know what element was deleted, simply assign a variable to the call of the .pop() method. 
#In this case, we assigned it to removed_element.

#Lastly lets remove "Balloon Making"

cs_topics.pop(2)
print(cs_topics)

#The method can be called with an optional specific index to remove. 
#In our case, the index 2 removes the value of "Balloon Making"
#We don’t have to save the removed value to any variable if we don’t care to use it later.

#Example problem
#Starting code:

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

#It looks like we have an overlap with our computer science curriculum for the topic of "Python 3".
#Let’s remove the topic from the list of data_science_topics using our newly learned .pop() method.

#Print data_science_topics to see your result.

data_science_topics.pop()
print(data_science_topics)

#Looks like there is overlap on the "Algorithms" topic as well. Let’s use .pop() to remove it as well.
#Print data_science_topics to see the changes.

data_science_topics.pop(3)
print(data_science_topics)


#CONSECUTIVE LISTS: RANGE
#Often, we want to create a list of consecutive numbers in our programs. 
#For example, suppose we want a list containing the numbers 0 through 9:

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Typing out all of those numbers takes time and the more numbers we type, 
#the more likely it is that we have a typo that can cause an error.
#The function range() takes a single input, 
#and generates numbers starting at 0 and ending at the number before the input.
#So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9

my_range = range(10)
print(my_range)

#The range() function is unique in that it creates a range object. 
#It is not a typical list like the ones we have been working with.
#In order to use this object as a list, 
#we have to first convert it using another built-in function called list().
#The list() function takes in a single input for the object you want to convert.
#We use the list() function on our range object like this:

print(list(my_range))

#Example Problem:
#Starting Code:
number_list = range(3)
print(list(number_list))

#Modify number_list 
#so that it is a range containing numbers starting at 0 and up to, but not including, 9.

number_list = range(9)
print(list(number_list))

#Create a range called zero_to_seven with the numbers 0 through 7.
#Print the result in list form.

zero_to_seven = range(8)
print(list(zero_to_seven))

#By default, range() creates a list starting at 0
#However, if we call range() with two inputs, we can create a list that starts at a different number.
#For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):

my_list = range(2, 9)
print(list(my_list))

#If we use a third input, we can create a list that “skips” numbers.
#For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:
#lists a range from two through nine but every number gets added by 2

my_range2 = range(2, 9, 2)
print(list(my_range2))

#We can skip as many numbers as we want!
#For example, we’ll start at 1 and skip in increments of 10 between each number until we get to 100:

my_range3 = range(1, 100, 10)
print(list(my_range3))

#Our list stops at 91 because the next number in the sequence would be 101, 
#which is greater than 100 (our stopping point).