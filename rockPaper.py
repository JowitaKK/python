# import random        / if playing computer
print("Rock...")
print("paper...")
print("Scissors")

player1 = input("Player 1, make your move: ").lower() # changes for lower cases
player2 = input("Player 2, make your move: ")

#======================== playing with computer
# rand_num = random.randint(0,2)
# if rand_num == 0:
#     computer = "rock"
# elif rand_num == 1:
#     computer = "paper"
# else:
#     computer = "scossors"
# print(f"Compuer plays {computer}")
#
# if player == computer:
#     prnt("its a tie")
#
#=========================

# if player1 == "rock" and player2 == "scissors":
#     print("player1 wins ")
# elif player1 == "rock" and player2 == "paper":
#     print("player2 wins")
# elif player1 == "paper" and player2 == "rock":
#     print("player1 wins")
# elif player1 == "paper" and player2 == "scissors":
#     print("player2 wins")
# elif player1 == "scissors" and player2 == "rock":
#     print("player2 wins")
# elif player1 == "scissors" and player == "paper":
#     print("player1 wins")
# elif player1 == player2:
#     print("It is a tie")
# else:
#     print("something went wrong")

# refactored code

if player1 == player2:
    print("It is a tie")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 wins ")
    elif player2 == "paper":
        print("player2 wins")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins")
    elif player2 == "scissors":
        print("player2 wins")
elif player1 == "scissors":
    if player2 == "rock":
        print("player2 wins")
    elif player == "paper":
        print("player1 wins")

else:
    print("something wrong")


# Colt code

from random import randint
# print("Rock...")
# print("Paper...")
# print("Scissors...")

# player = input("Player, make your move: ").lower()
# rand_num = randint(0,2)
# if rand_num == 0:
# 	computer = "rock"
# elif rand_num == 1:
# 	computer = "paper"
# else:
# 	computer = "scissors"
#
# print(f"Computer plays {computer}" )
#
# if player == computer:
# 	print("It's a tie!")
# elif player == "rock":
# 	if computer == "scissors":
# 		print("player wins!")
# 	else:
# 		print("computer wins!")
# elif player == "paper":
# 	if computer == "rock":
# 		print("player wins!")
# 	else:
# 		print("computer wins!")
# elif player == "scissors":
# 	if computer == "paper":
# 		print("player wins!")
# 	else:
# 		print("computer wins!")
# else:
# 	print("Please enter a valid move!")