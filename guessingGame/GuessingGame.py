import random as rd
import time as t


wantToPlay = False

def numberGuessing(computer=True):
    computerNumberHide = rd.randint(1,50)
#   a range where a computer guess the number

    if computer:
        userStop = int(input("computer should choose from 1 to where?: "))
        guess = rd.randint(1,userStop)
        print(guess)
#       if user put invalid input
        userAnswer = input("is that Correct ?(y/n): ").lower()
        while userAnswer != "y" and userAnswer != "n":
            print("invalid input")
            userAnswer = input("is that Correct ?(y/n): ").lower()

        if userAnswer == "y":
            print("Computer guess it right wwwwooowww!!!")
            exit()
        elif userAnswer == "n":
#       checking may be is only one step to guess correctly
            askUser = input("is it high or low (y/n): ")
            if askUser == "y":
                guess -= 1
                print(guess)
                userAnswer = input("is that Correct ?(y/n): ").lower()
                while userAnswer != "y" and userAnswer != "n":
                    print("invalid input")
                    userAnswer = input("is that Correct ?(y/n): ").lower()
                if userAnswer == "y":
                    print("Computer guess it right wwwwooowww!!!")
                    exit()
            elif askUser == 'n':
                guess += 1
                print(guess)
                userAnswer = input("is that Correct ?(y/n): ").lower()
                while userAnswer != "y" and userAnswer != "n":
                    print("invalid input")
                    userAnswer = input("is that Correct ?(y/n): ").lower()
                if userAnswer == "y":
                    print("Computer guess it right wwwwooowww!!!")
                    exit()
#   user guessing game
    else:
        userGuess = 0
        guessCount = 5
        print(f"Hello i am computer i hide a number from 1 to 50 i hope you can guess it")
        while guessCount > 0:
#           ask user for a valid input
            while True:
                try:
                    userGuess = int(input("what your guess? : "))
                    break
                except:
                    print("invalid input")
            if userGuess > computerNumberHide:
                print("the number you guess is high")
            elif userGuess < computerNumberHide:
                print("the number you guess is low")
            else:
                print("you guess it right wwwwooowww!!! good job")
                exit()
            guessCount -= 1
        print("Awwww you loose!")


def wordToGuess(words):
    hideWord = ""
    word_list = []
#   make the argument is a list
    if type(words) == type(list()):
#       filtering the words
        for word in words:
            if len(word) > 4:
                word_list.append(word)
            else:
                continue

        if len(word_list) < 1:
            print("all the words you pass they are invalid")
            print("check your word list there is no available words")
        else:
#           randomly choosing a word from the filtered ones
            hideWord = rd.choice(word_list)
            original_word = hideWord
            hideWord = hideWord.replace(hideWord[0:2], "--")
            hideWord = hideWord.replace(hideWord[-2:len(hideWord)], "--")
            return (hideWord, original_word)
    else:
        print("invalid input")





print("which mode do you want to play in a guessing game?")
print("1. number guessing game")
print("2. word guessing game")
userInput = int(input("put your input here: "))
if userInput == 1:
    print("1. give a computer oppurtunity to choose what you hide")
    print("2. computer hide a number guess it here")
    userInput = int(input("put your input here: "))
    if userInput == 1:
        numberGuessing(True)
    elif userInput == 2:
        numberGuessing(False)
    else:
        print("invalid input")

elif userInput == 2:
    secreWord = wordToGuess(["skeptic","spin","gallible","lets have a look"])
    userWord = ""

    while secreWord[1] != userWord:
        print(secreWord[0])
        userWord = input("write which word is this?")
    print("yay you guess it correct")
else:
    print("invalid input....")