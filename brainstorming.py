CARD = {'H': 2}
HAND = ['♠A', '♣A']

card = "asd"


def want_more():
    try:
        want_card = input("Do you need card? (y/n) ")
        if not want_card == 'Y':
            raise KeyError
    except KeyError:
        print('asd')
        # print('Possible answeres are: (y)es or (n)o')
        # want_more()
    else:
        vegre()


def vegre():
    print('thank you')

want_more()