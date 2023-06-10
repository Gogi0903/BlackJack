class Player:

    def __init__(self):
        self._cards = []

    @property
    def score(self):
        return self.check_scores()

    @property
    def hand(self):
        return str(self._cards)

    @property
    def first_card_in_hand(self):
        return str(self._cards[0])

    def draw_card(self, picked_card):
        # draws a card from deck
        self._cards.append(picked_card)
        return self._cards

    def card_value(self):
        # return values of player's cards in a list
        nums = []
        for card in self._cards:
            if card[1] == 'A':
                nums.append(11)
            elif card[1] == 'J' or card[1] == 'Q' or card[1] == 'K' or card[1] == '1':
                nums.append(10)
            else:
                nums.append(int(card[1]))
        return nums

    def check_scores(self):
        # calculates the score
        values = self.card_value()
        if sum(values) == 21 and len(values) == 2:
            return 21
        if sum(values) > 21 and 11 in values:
            values.remove(11)
            values.append(1)
        return sum(values)
