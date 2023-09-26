class Room:
    host: float
    players: list
    observers: list

    def __init__(
            self,
            host: float
            ):
        self.host = host
        self.players = []
        self.observers = []

    def add_player(
            self,
            player: float
            ):
        if player in self.observers:
            self.observers.remove(
                player
                )
        self.players.append(
            player
            ) if len(
            self.players
            ) < 3 else self.add_observer(
            observer=player
            )

    def add_observer(
            self,
            observer: float
            ):
        if observer in self.players:
            self.players.remove(
                observer
                )
        self.observers.append(
            observer
            )

    def players_session_ids(
            self
            ):
        return [str(
            _id
            ) for _id in [self.host] + self.players]

    def observers_session_ids(
            self
            ):
        return [str(
            _id
            ) for _id in self.observers]
