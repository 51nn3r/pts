from typing import List, Optional

from azul.simple_types import Tile, Points


class WallLine:
    def __init__(self, length: int, tile_types: List[Tile]):
        self.tileTypes: List[Tile] = tile_types
        self._contents: List[bool] = []
        self._lenght: int = length
        for i in range(0, self._lenght):
            self._contents.append(False)

    def canPut(self, tile: Tile) -> bool:
        for i in range(0, self._lenght):
            if not self._contents[i] and self.tileTypes[i] == tile:
                return True
        return False

    def getTiles(self) -> List[Optional[Tile]]:
        r: List[Optional[Tile]] = []
        for i in range(0, self._lenght):
            if self._contents[i]:
                r.append(self.tileTypes[i])
            else:
                r.append(None)
        return r

    def putTile(self, tile: Tile) -> Points:
        for i in range(0, self._lenght):
            if not self._contents[i] and self.tileTypes[i] == tile:
                self._contents[i] = True
                break

            # TODO: make it calculate and return points
