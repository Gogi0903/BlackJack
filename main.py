from Modules.deck import Deck
from Modules.dealer import Dealer
from Modules.player import Player


def compare(player_score, house_score):
    # compares scores
    if player_score == house_score:
        return f"Your score: {player_score}. House's score: {house_score}\nIt's a bust."

    elif house_score == 0:
        return f"Your score: {player_score}. House's score: 21\nIt's a BlackJack. You loose!"

    elif player_score == 0:
        return f"Your score: 21. House's score: {house_score}\nIt's a BlackJack. You won!"

    elif player_score > 21:
        return f"Your score: {player_score}. House's score: {house_score}\nToo much. You loose!"

    elif house_score > 21:
        return f"Your score: {player_score}. House's score: {house_score}\nIt's beyond 21. You won!"

    elif house_score > player_score:
        return f"Your score: {player_score}. House's score: {house_score}\nYou loose!"

    elif house_score < player_score:
        return f"Your score: {player_score}. House's score: {house_score}\nYou won!"
    
my_deck = Deck()
deck = my_deck.create_deck()
dealer = Dealer(deck)


def game():

    is_player_turn_ended = False

    player_hand = Player()
    house_hand = Player()
    
    for _ in range(2):
        player_hand.draw_card(dealer.pick_card())
        house_hand.draw_card((dealer.pick_card()))

    while not is_player_turn_ended:

        print('___________________________________')
        print(f'Your cards: {player_hand.hand}.\nYour score: {player_hand.score}')
        print(f"House's first cards: {house_hand.first_card_in_hand}, XX")
        print('___________________________________')

        if player_hand.score == 21 or house_hand.score == 21 or player_hand.score > 21:
            is_player_turn_ended = True
        else:
            if dealer.want_more('Do you need card? (y/n) '):
                player_hand.draw_card(dealer.pick_card())
            else:
                is_player_turn_ended = True

    if player_hand.score > 21:
        print('___________________________________')
        print(f'Your cards: {player_hand.hand}.')
        print(f"House's cards: {house_hand.hand}")
        print('___________________________________')
        print(compare(player_hand.score, house_hand.score))
        input('Press enter to continue!')
        # itt még törölni kellene a consolet
        game()

    while house_hand.score < 17:
        house_hand.draw_card((dealer.pick_card()))

    print('___________________________________')
    print(f'Your cards: {player_hand.hand}.')
    print(f"House's cards: {house_hand.hand}")
    print('___________________________________')
    print(compare(player_hand.score, house_hand.score))

    if not len(deck) > 10:
        print('There are not enough cards to continue.\nThank you for playing!')
        return
    else:
        input('Press enter to continue!')
        # itt még törölni kellene a consolet
        game()

game()