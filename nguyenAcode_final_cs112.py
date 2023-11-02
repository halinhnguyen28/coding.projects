# Ha Linh Nguyen # Acode
# FinalCS112

import random 
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.handValue = 0
        self.hand = []
    
    def __str__(self):
        report = "The final hand value of " + str(self.name) + " is " + str(self.handValue) +" with the hand of "+ str(self.hand)
        return report

    def update_hand_value(self, card, value):
        self.hand.append(card)

        if not card.startswith('Ace'):
            self.handValue += value
        elif self.handValue > 10:
            self.handValue += value 
        else: 
            self.handValue += 11

        return self.handValue
    
    def displayHand(self,name):
        print(name+"'s current hand of cards: "+str(self.hand))

class Card: 
    def __init__(self,rank,suit):
        self.num = rank
        self.suit = suit
        self.listOfCards = []
        
    def __str__(self):
        return str(self.listOfCards) 

    def create_deck(self):

        special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

        for suit in self.suit:
            for num in self.num:
                key = str(num) + ' ' + str(suit)

                if type(num) == int:
                    value = num
                else:
                    value = special_values[num]
            
                self.listOfCards.append([key, value])

        return self.listOfCards

def main():
    
    instructions()

    name1 = input("Player 1's name: ") 
    name2 = input("Player 2 or Dealer's name: ") 

    player = Player(name1)
    dealer = Player(name2)

    rank = [2,3,4,5,6,7,8,9,10,'Ace','King','Queen','Jack']
    suit = ['♠','♥','♣','♦']
    deck = Card(rank,suit)
    deck.create_deck()
    print()
    print("Here is your deck of card:",deck)
    print()
    
    count = 0
    while count < 4:
        #alternate players to receive the card
        if count % 2 == 0:
            temp_player = player
            temp_name = name1
        else: 
            temp_player = dealer
            temp_name = name2
        
        card, value = deal(deck.listOfCards)
        temp_player.update_hand_value(card, value)
        print(temp_name, "was dealt", card)

        count += 1

    player.displayHand(name1)
    dealer.displayHand(name2)

    print()
    print("Drawing cards time for player 1 "+name1)
    hitOrStay(player, name1, deck)
    time.sleep(1)
    print("Drawing cards time for player 2 or Dealer "+name2)
    dealerHitOrStay(dealer, name2, deck)

    time.sleep(3)
    print()
    print(player)
    print(dealer)

    resultReport(player,dealer,name1,name2) #Bust included in here

def instructions():

    print("Welcome to the Blackjack game!!!")
    print("Each card in the deck has a value from 1-10 and the player with the highest value sum of cards in their hand is still <= 21 wins (ties allowed). Any player with a hand value > 21 loses (so both players might lose)")
    print("Rules:")
    print("2 players will be asigned 2 random cards alternatively. Second player will be the dealer of the game.")
    print("Player 1, after receiving the 2 cards, will be asked to draw another card or hold the cards. Type HIT to draw and STAY to hold.")
    print("Player 2, or the Dealer, is instructed to draw a new card if the hand <= 16 and hold otherwise. Type HIT to draw and STAY to hold.")
    print("The King, Queen and Jack ranks are all assigned to the 10 value")
    print("If the current hand value is greater than 10,the Ace's value is 1 otherwise the value is 11.")
    print()


def deal(deck):

    random.shuffle(deck)
    card, value = deck.pop(0) #take the first card after each shuffle from the card to one player and remove it
    return(card,value)

def hitOrStay(player, name1, deck):

    turn = True
    while turn:
        choice = input(name1+", what's your choice? HIT or STAY: ") #choose to go or not

        if choice == "HIT":
            card, value = deal(deck.listOfCards)
            player.update_hand_value(card, value)
            print(name1, 'was dealt', card)
        elif choice == "STAY":
            print(name1+", your turn ends here with no more card drawn.")
            turn = False #out of loop if choose stay
        
        player.displayHand(name1)

def dealerHitOrStay(dealer, name2, deck):

    while dealer.handValue <= 16:
        print(name2+", as your hand value is now under or equal to 16, you have to draw cards until the value is over 16 and the stop.")
        card, value = deal(deck.listOfCards)
        dealer.update_hand_value(card, value)
        print(name2,"was dealt", card)

    if dealer.handValue > 16:
        print(name2+", your hand value is now more than 16 so your turn ends here with no more card drawn.")
    
    dealer.displayHand(name2)

def resultReport(player,dealer,name1,name2):
    if player.handValue > 21 and dealer.handValue < 22:
        print("BUST! Player 1",name1,"you lost the game!")
        print("Player 2 or Dealer",name2,"is the winner of the game.")
    
    if dealer.handValue > 21 and player.handValue < 22:
        print("BUST! Player 2 or Dealer",name2,"you lost the game!")
        print("Player 1",name1,"is the winner of the game.")
    
    if dealer.handValue > 21 and player.handValue > 21:
        print("BUST you all! Your hand values are over 21, so you both lost and we don't have a winner.")

    if player.handValue > dealer.handValue and player.handValue < 22:
        print("Player 1",name1,"is the winner of this game.")
    elif player.handValue < dealer.handValue and dealer.handValue < 22:
        print("Player 2 or Dealer",name2,"is the winner of the game.")
    elif player.handValue == dealer.handValue and dealer.handValue < 22:
        print("This is a tie match. We don't have a winner.")

    print("The end! Good game!")
main()