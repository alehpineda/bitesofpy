from collections import namedtuple

SUITS = "Red Green Yellow Blue".split()

UnoCard = namedtuple("UnoCard", "suit name")


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    uno_cards = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "Draw Two",
        "Skip",
        "Reverse",
    ]
    wild_cards = ["Wild", "Wild Draw Four"]
    zero_cards_list = [UnoCard(suit, "0") for suit in SUITS]
    uno_cards_list = [
        UnoCard(suit, name) for suit in SUITS for name in uno_cards
    ] * 2
    wild_cards_list = [UnoCard(None, name) for name in wild_cards] * 4
    return uno_cards_list + zero_cards_list + wild_cards_list
