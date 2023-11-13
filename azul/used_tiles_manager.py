from typing import List

from azul.interfaces import UsedTilesGiveInterface
from azul.simple_types import Tile
from azul.simple_types import compress_tile_list


class UsedTilesManager(UsedTilesGiveInterface):
    _used_tiles: List[Tile]

    def give(self, tiles: List[Tile]) -> None:
        super().give(tiles)
        self._used_tiles.extend(tiles.copy())

    def take_all(self) -> List[Tile]:
        used_tales = self._used_tiles.copy()
        self._used_tiles.clear()

        return used_tales

    def state(self):
        return self.__str__()

    def __str__(self):
        return compress_tile_list(self._used_tiles)
