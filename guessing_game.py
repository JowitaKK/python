# import random
#
# random_number = random.randint(1,100)
# guess = None  # or ''
#
# while guess != random_number:
#     guess = input('Pick a number prom 1 to 10 :') # String into int
#     guess = int(guess)
#     if guess < random_number:
#         print("Too low")
#     elif guess > random_number:
#         print('Too high')
#     else:
#         print("You won")
#
#     print(random_number)
#
#
import random

random_number = random.randint(1,10)

while True:
    guess = input('Pick a number prom 1 to 10 :') # String into int
    guess = int(guess)
    if guess < random_number:
        print("Too low")
    elif guess > random_number:
        print('Too high')
    else:
        print("You won")
        play_again = input("Do You want to play again? (y/n)")
        if play_again == "y":
            random_number= random.randint(1,10)
            guess = None
        else:
            print("Thank You for playing")
            break
