from random import randint
import WordGameFunctions
import twl

wins = 0
losses = 0

wordList = list(twl.iterator())

print("H A N G M A N")

while True:
    command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if command == "play":
        word = []
        wordToGuessAsAList = []
        lettersGuessed = []

        attempts = 8

        wordToGuess = wordList[randint(0, len(wordList) - 1)]

        for letter in wordToGuess:
            word.append("-")
            wordToGuessAsAList.append(letter)

        while attempts > 0:
            print()
            correctLetters = 0
            WordGameFunctions.printWord(word)

            letterGuess = input("Input a letter: ")

            if (len(letterGuess) > 1) or (len(letterGuess) == 0):
                print("Please, input a single letter.")
                continue

            if letterGuess == letterGuess.upper():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue

            if letterGuess in lettersGuessed:
                print("You've already guessed this letter.")
                continue
            else:
                lettersGuessed.append(letterGuess)

            if not (letterGuess in wordToGuess):
                print("That letter doesn't appear in the word.")
                attempts -= 1

            WordGameFunctions.letterChecker("HANGMAN", wordToGuessAsAList, word, letterGuess)

            for position in range(len(wordToGuessAsAList)):
                if wordToGuessAsAList[position] == word[position]:
                    correctLetters += 1

            print(lettersGuessed)

            if correctLetters == len(wordToGuessAsAList):
                break

        print()

        if attempts > 0:
            print(f"You guessed the word {wordToGuess}!")
            print("You survived!")
            wins += 1
        else:
            print("You lost!")
            print(f"The word was {wordToGuess}!")
            losses += 1

    elif command == "exit":
        break
    elif command == "results":
        print()
        print(f"You won: {wins} times.")
        print(f"You lost: {losses} times")

    print()