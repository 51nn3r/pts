from __future__ import annotations

from typing import List
from azul.simple_types import Tile
from azul.simple_types import Points

from azul.settings import TILES_IN_WALL


class WallLine:
    _tile_types: List[Tile]
    _tiles: List[Tile | None]
    _up: WallLine | None
    _down: WallLine | None

    def __init__(
            self,
            tile_types: List[Tile]
    ):
        self._tile_types = tile_types
        self._tiles = [None] * len(tile_types)

        self._up = None
        self._down = None

    def link(
            self,
            up: WallLine | None,
            down: WallLine | None,
    ) -> None:
        self._up = up
        self._down = down

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

        same_tiles_count_vertical = self.count_up(tile_index) + \
                                    self.count_down(tile_index) - 1
        same_tiles_count_horizontal = self.count_left(tile_index) + \
                                      self.count_right(tile_index) - 1

        same_tiles_count = same_tiles_count_vertical + same_tiles_count_horizontal
        if same_tiles_count_vertical == 1 or same_tiles_count_horizontal == 1:
            same_tiles_count -= 1

        return Points(same_tiles_count)

    def count_up(
            self,
            index: int,
    ) -> int:
        tile = self._tiles[index]
        if tile is None:
            return 0

        if self._up is not None:
            return self._up.count_up(index) + 1

        return 1

    def count_down(
            self,
            index: int,
    ) -> int:
        tile = self._tiles[index]
        if tile is None:
            return 0

        if self._down is not None:
            return self._down.count_down(index) + 1

        return 1

    def count_left(
            self,
            index: int,
    ) -> int:
        tile = self._tiles[index]
        if tile is None:
            return 0

        if index > 0:
            return self.count_left(index - 1) + 1

        return 1

    def count_right(
            self,
            index: int,
    ) -> int:
        tile = self._tiles[index]
        if tile is None:
            return 0

        if index < TILES_IN_WALL - 1:
            return self.count_right(index + 1) + 1

        return 1

    @property
    def tiles(self):
        return self._tiles

    @property
    def is_fool(self) -> bool:
        return None not in self._tiles

    def state(self):
        return self.__str__()
