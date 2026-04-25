from random import randint

options = ["rock", "paper", "scissors"]

def playerInput(numberOfPlayers, playerNumber = 1):
    if numberOfPlayers == 1:
        playerChoice = input("Enter a choice (rock, paper, scissors): ")
    elif numberOfPlayers == 2:
        playerChoice = input(f"Player {playerNumber}, enter a choice (rock, paper, scissors): ")
    else:
        print("Something went wrong")

    if playerChoice.lower() in options:
        print(f"You have chosen {playerChoice.upper()}!")
        return playerChoice.lower()
    else:
        print(f"{playerChoice.lower().capitalize()} is not one of the choices.")
        print()
        playerInput(numberOfPlayers, playerNumber)

def continuePlaying():
    play_again = input("Play again? (y/n/yes/no): ")
    if play_again.lower() == "y" or play_again.lower() == "n" or play_again.lower() == "yes" or play_again.lower() == "no":
        if play_again.lower() == "y" or play_again.lower() == "yes":
            return True
        else:
            return False
    else:
        print()
        print("Please input \"y,\" \"n,\" \"yes,\" or \"no\"")
        continuePlaying()


def results(numberOfPlayers, player1Choice = "NULL", player2Choice = "NULL"):
    player1Choice = player1Choice.lower()
    player2Choice = player2Choice.lower()
    if numberOfPlayers == 1:
        if player1Choice == player2Choice:
            message = "IT'S A TIE"
        elif player1Choice == "paper":
            if player2Choice == "rock":
                message = "PAPER BEATS ROCK, YOU WIN"
            elif player2Choice == "scissors":
                message = "PAPER GETS CUT BY SCISSORS, YOU LOSE"
            else:
                message = "Something went wrong"
        elif player1Choice == "rock":
            if player2Choice == "scissors":
                message = "ROCK BEATS SCISSORS, YOU WIN"
            elif player2Choice == "paper":
                message = "ROCK GETS COVERED BY PAPER, YOU LOSE"
            else:
                message = "Something went wrong"
        elif player1Choice == "scissors":
            if player2Choice == "paper":
                message = "SCISSORS GETS CRUSHED BY ROCK, YOU LOSE"
            elif player2Choice == "rock":
                message = "SCISSORS BEATS PAPER, YOU WIN"
            else:
                message = "Something went wrong"
        else:
            message = "Something went wrong"
    else:
        if player1Choice == player2Choice:
            message = "IT'S A TIE"
        elif player1Choice == "paper":
            if player2Choice == "rock":
                message = "PAPER BEATS ROCK, Player 1 Wins"
            elif player2Choice == "scissors":
                message = "PAPER GETS CUT BY SCISSORS, Player 2 Wins"
            else:
                message = "Something went wrong"
        elif player1Choice == "rock":
            if player2Choice == "scissors":
                message = "ROCK BEATS SCISSORS, Player 1 Wins"
            elif player2Choice == "paper":
                message = "ROCK GETS COVERED BY PAPER, Player 2 Wins"
            else:
                message = "Something went wrong"
        elif player1Choice == "scissors":
            if player2Choice == "paper":
                message = "SCISSORS GETS CRUSHED BY ROCK, Player 2 Wins"
            elif player2Choice == "rock":
                message = "SCISSORS BEATS PAPER, Player 1 Wins"
            else:
                message = "Something went wrong"
        else:
            message = "Something went wrong"

    return message

while True:
    player_count = input ("How many players? (1 or 2): ")
    print()
    if player_count.isdigit():
        players = int(player_count)

        if players != 1 and players != 2:
            print("Please enter a \"1\" or a \"2\"")
            continue
        else:
            if players == 1:
                userChoice = playerInput(players)

                computerChoice = options[randint(0, 2)]

                print(f"\nYou chose {userChoice.upper()}, computer chose {computerChoice.upper()}.\n")

                print(results(players, userChoice, computerChoice))

            else:
                player1 = playerInput(players, 1)

                for i in range(20):
                    print()

                player2 = playerInput(players, 2)

                print(f"\nPlayer 1 chose {player1}, and Player 2 chose {player2}.\n")

                print(results(players, player1, player2))

        if not continuePlaying():
            break
    else:
        print("Please enter a \"1\" or a \"2\"")