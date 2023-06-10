from Modules.deck import Deck
from Modules.dealer import Dealer
from Modules.score import Score, Comparison

my_deck = Deck()
deck = my_deck.create_deck()
dealer = Dealer(deck)


def game():

    player_hand = []
    house_hand = []

    is_player_turn_ended = False

    for i in range(2):
        player_hand.append(dealer.deal_card())
        house_hand.append(dealer.deal_card())

    house_score = Score(in_hand=house_hand).check_scores()

    while not is_player_turn_ended:

        player_score = Score(in_hand=player_hand).check_scores()

        if player_score == 0:
            player_score = 21

        print('___________________________________')
        print(f'Your cards: {player_hand}.\nYour score: {player_score}')
        print(f"House's cards: {house_hand[0]}, XX")
        print('___________________________________')

        if player_score == 0 or house_score == 0 or player_score > 21:
            is_player_turn_ended = True
        else:
            if dealer.want_more('Do you need card? (y/n) '):
                player_hand.append(dealer.deal_card())
            else:
                is_player_turn_ended = True

    if player_score > 21:
        print('___________________________________')
        print(f'Your cards: {player_hand}.')
        print(f"House's cards: {house_hand}")
        print('___________________________________')
        print(Comparison(player_score, house_score).compare())
        input('Press enter to continue!')
        # itt még törölni kellene a consolet
        game()

    while house_score != 0 and house_score < 17:
        house_hand.append(dealer.deal_card())
        house_score = Score(in_hand=house_hand).check_scores()

    print('___________________________________')
    print(f'Your cards: {player_hand}.')
    print(f"House's cards: {house_hand}")
    print('___________________________________')
    print(Comparison(player_score, house_score).compare())

    if not len(deck) > 10:
        print('There are not enough cards to continue.\nThank you for playing!')
        return
    else:
        input('Press enter to continue!')
        # itt még törölni kellene a consolet //import os / os.system('cls') valamiért nem működik
        game()

game()