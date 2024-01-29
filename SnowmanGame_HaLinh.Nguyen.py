# Ha Linh Nguyen
# Midterm Project II

import random
def main():
    wordList = wordListFromFile()
    #wordList = ["alligator", "squirrel", "eagle", "donkey", "monkey", "crocodile", "chimpanzee", "penguin", "buffalo", "octopus"]
    secretWord = random.choice(wordList)
    instructions()
    blanks = ["_"]*len(secretWord)
    wrongCount = 0
    guessedList = []
    playerCount = 0
    player1 = input("Enter your name player 1: ")
    player2 = input("Enter your name player 2: ")
    gameStart(secretWord,blanks,wrongCount,guessedList,playerCount,player1,player2) # statusReport and report function in getGuess

def wordListFromFile():
    file = open("wordList.txt", "r")
    lines = file.readlines()
    wordList = []
    for line in lines:
        line = line.rstrip("\n")
        wordList.append(line)
    file.close
    return wordList

def instructions():
    print("Welcome to the Snowman Game (or basically jusst a Hangman Game Winter version) !!!")
    print("You will get to guess a secret word.")
    print("There will be two players alternatively taking turns to guess the word.")
    print("The game will run until you guess all the letters and you win")
    print("Or until you get 5 wrong guesses and your snowman is built completely, then you lose.")
    print("A snowman will be built gradually. Each time you guess wrong, a part of the snowman will be built until the number of wrong guesses is 5, and then you lose.")
    print("The topic of the word is about animal. Good luck!!!")

def gameStart(sW,b,wC,gL,pC,p1,p2):

    #preview of snowman board
    display(wC)

    #print blanks to fill word
    print("Here's the blanks to fill out the letters: ", *b)

    #gamestart
    while "_" in b and wC < 5: 
        #alternate players
        if pC % 2 == 0:
            cp = p1
        elif pC % 2 != 0:
            cp = p2
        
        guess = input(cp+", type in your guess letter: ").lower()

        checkValidInput(sW,b,guess,gL,wC,pC,p1,p2,cp) #check if it's already guessed or valid or not
        
        found = False
        for char in range(len(sW)):
            if guess == sW[char]:
                b[char] = sW[char]
                print("Your guessing letter is in position", char+1, "of the secret word.") #start at 1 for user to easily keep track
                print(*b)
                found = True

        if not found and guess not in gL and guess.isalpha():
            gL.append(guess)
            wC += 1 # count the wrong guess
            pC += 1 #let one person guess until wrong
        
        display(wC)
        statusReport(b,gL)
    
    if "_" not in b and wC < 5:
        print("Congratulations "+cp+". You guessed the secret word. It's", sW)
    elif wC == 5 and "_" in b:
        print("Oh no. Both players lose the game. The secret word is", sW)
    
    report(sW,b,wC,cp)

def checkValidInput(sW,b,g,gL,wC,pC,p1,p2,cp):
    if not g.isalpha():
        print("Your guess is invalid. Remember to enter an alphabetic letter " + cp)
    elif g in gL:
        print("However, you or the other player have already guessed this letter. Try another letter.")
    else:
        print("Your guess is valid. Keep going " + cp)
            
def statusReport(b,gL):
    print("List of wrong guesses: ", gL)
    print("Your blanks of word until now: ", *b) #remind user which letters they have guessed correctly

def display(wC):
    print("Snowman building board: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "],
             ["~", "~", "~"]]   

    dict = {1:[[" ", "O", " "],[" ", " ", " "],[" ", " ", " "],["~", "~", "~"]],
            2:[[" ", "O", " "],[" ", "O", " "],[" ", " ", " "],["~", "~", "~"]],
            3:[[" ", "O", " "],[" ", "O", " "],[" ", "O", " "],["~", "~", "~"]],
            4:[[" ", "O", " "],["/", "O", " "],[" ", "O", " "],["~", "~", "~"]],
            5:[[" ", "O", " "],["/", "O", "\\"],[" ", "O", " "],["~", "~", "~"]]}
    
    if wC:
        board = dict[wC]

    print("---+---+----")
    for r in range(len(board)):
        print(board[r][0], " |", board[r][1], "|", board[r][2], "|")
        print("---+---+----")  

def report(sW,b,wC,cp):
    print("This is the final report of the game!")
    print("Number of wrong guesses in total: ", wC)
    if "_" not in b and wC <= 5:
        print("Player" + cp + " have successfully guessed", len(sW), "letters of the secret word", sW, "with",
              wC, "wrong guess(es). You are the winner " + cp)
    elif wC == 5 and "_" in b:
        print("Both players have guessed 5 times wrong in total and haven't guessed the secret word", sW, "yet.")



main()