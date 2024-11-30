from __future__ import annotations

from dataclasses import dataclass
from random import shuffle
from typing import List

from azul.randomizer import Randomizer
from azul.simple_types import compress_tile_list
from azul.used_tiles_manager import UsedTilesManager

from azul.settings import *


@dataclass(frozen=True)
class Bag:
    used_tiles_manager: UsedTilesManager
    tiles: List[Tile]
    randomizer: Randomizer

    def take(
            self,
            count: int,
    ) -> (List[Tile], Bag):
        tiles = self.tiles.copy()
        tacked_tiles = []

        used_tiles_manager = self.used_tiles_manager
        if len(self.tiles) < count:
            tacked_tiles.extend(tiles)
            count -= len(tiles)
            tiles, used_tiles_manager = self.used_tiles_manager.take_all()
            tiles = self.randomizer.shuffle_array(tiles)

        tacked_tiles.extend(tiles[:count])
        tiles = tiles[count:]

        return (
            tacked_tiles.copy(),
            Bag(
                used_tiles_manager=used_tiles_manager,
                tiles=tiles,
                randomizer=self.randomizer,
            ),
        )

    def give_used_tiles(
            self,
            tiles: List[Tile],
    ) -> Bag:
        return Bag(
            used_tiles_manager=self.used_tiles_manager.give(tiles),
            tiles=self.tiles,
            randomizer=self.randomizer,
        )

    def state(self) -> str:
        return self.__str__()

    @staticmethod
    def get_start_instance(
            used_tiles_manager: UsedTilesManager,
            randomizer: Randomizer,
    ) -> Bag:
        tiles = randomizer.shuffle_array([tt for tt in TILE_TYPES] * TYPED_TILES_COUNT)
        return Bag(
            used_tiles_manager=used_tiles_manager,
            tiles=tiles,
            randomizer=randomizer,
        )

    def __str__(self):
        return f'bag[{compress_tile_list(self.tiles)}, {self.used_tiles_manager}]'
