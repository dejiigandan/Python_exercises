import random
player1 = input("P1Enter: ")
player2 = random.choice(["rock", "paper", "scissors"])
print(player2)

if player1 == player2:
    print("It's a tie")
elif player1 == "rock" and player2 == "scissors":
    print("Rock wins")
elif player1 == "rock" and player2 == "paper":
    print("Paper wins")
elif player1 == "scissors" and player2 == "paper":
    print("Scissors wins")
elif player1 == "scissors" and player2 == "rock":
    print("Rock wins")
elif player1 == "paper" and player2 == "rock":
    print("Paper wins")
elif player1 == "paper" and player2 == "scissors":
    print("Scissors wins")