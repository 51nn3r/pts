from __future__ import annotations

from dataclasses import dataclass

from typing import List

from azul.interfaces import UsedTilesGiveInterface
from azul.simple_types import Tile
from azul.simple_types import compress_tile_list


@dataclass(frozen=True)
class UsedTilesManager(UsedTilesGiveInterface):
    used_tiles: List[Tile]

    def give(self, tiles: List[Tile]) -> UsedTilesManager:
        return UsedTilesManager(self.used_tiles + tiles)

    def take_all(self) -> (List[Tile], UsedTilesManager):
        used_tales = self.used_tiles.copy()

        return (
            used_tales,
            UsedTilesManager([]),
        )

    def state(self):
        return self.__str__()

    @staticmethod
    def get_start_instance() -> UsedTilesManager:
        return UsedTilesManager([])

    def __str__(self):
        return compress_tile_list(self.used_tiles)
