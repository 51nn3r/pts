import unittest
from typing import List, Optional
from azul.simple_types import Tile, TILE_TYPES
from azul.game_finished import GameFinished
from azul.settings import TILES_IN_WALL, WALL_LINES_COUNT

class TestGameFinished(unittest.TestCase):
    def setUp(self) -> None:
        self.wall: List[List[Optional[Tile]]] = []
        for _ in range(WALL_LINES_COUNT):
            row: List[Optional[Tile]] = []
            for _ in range(TILES_IN_WALL):
                row.append(None)
            self.wall.append(row)
        self.fullrow : List[Optional[Tile]] = []
        for i in range(TILES_IN_WALL):
            self.fullrow.append(TILE_TYPES[i])
        self.partrow: List[Optional[Tile]] = []
        for i in range(TILES_IN_WALL):
            if i <= 2:
                self.partrow.append(TILE_TYPES[i])
            else:
                self.partrow.append(None)
        
    def test_game_finished(self) -> None:

        self.assertEqual(GameFinished().game_finished(self.wall).__str__(), "N")
        self.wall[0] = self.partrow
        self.assertEqual(GameFinished().game_finished(self.wall).__str__(), "N")
        self.wall[1] = self.partrow
        self.assertEqual(GameFinished().game_finished(self.wall).__str__(), "N")
        self.wall[2] = self.partrow
        self.assertEqual(GameFinished().game_finished(self.wall).__str__(), "N")
        self.wall[3] = self.fullrow
        self.assertEqual(GameFinished().game_finished(self.wall).__str__(), "F")
        self.wall[3] = self.partrow
        self.assertEqual(GameFinished().game_finished(self.wall).__str__(), "N")
        self.wall[4] = self.fullrow
        self.assertEqual(GameFinished().game_finished(self.wall).__str__(), "F")



if __name__ == '__main__':

    unittest.main()
