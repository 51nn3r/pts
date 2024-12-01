from __future__ import annotations

from dataclasses import dataclass
from typing import List

from azul.tile_source import TileSource
from azul.simple_types import Tile
from azul.simple_types import STARTING_PLAYER


@dataclass(frozen=True)
class TableCenter(TileSource):
    _tiles: List[Tile]

    def take(
            self,
            idx: int,
    ) -> (List[Tile], TileSource):
        tiles, other_tiles = super().take(idx)

        if STARTING_PLAYER in other_tiles:
            tiles.append(STARTING_PLAYER)
            other_tiles.remove(STARTING_PLAYER)

        return tiles, other_tiles
