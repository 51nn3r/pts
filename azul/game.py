from interfaces import GameInterface
from azul.used_tiles_manager import UsedTilesManager
from bag import Bag
from azul.table_area import TableArea


class Game(GameInterface):
    _players_count: int
    _used_tiles_manager: UsedTilesManager
    _bag: Bag
    _table_area: TableArea

    def __init__(self, players_count: int):
        self._players_count = players_count
        self._used_tiles_manager = UsedTilesManager()
        self._bag = Bag(self._used_tiles_manager)
        self._table_area = TableArea(
            players_count=players_count,
            bag=self._bag,
        )

    def take(
            self,
            player_id: int,
            source_id: int,
            idx: int,
            dst: int,
    ) -> bool:
        pass
