from random import randint
from WordGameFunctions import printWord
import twl

wordList = twl.numberIterator(5)
word = []
wordToGuessAsAList = []
wordToGuess = wordList[randint(0, len(wordList) - 1)]

for letter in wordToGuess:
    word.append("-")
    wordToGuessAsAList.append(letter)

print(wordList)

print(wordToGuess)

printWord(word)