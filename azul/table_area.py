from typing import List

from azul.simple_types import Tile
from azul.bag import Bag
from azul.tile_source import TileSource
from azul.table_center import TableCenter
from azul.factory import Factory

from azul.settings import PLAYERS_TO_FACTORIES


class TableArea:
    _sources: List[TileSource]

    def __init__(
            self,
            players_count: int,
            bag: Bag,
    ):
        table_center = TableCenter()
        self._sources = [table_center]

        if players_count not in PLAYERS_TO_FACTORIES:
            raise "invalid players count"

        factories_count = PLAYERS_TO_FACTORIES[players_count]
        for _ in range(factories_count):
            self._sources.append(Factory(
                bag=bag,
                table_center=table_center,
            ))

    def take(
            self,
            source_index: int,
            idx: int
    ) -> List[Tile]:

        if source_index > len(self._sources):
            raise "invalid source index"

        return self._sources[source_index].take(idx)

    def is_round_end(self) -> bool:
        for source in self._sources:
            if not source.is_empty():
                return False

        return True

    def start_new_round(self) -> None:
        for source in self._sources:
            source.start_new_round()

    def state(self) -> str:
        return self.__str__()
