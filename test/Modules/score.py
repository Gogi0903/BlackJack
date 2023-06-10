class Score:

    def __init__(self, in_hand=''):
        self.score = 0
        self.in_hand = in_hand


    def card_value(self):
        # return values of player's cards in a list
        nums = []
        for card in self.in_hand:
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
            return 0
        if sum(values) > 21 and 11 in values:
            values.remove(11)
            values.append(1)
        self.score = sum(values)
        return self.score


class Comparison:

    def __init__(self, p_score=0, c_score=0):
        self.player_score = p_score
        self.computer_score = c_score


    def compare(self):
        # compares scores
        if self.player_score == self.computer_score:
            return f"Your score: {self.player_score}. House's score: {self.computer_score}\nIt's a bust."

        elif self.computer_score == 0:
            return f"Your score: {self.player_score}. House's score: 21\nIt's a BlackJack. You loose!"

        elif self.player_score == 0:
            return f"Your score: 21. House's score: {self.computer_score}\nIt's a BlackJack. You won!"

        elif self.player_score > 21:
            return f"Your score: {self.player_score}. House's score: {self.computer_score}\nToo much. You loose!"

        elif self.computer_score > 21:
            return f"Your score: {self.player_score}. House's score: {self.computer_score}\nIt's beyond 21. You won!"

        elif self.computer_score > self.player_score:
            return f"Your score: {self.player_score}. House's score: {self.computer_score}\nYou loose!"

        elif self.computer_score < self.player_score:
            return f"Your score: {self.player_score}. House's score: {self.computer_score}\nYou won!"
