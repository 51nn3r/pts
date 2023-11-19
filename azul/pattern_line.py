from typing import List

from azul.simple_types import Tile
from azul.wall_line import WallLine
from azul.floor import Floor


class PatternLine:
    def __init__(
            self,
            capacity: int,
            wall_line: WallLine,
            floor: Floor
    ):
        self.capacity = capacity
        self._wline: WallLine = wall_line
        self._tile_type: Tile
        self._contents: int = 0
        self._floor = floor
        # there is no reference for UsedTiles bc I didn't get why is it there in the first place
        # I guess TODO: make reference for UsedTiles

    ''' state will be in that format:
            if capacity == 5, self._tile_type == Tile(RED)
            
                R R . . . 
                
    '''
    def state(self) -> str:
        r = ""
        for t in range(0, self._contents):
            r += self._tile_type.__str__() + " "

        for t in range(0, self.capacity - self._contents):
            r += ". "

        return r

    def put(self, tiles: List[Tile]):
        for tile in tiles:
            if self._contents == 0:
                self._tile_type = tile
                self._contents = 1
            elif self._contents >= self.capacity:
                self._floor.put([tile])
            elif self._tile_type == tile:
                self._contents += 1
            else:
                raise "incorrect tile type"

        if self._contents >= self.capacity:
            self._wline.putTile(self._tile_type)
            self._contents = 0
            # No need to reset tile type: it will be reset anyway bc of self._contents = 0
