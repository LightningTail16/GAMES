def printWord(word):
    printWord = ""
    for position in range(len(word)):
        printWord += word[position]

    print(printWord)

def letterChecker(game, list1, list2, letter):
    for position in range(len(list1)):
        if game == "HANGMAN":
            if (list1[position] == letter) and (list2[position] != letter):
                list2.insert(position, letter)
                list2.pop(position + 1)
        if game == "Wordle":
            if (list1[position] == letter[position]) and (list2[position] != letter[position]):
                list2.insert(position, letter[position])
                list2.pop(position + 1)
