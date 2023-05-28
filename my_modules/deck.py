class Deck:

    def __init__(self):
        self.suits = ['♥', '♦', '♠', '♣']  # heart, diamonds, spade, club
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


    def create_deck(self):
        # creates a deck (list with tuple elements)
        deck = []
        for suit in self.suits:
            for rank in self.ranks:
                deck.append(suit+rank)
        return deck
