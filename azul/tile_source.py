from typing import List

from azul.simple_types import Tile

from azul.settings import TILES_INDEXES


class TileSource:
    _tiles: List[Tile]

    def __init__(self):
        self._tiles: List[Tile] = []

    def take(self, idx: int) -> List[Tile]:
        if idx not in TILES_INDEXES or idx == 0:
            raise "invalid tile index"

        tile_representation = TILES_INDEXES[idx]
        tiles = []

        while Tile(tile_representation) in self._tiles:
            self._tiles.remove(Tile(tile_representation))
            tiles.append(Tile(tile_representation))

        return tiles

    def is_empty(self) -> bool:
        return not self._tiles

    def start_new_round(self) -> None:
        pass

    def state(self) -> str:
        return self.__str__()
