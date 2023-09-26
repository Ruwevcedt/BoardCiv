import random

from Card import (
    Suit,
    ALL_SUITS,
    )
from Field import Nation


class User:
    session: str

    def __init__(
            self,
            session: str
            ):
        self.session = session


class Player(
        User
        ):
    suit: Suit
    nation: Nation

    def __init__(
            self,
            session: str,
            suit: Suit
            ):
        super(
            Player,
            self
            ).__init__(
            session=session
            )

        self.suit = suit
        self.nation = Nation(
            suit=self.suit
            )

    def decision(
            self,
            min: int,
            max: int
            ):
        return random.randint(
            min,
            max
            )


class Observer(
        User
        ):
    suit: Suit

    def __init__(
            self,
            session: str
            ):
        super(
            Observer,
            self
            ).__init__(
            session=session
            )

        self.suit = ALL_SUITS[0]
