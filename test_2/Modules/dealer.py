from random import choice

class Dealer:

    def __init__(self, deck):
        self.deck = deck
        self._players = []


    def pick_card(self):
        # picks a card from the deck
        picked_card = choice(self.deck)
        self.deck.remove(picked_card)
        return picked_card


    def want_more(self, text=''):
        # asks the player
        # try:
        want_card = input(text)
        if want_card.lower() != 'y' and want_card.lower() != 'n':
            print('Possible answer: (y)es or (n)o')
            self.want_more()
        else:
            return want_card.lower() == 'y'


    def new_player(self, player):
        self._players.append(player)


    def deal_round(self, nr_of_rounds):
        for _ in range(nr_of_rounds):
            for player in self._players:
                player.draw_card(self.pick_card())
