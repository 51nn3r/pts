from typing import List

from tile_source import TileSource
from azul.simple_types import Tile
from azul.simple_types import STARTING_PLAYER


class TableCenter(TileSource):
    _tiles: List[Tile]

    def add(
            self,
            tiles: List[Tile]
    ):
        self._tiles = [STARTING_PLAYER]
        self._tiles.extend(tiles)

    def take(self, idx: int) -> List[Tile]:
        tiles = super().take(idx)

        if STARTING_PLAYER in self._tiles:
            tiles.append(STARTING_PLAYER)
            self._tiles.remove(STARTING_PLAYER)

        return tiles
