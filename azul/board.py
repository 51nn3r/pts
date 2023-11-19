from typing import List

from azul.simple_types import Tile, Points
from azul.pattern_line import PatternLine
from azul.wall_line import WallLine

BOARD_HEIGHT: 5  # in the "classic" config there are 5 pattern lines


class Board:
    def __init__(self):
        self.points_: Points = Points(0)
        self._wallLines: List[WallLine] = []
        self._patternLines: List[PatternLine] = []
        for i in range(0, BOARD_HEIGHT - 1):
            self._wallLines[i] = WallLine(BOARD_HEIGHT, [])
            self._patternLines[i] = PatternLine(i, self._wallLines[i])

    def put(self, destinationIdx: int, tiles: List[Tile]):
        if destinationIdx < BOARD_HEIGHT:
            raise "invalid pattern line index"

        self._patternLines[destinationIdx].put(tiles)

    ''' state will look something like this:
    
                            . : . . . . B 
                          . . : . R . . G
                        G . . : . . . . . 
                      B B B . : . . . R .
                    R R . . . : . . . . . 
    '''
    def state(self) -> str:
        r = ""
        for i in range(0, BOARD_HEIGHT - 1):
            r += "  " * i
            r += self._patternLines[i].state() + ": " + self._wallLines[i].state()

        return r

    # TODO: implement finishRound and endGame methods

