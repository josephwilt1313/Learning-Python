#BOOLEAN EXPRESSIONS
#A boolean expression is a statement that can either be true or false



#RATIONAL OPERATORS
#We can create a boolean expression by using relational operators
#Relational operators compare two items and return either True or False
#You will sometimes hear them called comparators
#Two relational operators are Equals: == and Not Equals: !=

1 == 1     # True
2 != 4     # True
3 == 5     # False
"7" == 7   # False



#BOOLEAN VARIABLES
#True and False are their own special type: bool
#True and False are the only bool types.
#Boolean variables can be created in several ways. The easiest way is to simply assign True or False to a variable
#Example: 
set_to_true = True
set_to_false = False

#You can also set a variable equal to a boolean expression
bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

print(bool_one)
print(bool_two)
print(bool_three)



#IF STATEMENT
#Boolean variables and expressions are the building blocks of conditional statements
#"it is raining" is a boolean expression
#If "it is raining == True" then the rest of the conditional statement will be executed
#A colon tells the computer that what's coming next is what should be executed if the condition is met

user_name = "Joseph"
if user_name == "Dave":
    print("Get off my computer Dave! ")



#RELATIONAL OPERATORS II
#There are four more relational operators to know:
# > Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to
age = 12
if age <= 13:
    print("Sorry, parental control required")

x = 20
y = 20

if x == y:
    print("These numbers are the same")

credits = 120

if credits >= 120:
    print("You have enough credits to graduate!")



#BOOLEAN OPERATORS: and
#Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover
#In these cases, you cana build larger boolean expressions using boolean operators.
#These operators (known as logical operators) combine smaller boolean expressions into larger boolean expressions
#There are three boolean operators that are covered: and, or, not

#and combines two boolean expressions and evaluates if both its components are True, but false otherwise
#example:

statement_one = (2 + 2 + 2 >= 6) and  (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
    print("You meet the requirements to graduate!")

#or combines two expressions into a larger expression that is true if either component is true.

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
statement_two = (9 + 5 <= 15) or (7 != 4 +3)

credits - 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
    print("You have met at least one of the requirements.")



#not: when applied to any boolean expression it reverses the boolean value
#example:
statement_one = not (4 + 5 <= 9)
statement_two = not (8 * 2) != 20 - 4
credits = 120
gpa = 1.8
#If a student's credits is NOT greater or equal to 120
if not credits >= 120:
  print("You do not have enough credits to graduate.")
#If their GPA is NOT greater or equal to 2.0
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")
#If their credits is NOT greater than or equal to 120 AND their gpa is NOT greater than or equal to 2.0
if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")



#ELSE STATEMENTS
#else statements allow us to describe what we want our code to do when certain conditions are NOT met
#else statements always appear in conjunction with if statements

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
    print("You do not meet the requirements to graduate.")



#ELSE IF STATEMENTS
#elif statement checks another condition after the previous if statements conditions are not met.
#We can use elif statements to control the order we want our program to check each of our conditional statements.
#First, the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions are met
#Example:
donation = 50

print("Thank you for the donation!")
if donation >= 1000:
    print("You've achieved platinum status")
elif donation >= 500:
    print("You've achieved gold donor status")
elif donation >= 100:
    print("You've achieved silver donor status")
else: print("You've achieved bronze donor status")

grade = 86
if grade >= 90:
    print("A")
elif grade >= 80:
    print ("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")



if (9 - 4) * 2 == 77 / 7 - 1:
    print("true")
else:
    print("false")

if  3 ** 2 + 1 != 30 / 3:
    print("true")
else:
    print("false")

if  4 * 5 <= 21 - 1:
    print("true")
else:
    print("false")

if  (4 <= 2 * 3) and (7 + 1 == 8):
    print("true")
else:
    print("false")



#ERRORS IN PYTHON
#Python refers to the mistakes within the program as errors and will point to the errors and will point to the location where an error occurred with  ^ character.
#We call those errors bugs
#SyntaxErorr: Error caused by not following the proper structure (syntax) of the language
#NameError: Errors reported when the interpreter detects a variable that is unknown
#TypeError: Errors thrown when an operation is applied to aan object of an inappropriate type.

#SyntaxError
#Some common errors are misspelling a Python keyword
#Missing colon :.
#Missing closing parenthesis, square bracket, or curly brace.

#NameError
#Can occur if a variable is used before it has been assigned a value or if a variable name is spelled differently than the point at which it was defined
#Misspelling a variable name
#Forgetting to define a variable

#TypeError
#Can occur when one attempts to use an operator on something of the incorrect type.
#Accidentally adding or subtracting a string value.
#Call a function on something of the incorrect type.

























