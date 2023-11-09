# create a rock, paper and scissors game

# import random module
import random

# define variables to store valid_moves
valid_moves = ["rock", "paper", "scissors"]
player1 = ""
player2 = ""
player1_score = 0
player2_score = 0

play_again = True
while play_again == True:
    # print welcome message
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    # show rules
    print("Rules: ")
    print("Rock beats scissors")
    print("Scissors beats paper")
    print("Paper beats rock")

    # read input from player1
    valid_input_player = False
    while valid_input_player == False:
        player1 = input("Player 1, make your move: ").lower()
        if player1 in valid_moves:
            valid_input_player = True
        else:
            print("Invalid move, you can only choose rock, paper or scissors")

    # read input from CPU player (player2)
    player2 = random.choice(valid_moves)
    print("Computer chose: " + player2)

    # Determine the winner and add score to the winner
    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("player1 wins!")
            player1_score += 1
        elif player2 == "paper":
            print("player2 wins!")
            player2_score += 1
    elif player1 == "paper":
        if player2 == "rock":
            print("player1 wins!")
            player1_score += 1
        elif player2 == "scissors":
            print("player2 wins!")
            player2_score += 1
    elif player1 == "scissors":
        if player2 == "paper":
            print("player1 wins!")
            player1_score += 1
        elif player2 == "rock":
            print("player2 wins!")
            player2_score += 1
    else:
        print("something went wrong")

    # ask player if they want to play again
    valid_input_play = False
    while valid_input_play == False:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            valid_input_play = True
            play_again = True
        elif play_again == "n":
            valid_input_play = True
            play_again = False
        else:
            print("Invalid input, you can only choose y or n")

# print final score
print("Final score:")
print(f"Player1: {player1_score}")
print(f"Player2: {player2_score}")
print("Goodbye!")

