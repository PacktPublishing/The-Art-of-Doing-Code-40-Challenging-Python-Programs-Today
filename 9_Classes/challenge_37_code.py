#Classes Challenge 37:  Casino Black Jack App
import random
import time

class Card():
    """Simulate a single card with rank, value, and suit."""

    def __init__(self, rank, value, suit):
        """Initialize card attributes"""
        self.rank = rank #2-10, J, Q, K, A
        self.value = value #1-11
        self.suit = suit 


    def display_card(self):
        """show the rank and suit of an individual card."""
        print(self.rank + " of " + self.suit)
        

class Deck():
    """Simulate a deck of 52 individual playing cards."""

    def __init__(self):
        """Initialize deck attributes"""
        self.cards = [] #A list to hold all future cards in the deck


    def build_deck(self):
        """Build a deck consisting of 52 unique cards."""
        #Information for all potential cards in a deck
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                 '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11,}

        #Build the deck, creating 52 individual cards and append them to the cards list.
        for suit in suits:
            for rank, value in ranks.items():
                card = Card(rank, value, suit)
                self.cards.append(card)


    def shuffle_deck(self):
        """Shuffle a deck of cards"""
        #Use random.shuffle() to shuffle deck
        random.shuffle(self.cards)


    def deal_card(self):
        """Remove a card from the deck to be dealt."""
        #Deal the last card in the shuffled deck
        card = self.cards.pop()
        return card


class Player():
    """A class for the user to play Black Jack."""

    def __init__(self):
        """Initialize the player."""
        self.hand = [] #A list to hold the players cards
        self.hand_value = 0 #Total value of the players current hand
        self.playing_hand = True #A bool to track if the player is playing the hand


    def draw_hand(self, deck):
        """Deal the players starting hand"""
        #Player must start with 2 cards in hand
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)
        

    def display_hand(self):
        """show the players hand."""
        print("\nPlayer's Hand: ")
        for card in self.hand:
            card.display_card()


    def hit(self, deck):
        """Give the player a new card."""
        card = deck.deal_card()
        self.hand.append(card)
        

    def get_hand_value(self):
        """Compute the value of the players hand."""
        self.hand_value = 0

        #Bool to track if you have an Ace
        ace_in_hand = False

        for card in self.hand:
            self.hand_value += card.value
            #Check for Ace
            if card.rank == 'A':
                ace_in_hand = True

        #The user went over 21, but they have an ace so treat ace as a 1.
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10 #Ace is treated as 1 instead of 11 so subtract 10 from hand_value.  

        print("Total value: " + str(self.hand_value))


    def update_hand(self, deck):
        """Update the players hand by allowing them to hit."""
        #The player has the option to hit
        if self.hand_value < 21:
            choice = input("Would you like to hit (y/n): ").lower()
            if choice == 'y':
                self.hit(deck)
            #Player is happy with hand value, done playing hand
            else:
                self.playing_hand = False
        #Player is over 21, cannot hit again
        else:
            self.playing_hand = False


class Dealer():
    """A class simulating the black jack dealer.  They must hit up to 17
    and they must reveal their first card."""

    def __init__(self):
        """Initialize the dealer"""
        self.hand = [] #A list to hold the dealers cards
        self.hand_value = 0 #Total value of the dealers current hand
        self.playing_hand = True #A bool to track if the dealer is playing the hand


    def draw_hand(self, deck):
        """Deal the dealers starting hand"""
        #Dealer must start with 2 cards in hand
        for i in range(2):
            card = deck.deal_card()
            self.hand.append(card)


    def display_hand(self):
        """Show the dealers hand one card at a time."""
        input("\nPress enter to reveal the dealer's hand. ")

        #Show all cards in the dealer's hand
        for card in self.hand:
            card.display_card()
            #Pause the program for 1 second to build suspense
            time.sleep(1)


    def hit(self, deck):
        """The dealer must hit until they have reached 17, then they stop."""
        self.get_hand_value()

        #As long as the hand_value is less than 17, dealer must hit.
        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()

        print("\nDealer is set with a total of " + str(len(self.hand)) + " cards.")


    def get_hand_value(self):
        """Compute the value of the dealers hand."""
        self.hand_value = 0

        #Bool to track if you have an Ace
        ace_in_hand = False

        for card in self.hand:
            self.hand_value += card.value
            #Check for Ace
            if card.rank == 'A':
                ace_in_hand = True

        #The dealer went over 21, but they have an ace so treat ace as a 1.
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10 #Ace is treated as 1 instead of 11 so subtract 10 from hand_value.  

    
class Game():
    """A class to hold bets and payouts"""

    def __init__(self, money):
        """Initialize attributes"""
        self.money = int(money) #Total money the user is playing with
        self.bet = 20 #Minimum bet per hand is $20
        self.winner = "" #No winner yet, no hand has been played


    def set_bet(self):
        """Get a users bet for a hand of black jack."""
        betting = True
        while betting:
            #Get a users bet
            bet = int(input("What would you like to bet (minimum bet of 20): "))
            #Bet is too small, set to min value
            if bet < 20:
                bet = 20

            #Bet is too high, make them bet again
            if bet > self.money:
                print("Sorry, you can't afford that bet.")
            #Bet is acceptable, set bet and stop betting.
            else:
                self.bet = bet
                betting = False

        
    def scoring(self, p_value, d_value):
        """Score a round of black jack."""
        #Someone got black jack 21!
        if p_value == 21:
            print("You got BLACK JACK!!! You win!")
            self.winner = 'p'
        elif d_value == 21:
            print("The dealer got black jack...You loose!")
            self.winner = 'd'

        #Someone went over 21.
        elif p_value > 21:
            print("You went over 21...You loose!")
            self.winner = 'd'
        elif d_value > 21:
            print("Dealer went over 21!  You win!")
            self.winner = 'p'

        #Other cases.
        else:
            if p_value > d_value:
                print("Dealer gets " + str(d_value) + ". You win!")
                self.winner = 'p'
            elif d_value > p_value:
                print("Dealer gets " + str(d_value) + ". You loose.")
                self.winner = 'd'
            else:
                print("Dealer gets " + str(d_value) + ". It's a push...")
                self.winner = 'tie'


    def payout(self):
        """Update the money attribute based on who won a hand."""
        #You won, you earn money
        if self.winner == 'p':
            self.money += self.bet
        #You lost, you loose money
        elif self.winner == 'd':
            self.money -= self.bet


    def display_money(self):
        """Display current money for the overall game"""
        print("\nCurrent Money: $" + str(self.money))


    def display_money_and_bet(self):
        """Display the current money and bet for a game round."""
        print("\nCurrent Money: $" + str(self.money) + "\t\tCurrent Bet: $" + str(self.bet))


#The main code
print("Welcome to the Casino Blackjack App")
print("The minimum bet at this table is $20.")

#Create a game object to keep track of bets, total cash, round winners, and payouts
money = int(input("\nHow much money are you willing to play with today: "))
game = Game(money)

#The main game loop
playing = True
while playing:
    #Build a deck, populate it with cards, and shuffle.
    game_deck = Deck()
    game_deck.build_deck()
    game_deck.shuffle_deck()

    #Create a player and dealer
    player = Player()
    dealer = Dealer()

    #Show how much money the player has and get the players bet
    game.display_money()
    game.set_bet()

    #Draw the player and dealer hands
    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    #Simulate a single round of black jack for the player
    game.display_money_and_bet()
    print("The dealer is showing a " + dealer.hand[0].rank + " of " + dealer.hand[0].suit + ".")

    #While the player is playing, show hand, calc values, allow player to hit or stay
    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)

    #Simulate a single round of black jack for the dealer
    dealer.hit(game_deck)
    dealer.display_hand()

    #Determine the winner and the payout
    game.scoring(player.hand_value, dealer.hand_value)
    game.payout()

    #The user ran out of money, kick them out
    if game.money < 20:
        playing = False
        print("Sorry, you ran out of money.  Please try again.")
