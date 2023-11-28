import unittest
from azul.settings import TILES_IN_WALL, WALL_LINES_COUNT, WALL_LINE,points_pattern
from azul.simple_types import Tile
from azul.wall_line import WallLine
from azul.pattern_line import PatternLine
from azul.floor import Floor
from azul.used_tiles_manager import UsedTilesManager


class TestPatternLine(unittest.TestCase):

    def setUp(self) -> None:

        wallLines = []
        self.patternLines = []
        wallLines.append(WallLine(WALL_LINE.copy()))
        self.used_tiles_manager = UsedTilesManager()
        self.floor = Floor(points_pattern,self.used_tiles_manager)
        self.patternLines.append(PatternLine(1,wallLines[0],self.floor,self.used_tiles_manager))
        for i in range(WALL_LINES_COUNT-1):
            wallLine = WallLine(WALL_LINE.copy()[TILES_IN_WALL-1-i:]+WALL_LINE.copy()[:TILES_IN_WALL-1-i])
            
            self.patternLines.append(PatternLine(i+2,wallLine,self.floor,self.used_tiles_manager))
            wallLines.append(wallLine)
            wallLines[i].link(wallLines[i]._up or None,wallLine)
            wallLine._up = wallLines[i]


    def test_pattern_line(self) -> None:
        self.patternLines[0].put([Tile("R")])
        self.assertEqual(self.patternLines[0].finish_round().value, 1)

        self.patternLines[1].put([Tile("Y"),Tile("Y")])
        self.assertEqual(self.patternLines[1].finish_round().value, 2)

        self.patternLines[2].put([Tile("L"),Tile("L"),Tile("L")])
        self.assertEqual(self.patternLines[2].finish_round().value, 1)

        self.patternLines[2].put([Tile("G"),Tile("G"),Tile("G")])
        self.assertEqual(self.patternLines[2].finish_round().value, 2)

        self.patternLines[2].put([Tile("B"),Tile("B"),Tile("B")])
        self.assertEqual(self.patternLines[2].finish_round().value, 6)

        self.patternLines[2].put([Tile("Y"),Tile("Y"),Tile("Y"),Tile("Y")])
        self.assertEqual(self.patternLines[2].finish_round().value, 4)

        self.assertEqual(self.floor._tiles[0], Tile("Y"))


if __name__ == '__main__':

    unittest.main()
