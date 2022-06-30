#Writing a Python program that can answer any "Yes" or "No" question with a different fortune every time it executes.
#"Yes - definitely"
#"It is decidedly so"
#"Without a doubt"
#"Reply hazy, try again"
#"Ask again later."
#"Better not tell you now."
#"My sources say no."
#"Outlook not so good"
#"Very doubtful."

#The output of the program will have the following format:
#[Name] asks: [Question]
#Magic 8-Ball's answer: [Answer]

name = "Joseph"
question = "Is the sky blue?"
answer = ""

#In order for the answer to be different each time we run the program, we will utilize randomly generated values.
#In Python we can use .randint() function from the random module to generate a number from a random range
#Import the module so we can use its functions.

import random

#create a variable to store the randomly generated value.

random_number = random.randint(1, 10)

print(random_number)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
  answer ="Never"
else:
    answer = "Error"

if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something")
else:
 print("Magic 8-Ball's answer: " + answer)
























