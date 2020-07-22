import random

class card:
    def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit
    



def play_war(deck):   
    a_cards = deck[:len(deck)/2]
    b_cards = deck[len(deck)/2:]
    print(f"Rank is {card.rank} suit is {card.suit}")
    for card in range(a_cards):
        print(f"Rank is {card.rank} suit is {card.suit}")

def ranks():
    return ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
def suits():
    return  ["diamonds", "clubs", "spades", "hearts"]


if __name__ == "__main__":
    deck = initialize_deck()
#def initialize_deck():  
    deck = [card(rank, suit) for rank in ranks() for suit in suits()]
    random.shuffle(deck)
    for card in deck:
        #print(f"Rank is {card.rank} suit is {card.suit}")

        play_war(deck)

