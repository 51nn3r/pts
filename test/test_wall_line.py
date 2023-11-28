import unittest
from azul.settings import TILES_IN_WALL, WALL_LINES_COUNT, WALL_LINE
from azul.simple_types import Tile
from azul.wall_line import WallLine


class TestGameFinished(unittest.TestCase):
    def setUp(self) -> None:

        self.wallLines = []
        self.wall = WallLine(WALL_LINE.copy())
        self.wallLines.append(self.wall)

        for i in range(WALL_LINES_COUNT-1):
            wallLine = WallLine(WALL_LINE.copy()[TILES_IN_WALL-1-i:]+WALL_LINE.copy()[:TILES_IN_WALL-1-i])
            self.wallLines.append(wallLine)
            self.wallLines[i].link(self.wallLines[i]._up or None,wallLine)
            wallLine._up = self.wallLines[i]

        for i in range(WALL_LINES_COUNT):
            print(self.wallLines[i]._tile_types)


    def test_game_finished(self) -> None:
        self.assertEqual(self.wallLines[0].can_put_tile(Tile("R")), True)
        self.assertEqual(self.wallLines[0].put_tile(Tile("R")).value, 1)
        self.assertEqual(self.wallLines[0].can_put_tile(Tile("R")), False)
        self.assertEqual(self.wallLines[1].put_tile(Tile("Y")).value, 2)
        self.assertEqual(self.wallLines[2].put_tile(Tile("G")).value, 1)
        self.assertEqual(self.wallLines[2].can_put_tile(Tile("B")), True)
        self.assertEqual(self.wallLines[2].put_tile(Tile("B")).value, 5)
        self.assertEqual(self.wallLines[2].can_put_tile(Tile("B")), False)
        self.assertEqual(self.wallLines[2].put_tile(Tile("Y")).value, 3)
        self.assertEqual(self.wallLines[1].put_tile(Tile("R")).value, 4)
        self.assertEqual(self.wallLines[4].put_tile(Tile("L")).value, 1)
        self.assertEqual(self.wallLines[3].put_tile(Tile("G")).value, 5)



if __name__ == '__main__':

    unittest.main()
