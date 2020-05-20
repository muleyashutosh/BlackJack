
import random
import os

os.system('clear')

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = { 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen':10,'King': 10, 'Ace': 11}



class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    
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
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
    def __len__(self):
        return len(self.deck)



class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    
    def __init__(self):
        self.total = 1000
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Set your Bet value: "))
        except:
            print("Sorry!! Enter an integer as a Bet")
        else:
        
            if chips.bet < 0:
                print("Invalid Amount Entered!! Enter a Positive Integer")
            elif chips.bet == 0:
                print("You can't bet 0!!! You need to bet something!!!")
            elif  chips.bet <= chips.total:
                break
            else:
                print(f"You dont have enough Chips!! You have {chips.total}")



def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        try:
            choice = int(input("\nWhats your move?: \n1.Hit \n2.Stand\n"))
            if choice > 0 and choice <= 2:
                if choice == 1:
                    hit(deck, hand)
                else:
                    print("Player Takes a Stand!!!")
                    playing = False
            else:
                print("Invalid Choice!!!__Choose between 1 and 2!!")
        except:
            print("Sorry!!! integer required as choice")
        else:
            break

def show_some(player,dealer):
    os.system('clear')
    print("\nDEALER's HAND:")
    print(dealer.cards[1])
    print("*one card hidden*")
    #print("Value of Dealer: ", dealer.value)
    print("\n")
    print("PLAYER's HAND: ")
    for card in player.cards:
        print(card)
    print("Value of Player: ", player.value)

def show_all(player,dealer):
    os.system('clear')
    print("\nDEALER's HAND: ")
    for card in dealer.cards:
        print(card)
    print("Value of Dealer: ", dealer.value)
    print("\n")
    print("PLAYER's HAND: ")
    for card in player.cards:
        print(card)
    print("Value of Player: ", player.value)


def player_busts(player,dealer,chips):
    print("DEALER WINS!!!____PLAYER BUSTED!!!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!!!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS!!!____DEALER BUSTED!!")
    chips.win_bet()

    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!!!")
    chips.lose_bet()

    
def push(player, dealer):
    print("PLAYER AND DEALER HAVE A TIE!!\n PUSH!!!")

if __name__ == "__main__":
     # Print an opening statement
    print("HELLO!!! WELCOME TO BLACKJACK!!!")
    # Set up the Player's chips
    chips = Chips()
    print(f"You have ${chips.total} chips")   
    round_count = 1
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
        print(f"ROUND: {round_count}".center(30,'_'))
        print("TOTAL CHIPS: ", chips.total)
        take_bet(chips)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
        print(f"\nBET VALUE: {chips.bet} \t TOTAL CHIPS: {chips.total}")
        playing = True
        while playing:  # recall this variable from our hit_or_stand function
            
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player)
            
            # Show cards (but keep one dealer card hidden)
            show_some(player, dealer)
            print(f"\nBET VALUE: {chips.bet} \t TOTAL CHIPS: {chips.total}")
            
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.value > 21:
                player_busts(player, dealer, chips)
                break
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player.value <= 21:
            while dealer.value <= 17:
                hit(deck, dealer)

            # Show all cards
            show_all(player, dealer)
            # Run different winning scenarios
            if dealer.value > 21:
                dealer_busts(player, dealer, chips)
            elif dealer.value > player.value:
                dealer_wins(player, dealer, chips)
            elif dealer.value < player.value:
                player_wins(player, dealer, chips)
            else:
                push(player, dealer)
        
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
            else:
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
            else:
                print("Please Provide a Valid Choice!!!")
      
        if choice[0].lower() == 's' or chips.total == 0:
            if chips.total == 0:
                print("You are broke!! Resetting Chips....")
            chips.total = 1000
            round_count = 1
        else:
            round_count += 1
        
        os.system('clear')

