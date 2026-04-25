from random import randint
import WordGameFunctions
import twl

wordList = twl.numberIterator(5)





while True:
    command = input('Type "play" to play the game and "exit" to quit: ')

    if command.lower() == "play":
        word = []
        wordToGuessAsAList = []
        wordGuessAsAList = []
        correctButWrongLetters = []
        wrongWords = []

        wordToGuess = wordList[randint(0, len(wordList))]
        lives = 6

        for letter in wordToGuess:
            word.append("-")
            wordToGuessAsAList.append(letter)

        WordGameFunctions.printWord(word)

        while lives > 0:
            wordGuess = input("Input a Word: ")
            if wordGuess in wrongWords:
                print(f"You have already guessed {wordGuess}")
                print()
                continue

            wrongWords.append(wordGuess)

            if wordGuess in wordList:
                for letter in wordGuess:
                    wordGuessAsAList.append(letter.lower())

                WordGameFunctions.letterChecker("Wordle", wordToGuessAsAList, word, wordGuessAsAList)


                WordGameFunctions.printWord(word)

                if word == wordToGuessAsAList:
                    print("You guessed the word. You Win")
                    print()
                    break
                else:
                    for i in range(len(wordGuessAsAList)):
                        if (wordGuessAsAList[i] in wordToGuessAsAList) and (not (wordGuessAsAList[i] in word)):
                            correctButWrongLetters.append(wordGuessAsAList[i])

                    print(f"There are these letters in the word, but they are wrongly placed: {correctButWrongLetters}")

                wordGuessAsAList = []
                correctButWrongLetters = []
                lives -= 1

            else:
                print("That is not a valid word")
            print()
        if (lives == 0) and (not (word == wordToGuessAsAList)):
            print(f"The word was {wordToGuess}. You Lost")

    elif command.lower() == "exit":
        print("Thank you for playing")
        break
    else:
        print("That is not a correct command!")