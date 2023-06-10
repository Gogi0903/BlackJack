import random

class Dealer:

    def __init__(self, deck):
        self.deck = deck


    def deal_card(self):
        # moves the choosed card from the deck to draw_card
        picked_card = random.choice(self.deck)
        self.deck.remove(picked_card)
        return picked_card


    def want_more(self, text=''):
        # asks the player
        try:
            want_card = input(text)
            if want_card.lower() != 'y' and want_card.lower() != 'n':
                raise KeyError
        except KeyError:
            print('Possible answer: (y)es or (n)o')
            self.want_more()
        else:
            if want_card.lower() == 'y':
                return True
