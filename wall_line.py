from typing import List
from azul.simple_types import Tile
from azul.simple_types import Points


class WallLine:
    _tile_types: List[Tile]
    _tiles: List[Tile | None]

    def __init__(
            self,
            tile_types: List[Tile]
    ):
        self._tile_types = tile_types
        self._tiles = [None] * len(tile_types)

    def can_put_tile(
            self,
            tile: Tile,
    ) -> bool:
        return tile in self._tile_types and tile not in self._tiles

    def get_tiles(self) -> List[Tile | None]:
        return self._tiles

    def put_tile(
            self,
            tile: Tile
    ) -> Points:
        tile_index = self._tile_types.index(tile)
        self._tiles[tile_index] = tile
        return Points(1)

    @property
    def is_fool(self) -> bool:
        return None not in self._tiles

    def state(self):
        return self.__str__()
