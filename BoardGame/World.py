import random

from Card import ALL_SUITS
from Field import (
    Nature,
    move_cards,
    )
from User import (
    Player,
    Observer,
    )


class World:
    nature: Nature
    world: [Player]
    observer: [Observer]

    def __init__(
            self,
            session_of_players: [str],
            session_of_observers: [str]
            ):
        self.nature = Nature()
        self.world = [Player(
            session=_session,
            suit=ALL_SUITS[_code]
            )
                      for _code, _session in enumerate(
                    session_of_players
                    )]
        self.observer = Observer(
            session=session_of_observers
            )

        [move_cards(
            from_field=self.nature.deck,
            to_field=self.world[_code].nation.king,
            cards=[self.nature.deck[-4 + _code]]
            ) for _code in range(
            4
            )]
        random.shuffle(
            self.nature.deck
            )

        for _nation in [_player.nation for _player in self.world]:
            move_cards(
                from_field=self.nature.deck,
                to_field=_nation.people,
                cards=self.nature.deck[:5]
                )
            _foreigner = [_card for _card in _nation.people if _card.suit != _nation.suit]
            while len(
                    _foreigner
                    ) > 3:
                move_cards(
                    from_field=_nation.people,
                    to_field=self.nature.deck,
                    cards=_foreigner
                    )
                move_cards(
                    from_field=self.nature.deck,
                    to_field=_nation.people,
                    cards=self.nature.deck[:len(
                        _foreigner
                        )]
                    )
                _foreigner = [_card for _card in _nation.people if _card.suit != _nation.suit]
            _nation.people.sort(
                key=lambda
                    _card: _card.coded_suit
                )


debug_world = World(
    session_of_players=['0', '1', '2', '3'],
    session_of_observers=['4', '5', '6']
    )
