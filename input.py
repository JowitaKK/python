# print("What is your favorite colour?")
# data = input()
# print("You said " + data)

# conditional check

name = "Jow"

if name == "Tomek":
    print("its not correct")
elif name == "Jow":
    print("Almost right")
else:
    print("carry on")

# exercise
# from random import randint
# 1)

choice = randint(1, 10)

if choice == 7:
    print("lucky")
else:
    print("unlucky")

# 2)
from random import randint
num = randint(1, 1000)

if num % 2 != 0:
    print("odd")
else:
    print("even")

# 3) to check if user put any input

animal = input("entern animal")
if animal:  # here is no input so that is how we know it value is false so is checking rest
    print(animal + "is my favourite too")
else:
    print("You did not say anything!!!")

# 4)
food = choice(['apple', 'grape', 'bacon', 'steak' ])

if food == 'apple' or food == 'grape' :
    print ("fruit")
elif food == 'bacon' or food == 'steak':
    print("meat")
else:
    print("fuuu")


