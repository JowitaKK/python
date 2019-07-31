# # ask for age
# age = input("how old are You: ")  # remember its string and answer is int
# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         print("You can enter, but need a wristband ")
#     elif age >= 21:
#         print("You are good to enter and can drink")
#     else:
#         print("You are little one, no enter ")
# else:
#     print("Please enter an age")



# calling sick regarding job

from random import choice, randint

actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)


calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# Note, we don't need to check if actually_sick == True
#  Instead, just check if actually_sick, since it's a boolean

if actually_sick and sick_days > 0:
    calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False