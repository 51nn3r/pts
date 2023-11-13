from typing import List

from tile_source import TileSource
from azul.bag import Bag
from azul.table_center import TableCenter
from azul.simple_types import Tile


class Factory(TileSource):
    _tiles: List[Tile]
    _bag: Bag
    _table_center: TableCenter

    def __init__(
            self,
            bag: Bag,
            table_center: TableCenter,
    ):
        super().__init__()

        self._bag = bag
        self._table_center = table_center

    def take(self, idx: int) -> List[Tile]:
        tiles = super().take(idx)

        self._table_center.add(self._tiles.copy())
        self._tiles.clear()

        return tiles
