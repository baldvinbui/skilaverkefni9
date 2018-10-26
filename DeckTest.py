import random

class Card():
    def __init__(self, rank = "", suit = ""):
        rank_dict = {"1":"A","11":"J","12":"Q","13":"K"}
        #if(type(rank) == str):
        #    if rank in '111213':
        #        rank = int(rank)
        #        #pass

        if(type(rank) == int):
            if rank >= 1 and rank <= 13:
                if rank >= 2 and rank <= 10:
                    rank = str(rank)
                elif str(rank) in rank_dict:
                    rank = str(rank)
                    rank = rank_dict[rank]

        if rank not in '12345678910111213aAjJqQkK':
            rank = "blk"

        if type(suit) == int or suit not in "SDHCsdhc":
            suit = "blk"
        
        #if self.is_blank() == False:
        if rank == "" or suit == "":
            rank = "blk"
            suit = "blk"

        self.suit = suit
        self.rank = rank

    def __str__(self):
        if self.rank != "blk" and self.suit != "blk" or self.is_blank() == False:
            return "{:>3}{}".format(self.rank.upper(),self.suit.upper())
        else:
            return "{}".format("blk")

    def is_blank(self):
        if self.rank == "" or self.suit == "":
            return False
        else:
            return True

class Deck():
    def __init__(self):
        deck = []
        suits = "hsdc"
        for suit in suits:    
            for card in range(1,14):
                card_name = str(Card(str(card),suit)).strip()
                deck.append(card_name)
        self.deck = deck
        # A constructor without any parameters. The constructor creates a deck of 52 cards.
    
    def __str__(self):
        printed = ""
        #print(self.deck)
        deck_of_thirteen = [self.deck[x:x+13] for x in range(0, len(self.deck), 13)]
        for thirteen in deck_of_thirteen:
            printed += (" {:>3}"*len(thirteen)).format(*thirteen) + "\n"
        return printed
        # Method __str__() for returning a string representation of a deck, consisting of 4 lines containing 13 cards each.
    
    def shuffle(self):
        random.shuffle(self.deck)

        # Method shuffle(). Shuffles the cards in the deck.
    
    def deal(self):
        #print(self.deck)
        return self.deck.pop()
        #hand1 = []
        #hand2 = []
        #hand3 = []
        #hand4 = []
#
        #while len(self.deck) > 0:
        #    hand1.append(self.deck.pop())
        #    hand2.append(self.deck.pop())
        #    hand3.append(self.deck.pop())
        #    hand4.append(self.deck.pop())
#
        #return hand1, hand2, hand3, hand4
        # Method deal(). Deal a single card by returning the card that is removed off the top of the deck.

class PlayingHand():
    # A constant, NUMBER_CARDS, with value 13
    NUMBER_CARDS = 13

    def __init__(self):
        hand = ["blk" for line in range(self.NUMBER_CARDS)]
        self.hand = hand
        # A constructor without any parameters. The constructor creates a hand of 13 blank cards.
    
    def __str__(self):
        printed = (" {:>3}"*len(self.hand)).format(*self.hand)
        return printed
        # Method __str__() for returning a string representation of a playing hand, consisting of a single line containing a string representation of each card.
    
    def add_card(self):
        return "s1"
        # Method add_card() with the parameter denoting a card. The methods adds the given card to the playing hand at the first blank position.

def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5,'s')
    print(card2)
    card3 = Card('Q','D')
    print(card3)
    card4 = Card('x', 7)
    print(card4)

def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands '''
    for i in range(PlayingHand.NUMBER_CARDS):
        pass
        #hand1.add_card(deck.deal())
        #hand2.add_card(deck.deal())
        #hand3.add_card(deck.deal())
        #hand4.add_card(deck.deal())
        print(deck.deal())
        
def print_4_hands(hand1, hand2, hand3, hand4):
    ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)

def test_hands(deck):
    hand1 = PlayingHand()
    hand2 = PlayingHand()
    hand3 = PlayingHand()
    hand4 = PlayingHand()
    print("The 4 hands:")
    print_4_hands(hand1, hand2, hand3, hand4)
    deal_4_hands(deck, hand1, hand2, hand3, hand4)

random.seed(10)
test_cards()
deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)
test_hands(deck)