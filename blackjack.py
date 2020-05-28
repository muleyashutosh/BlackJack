'''
A Single Player BlackJack Game Module 
Made By:- Ashutosh Muley
'''

import random
import os
import time

os.system('clear')

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}



class Card:
    '''
    A Class to define a single card object
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __len__(self):
        return self.value


class Deck:
    '''
    A class to define a deck of 52 card objects
    '''
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def __str__(self):
        deck_string = ""
        for card in self.deck:
            deck_string += str(card) + "\n"

        return "The Deck Has: \n" + deck_string
    def shuffle(self):
        '''
        Shuffle the deck
        '''
        random.shuffle(self.deck)

    def deal(self):
        '''
        deal a single card to player's hand
        '''
        return self.deck.pop()
    def __len__(self):
        return len(self.deck)



class Hand:
    '''
    A class to define a player's hand with cards
    '''
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        '''
        add a single card to the hand
        '''
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        '''
        adjust the value of ace so not to bust
        '''
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    '''
    A class to control the bets and total no. of chips
    '''
    def __init__(self):
        self.total = 1000
        self.bet = 0

    def win_bet(self):
        '''
        add bet value to total chips
        '''
        self.total += self.bet

    def lose_bet(self):
        '''
        take bet value from total chips
        '''
        self.total -= self.bet


def take_bet(mychips):
    '''
    A function to take a bets
    input: chips object
    '''
    while True:
        try:
            mychips.bet = int(input("Set your Bet value: "))
        except ValueError:
            print("Sorry!! Enter an integer as a Bet")
        else:

            if mychips.bet < 0:
                print("Invalid Amount Entered!! Enter a Positive Integer")
            elif mychips.bet == 0:
                print("You can't bet 0!!! You need to bet something!!!")
            elif  mychips.bet <= mychips.total:
                break
            else:
                print(f"You dont have enough Chips!! You have {chips.total}")



def hit(mydeck, hand):
    '''
    Function to add cards to a hand from a given deck
    input: deck and hand(player or dealer)
    '''
    hand.add_card(mydeck.deal())
    hand.adjust_for_ace()


def hit_or_stand(mydeck, hand):
    '''
    A function to allow user to Make a move Hit or stand.
    input: deck, hand
    '''
    play = True # to control an upcoming while loop

    while True:
        try:
            cho = int(input("\nWhats your move?: \n1.Hit \n2.Stand\n"))
            if 0 < cho <= 2:
                if cho == 1:
                    hit(mydeck, hand)
                else:
                    print("Player Takes a Stand!!!")
                    play = False
            else:
                print("Invalid Choice!!!__Choose between 1 and 2!!")
        except ValueError:
            print("Sorry!!! integer required as choice")
        else:
            break
    return play

def show_some(playerh, dealerh):
    '''
    function to show some details of player's and dealer's hand(one card hidden)
    input: player's hand, dealer's hand
    '''
    os.system('clear')
    print("\nDEALER's HAND:")
    print(dealerh.cards[1])
    print("*one card hidden*")
    #print("Value of Dealer: ", dealer.value)
    print("\n")
    print("PLAYER's HAND: ")
    for card in playerh.cards:
        print(card)
    print("Value of Player: ", playerh.value)

def show_all(playerh, dealerh):
    '''
    Function to show all cards in both player's and dealer's hands
    input: player's hand, dealer's hand
    '''
    os.system('clear')
    print("\nDEALER's HAND: ")
    for card in dealerh.cards:
        print(card)
    print("Value of Dealer: ", dealerh.value)
    print("\n")
    print("PLAYER's HAND: ")
    for card in playerh.cards:
        print(card)
    print("Value of Player: ", playerh.value)


def player_busts(mychips):
    '''
    called when player busts over 21 and loses bet
    '''
    print("DEALER WINS!!!____PLAYER BUSTED!!!")
    mychips.lose_bet()

def player_wins(mychips):
    '''
    called when player wins the bet
    '''
    print("PLAYER WINS!!!")
    mychips.win_bet()

def dealer_busts(mychips):
    '''
    called when dealer busts over 21 and player wins bet
    '''
    print("PLAYER WINS!!!____DEALER BUSTED!!")
    mychips.win_bet()


def dealer_wins(mychips):
    '''
    called when dealer wins and player loses bet
    '''
    print("DEALER WINS!!!")
    mychips.lose_bet()


def push():
    '''
    called when there is a TIE
    '''
    print("PLAYER AND DEALER HAVE A TIE!!\n PUSH!!!")

if __name__ == "__main__":
     # Print an opening statement
    print("HELLO!!! WELCOME TO BLACKJACK!!!")
    # Set up the Player's chips
    chips = Chips()
    print(f"You have ${chips.total} chips")
    ROUNDS_COUNT = 1
    while True:

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        player = Hand()
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        player.adjust_for_ace()
        dealer = Hand()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())
        dealer.adjust_for_ace()
        # Prompt the Player for their bet
        print(f"ROUND: {ROUNDS_COUNT}".center(30, '_'))
        print("TOTAL CHIPS: ", chips.total)
        take_bet(chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
        print(f"\nBET VALUE: {chips.bet} \t TOTAL CHIPS: {chips.total}")
        PLAY = True
        while PLAY:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            PLAY = hit_or_stand(deck, player)

            # Show cards (but keep one dealer card hidden)
            show_some(player, dealer)
            print(f"\nBET VALUE: {chips.bet} \t TOTAL CHIPS: {chips.total}")

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.value > 21:
                player_busts(chips)
                break
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player.value <= 21:
            while dealer.value <= 17:
                hit(deck, dealer)

            # Show all cards
            show_all(player, dealer)
            # Run different winning scenarios
            if dealer.value > 21:
                dealer_busts(chips)
            elif dealer.value > player.value:
                dealer_wins(chips)
            elif dealer.value < player.value:
                player_wins(chips)
            else:
                push()

        # Inform Player of their chips total
        print("TOTAL CHIPS: ", chips.total)
        # Ask to play again
        while True:
            choice = input("Would you like to continue Playing?(Yes / NO)\n")
            if choice == "":
                print("Please Provide Valid Choice!!!")
                continue
            if choice[0].lower() == 'n' or choice[0].lower() == 'y':
                break

            print("Please Provide Valid Choice!!!")

        if choice[0].lower() == 'n':
            break

        while True:
            choice = input("Would you like to Start Over or Continue Playing?(S / C)\n")
            if choice == "":
                print("Please Provide Valid Choice!!!")
                continue
            if choice[0].lower() == 's' or choice[0].lower() == 'c':
                break

            print("Please Provide a Valid Choice!!!")

        if choice[0].lower() == 's' or chips.total == 0:
            if chips.total == 0:
                print("You are broke!! Resetting Chips....")
                time.sleep(1.5)


            chips.total = 1000
            ROUNDS_COUNT = 1
        else:
            ROUNDS_COUNT += 1

        os.system('clear')
