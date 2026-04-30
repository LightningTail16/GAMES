from random import randint
import WordGameFunctions
import twl


while True:
    command = input('Type "play" to play the game and "exit" to quit: ')

    if command.lower() == "play":
        numberOfLetters = 0
        while (numberOfLetters < 2) or (numberOfLetters > 15):
            print()
            numberOfLetters = input("How many letters would you like each word to have? (2-15) ")
            try:
                numberOfLetters = int(numberOfLetters)
            except ValueError:
                print("That is not a number")
                numberOfLetters = 0
                continue
            numberOfLetters = int(numberOfLetters)
            if numberOfLetters < 2:
                print("That is not enough letters")
            elif numberOfLetters > 15:
                print("That is too many letters")

        wordList = twl.numberIterator(numberOfLetters)

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
                    print("Note: The amount of a single letter in this list does not show the number of this letter in the word")

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