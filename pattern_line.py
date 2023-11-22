from typing import List

from azul.simple_types import Tile
from azul.wall_line import WallLine
from azul.floor import Floor
from azul.used_tiles_manager import UsedTilesManager
from azul.simple_types import Points


class PatternLine:
    _capacity: int
    _wall_line: WallLine
    _floor: Floor
    _used_tiles: UsedTilesManager
    _tiles: List[Tile]

    def __init__(
            self,
            capacity: int,
            wall_line: WallLine,
            floor: Floor,
            used_tiles: UsedTilesManager,
    ):
        self._capacity = capacity
        self._wall_line = wall_line
        self._floor = floor
        self._used_tiles = used_tiles

    def put(
            self,
            tiles: List[Tile]
    ):
        if not self._wall_line.can_put_tile(tiles[-1]):
            self._floor.put(tiles.copy())
            return

        empty_places = self._capacity - len(self._tiles)
        self._tiles.extend(tiles[:empty_places].copy())

        extra_tiles = tiles[empty_places:]
        if extra_tiles:
            self._floor.put(extra_tiles.copy())

    def finish_round(self) -> Points:
        if len(self._tiles) < self._capacity:
            return Points(0)

        points: Points = self._wall_line.put_tile(self._tiles[-1])
        self._used_tiles.give(self._tiles[:-1].copy())

        return points

    @property
    def finished(self) -> bool:
        return self._wall_line.is_fool

    def state(self):
        return self.__str__()
