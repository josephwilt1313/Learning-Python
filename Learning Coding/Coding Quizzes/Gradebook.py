#You are a student and you are trying to organize your subjects and grades using Python. 
#Let’s explore what we’ve learned about lists to organize your subjects and scores.

#Starting Code:
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#Create a list called subjects and fill it with the classes you are taking

subjects = ["physics", "calculus", "poetry", "history"]

#Create a list called grades and fill it with your scores

grades = [98, 97, 85, 88]

#Manually (without any methods) create a 2D list to combine subject and grades
#assign the value into the variable gradebook

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#Print gradebook

print(gradebook)

#Your grade for your CS class came in, you got a perfect score, 100!
#Use the append method to add a list with the values of computer science and an associated grade value of 100 to the gradebook list

gradebook.append(["computer science", 100])

#your grade for visual arts just came in, you got a 93
#append that to the list

gradebook.append(["visual arts", 93])

#Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class
#access the index of the grade for your visual arts class and modify it to be 5 points greater

gradebook[-1][-1] = 98

#you decided to switch from a numerical grade value to a Pass/Fail option for poetry
#find the gradevalue in your poetry class to .remove it

gradebook[2].remove(85)

#append with the new pass value

gradebook[2].append("pass")

#you also have your grades from last semester, create a new gradebook that combines both last semester and this semester
#into one complete gradebook called full_gradebook

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)