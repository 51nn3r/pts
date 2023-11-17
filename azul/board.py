from typing import List

from azul.simple_types import Tile, Points
from azul.pattern_line import PatternLine

BOARD_HEIGHT: 5  # in the "classic" config there are 5 pattern lines

class Board:
    def __init__(self):
        self.points_: Points = Points(0)
        self.patternLines: List[PatternLine] = []
        for i in range(0, BOARD_HEIGHT - 1):
            self.patternLines[i] = PatternLine(i)

    def put(self, destinationIdx: int, tiles: List[Tile]):
        if destinationIdx < BOARD_HEIGHT:
            raise "invalid pattern line index"

        self.patternLines[destinationIdx].put(tiles)

    def state(self) -> str:
        r = ""
        for pl in self.patternLines:
            r += pl.state() + "\n"

        return r

    # TODO: implement finishRound and endGame methods

