from typing import List

from azul.simple_types import Tile


class PatternLine:
    def __init__(self, capacity: int):  # NEED TO ADD wall_line: WallLine
        self.capacity = capacity
        # self.wline: WallLine = WallLine()
        self._tile_type : str = ""
        self._contents : int = 0

    def state(self) -> str:
        r = ""
        for t in range(0, self._contents):
            r += " " + self._tile_type + " "

        for t in range(0, self.capacity - self._contents):
            r += " . "

        return r

    def put(self, tiles: List[Tile]):
        for tile in tiles:
            if self._contents == 0:
                self._tile_type = tile
                self._contents = 1
            elif self._tile_type == tile:
                self._contents += 1
            else:
                raise "incorrect tile type"

            if self._contents >= self.capacity:
                # self.wline.putTile(Tile(_tile_type))
                self._contents = 0
                self._tile_type = ""

        # TODO: MAKE TILES DROP TO THE FLOOR
