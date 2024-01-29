#Ha Linh Nguyen 4004593 Midterm Project 1

import random

print("Hello, how is your day? Let's play some guessing games!")
print("This guessing game has 2 players and 3 different games in total.")
print("Two players will alternatively take turns playing in each game. Each player will have 3 turns each game.")
player1 = input("Welcome player 1. Enter your name: ")
player2 = input("Welcome player 2. Enter your name: ")

x = 0
y = 0

for count1 in range(1, 4):
    num = random.randint(1, 10)
    answer = random.randint(1, 100)
    while answer % num != 0:
        answer = random.randint(1, 100)
    print("Welcome to game", count1, ". Each of you has to guess a multiple-of-", num, "number between 1 and 100. You will have 3 turns each.")
    guess_list = []
    for count2 in range(1, 7):
        if count2 % 2 != 0:
            player = player1
        else:
            player = player2

        guess = int(input("Enter your guess of a multiple-of-" + str(num) + " number " + player + ": "))

        if guess % num != 0:
            print("The guess is invalid. It must be a multiple-of-", num, "number", player)
        elif guess in guess_list:
            print("This number has been guessed before", player, ". Choose another one")
        elif guess > answer:
            print("The answer is lower than your guess", player)
            guess_list.append(guess)
        elif guess < answer:
            print("The answer is higher than your guess", player)
            guess_list.append(guess)
        elif guess == answer:
            print("Congratulations! The correct number is", answer, ". You have won game", count1, "player", player)
            if player == player1:
                x += 1
            else:
                y += 1
            break
    else:
        print("Oops, you both lost game", count1, ". The correct answer is", answer)

print("Player", player1, "has won", x, "/3 games")
print("Player", player2, "has won", y, "/3 games")

if x > y:
    print("Player", player1, "has more wins than player", player2, ". You are the final winner", player1, ". Congratulations.")
elif x < y:
    print("Player", player2, "has more wins than player", player1, ". You are the final winner", player2, ". Congratulations.")
else:
    print("This is a tie match. You two are co-winners.")

print("This is the end of our game. Great job. See you in the next game,", player1, "and", player2, "!")
