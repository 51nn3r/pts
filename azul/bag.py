from typing import List
from random import shuffle

from azul.simple_types import Tile
from azul.simple_types import compress_tile_list
from azul.simple_types import TILE_TYPES
from azul.used_tiles_manager import UsedTilesManager

from azul.settings import *


class Bag:
    _tiles: List[Tile]
    _used_tiles_manager: UsedTilesManager

    def __init__(
            self,
            used_tiles_manager: UsedTilesManager
    ):
        self._used_tiles_manager = used_tiles_manager

        self._tiles = [tt for tt in TILE_TYPES] * TYPED_TILES_COUNT
        shuffle(self._tiles)

    def take(self, count: int) -> List[Tile]:
        tacked_tiles = []

        if len(self._tiles) < count:
            tacked_tiles.extend(self._tiles)
            count -= len(self._tiles)
            self._tiles = self._used_tiles_manager.take_all()
            shuffle(self._tiles)

        tacked_tiles.extend(self._tiles[:count])
        self._tiles = self._tiles[count:]

        return tacked_tiles.copy()

    def state(self) -> str:
        return self.__str__()

    def __str__(self):
        return compress_tile_list(self._tiles)
