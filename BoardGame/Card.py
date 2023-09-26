class Suit:
    suit: str

    def __init__(
            self,
            suit: str
            ):
        self.suit = suit

    def __str__(
            self
            ):
        return self.suit


class Letter:
    letter: str

    def __init__(
            self,
            letter: str
            ):
        self.letter = letter

    def __str__(
            self
            ):
        return self.letter


ALL_SUITS: [Suit] = [Suit(
    suit=x
    ) for x in [
                             'spade', 'heart', 'club', 'diamond', 'none'
                             ]]
ALL_LETTERS: [Letter] = [Letter(
    letter=x
    ) for x in [
                                 'Z', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
                                 ]]


class Card:
    suit: Suit
    letter: Letter

    coded_suit: int
    coded_letter: int

    def __init__(
            self,
            suit: Suit,
            letter: Letter
            ):
        self.suit = suit
        self.letter = letter

        self.coded_suit = ALL_SUITS.index(
            self.suit
            )
        self.coded_letter = ALL_LETTERS.index(
            self.letter
            )

    def __repr__(
            self
            ):
        return f"\t({self.suit} \t{self.letter})\n"


ALL_CARDS: [Card] = [
                            Card(
                                suit=_suit,
                                letter=_letter
                                ) for _suit in ALL_SUITS[:-1] for _letter in ALL_LETTERS[1:-1]
                            ] + [
                            Card(
                                suit=ALL_SUITS[-1],
                                letter=ALL_LETTERS[0]
                                )
                            ] * 2 + [
                            Card(
                                suit=_suit,
                                letter=ALL_LETTERS[-1]
                                ) for _suit in ALL_SUITS[:-1]
                            ]

print(
    ALL_CARDS
    )
'''
[	(spade 	A)
, 	(spade 	2)
, 	(spade 	3)
, 	(spade 	4)
, 	(spade 	5)
, 	(spade 	6)
, 	(spade 	7)
, 	(spade 	8)
, 	(spade 	9)
, 	(spade 	10)
, 	(spade 	J)
, 	(spade 	Q)
, 	(heart 	A)
, 	(heart 	2)
, 	(heart 	3)
, 	(heart 	4)
, 	(heart 	5)
, 	(heart 	6)
, 	(heart 	7)
, 	(heart 	8)
, 	(heart 	9)
, 	(heart 	10)
, 	(heart 	J)
, 	(heart 	Q)
, 	(club 	A)
, 	(club 	2)
, 	(club 	3)
, 	(club 	4)
, 	(club 	5)
, 	(club 	6)
, 	(club 	7)
, 	(club 	8)
, 	(club 	9)
, 	(club 	10)
, 	(club 	J)
, 	(club 	Q)
, 	(diamond 	A)
, 	(diamond 	2)
, 	(diamond 	3)
, 	(diamond 	4)
, 	(diamond 	5)
, 	(diamond 	6)
, 	(diamond 	7)
, 	(diamond 	8)
, 	(diamond 	9)
, 	(diamond 	10)
, 	(diamond 	J)
, 	(diamond 	Q)
, 	(none 	Z)
, 	(none 	Z)
, 	(spade 	K)
, 	(heart 	K)
, 	(club 	K)
, 	(diamond 	K)
]
'''
