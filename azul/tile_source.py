from __future__ import annotations
from typing import List
from dataclasses import dataclass

from azul.simple_types import Tile

from azul.settings import TILES_INDEXES


@dataclass(frozen=True)
class TileSource:
    _tiles: List[Tile]

    def take(
            self,
            idx: int,
    ) -> (List[Tile], List[Tile]):
        if idx not in TILES_INDEXES or idx == 0:
            raise "invalid tile index"

        tile_representation = TILES_INDEXES[idx]
        tiles = []
        other_tiles = self._tiles.copy()
        while tile_representation in other_tiles:
            other_tiles.remove(tile_representation)
            tiles.append(tile_representation)

        return (
            tiles,
            other_tiles,
        )

    def is_empty(self) -> bool:
        return not self._tiles

    def state(self) -> str:
        return self.__str__()

    @property
    def tiles(self) -> List[Tile]:
        return self._tiles
