import unittest
from typing import List, Optional
from azul.simple_types import Tile
from azul.game_finished import GameFinished


class TestGameFinished(unittest.TestCase):
    def setUp(self) -> None:
        self.wall: List[List[Optional[Tile]]] = []
        for _ in range(5):
            row: List[Optional[Tile]] = []
            for _ in range(5):
                row.append(None)
            self.wall.append(row)
        self.fullrow : List[Optional[Tile]] = []
        for _ in range(5):
            self.fullrow.append(Tile("B"))
        self.partrow: List[Optional[Tile]] = []
        for i in range(5):
            if i <= 2:
                self.partrow.append(Tile("B"))
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
