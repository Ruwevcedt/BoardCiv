import copy

from Card import Suit, ALL_SUITS, ALL_CARDS


class Nation:
    suit: Suit

    king: list
    secretary: list
    premier: list
    army: list
    people: list

    def __init__(self, suit: Suit):
        self.suit = suit

        self.king = []
        self.secretary = []
        self.premier = []
        self.army = []
        self.people = []


class BattleField:
    offensive_suit: Suit
    defensive_suit: Suit

    offensive_left: list
    offensive_main: list
    offensive_right: list

    defensive_left: list
    defensive_main: list
    defensive_right: list

    def __init__(self, offensive_suit: Suit, defensive_suit: Suit):
        self.offensive_suit = offensive_suit
        self.defensive_suit = defensive_suit

        self.offensive_left = []
        self.offensive_main = []
        self.offensive_right = []

        self.defensive_left = []
        self.defensive_main = []
        self.defensive_right = []


class Nature:
    suit: Suit

    deck: list

    war: list

    def __init__(self, suit: Suit = ALL_SUITS[0]):
        self.suit = suit
        self.deck = copy.copy(ALL_CARDS)
        self.war = []


def put_cards(to_field: list, cards: list):
    to_field.extend(cards)


def pop_cards(from_field: list, cards: list):
    [from_field.remove(_card) for _card in cards]
    return cards


def move_cards(from_field: list, to_field: list, cards: list):
    put_cards(to_field=to_field, cards=pop_cards(from_field=from_field, cards=cards))
