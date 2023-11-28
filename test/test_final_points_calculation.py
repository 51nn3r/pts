import unittest
from typing import List, Optional
from azul.settings import TILES_IN_WALL, WALL_LINES_COUNT
from azul.simple_types import Tile, TILE_TYPES
from azul.final_points_calculation import FinalPointsCalculation


class TestFinalPointsCalculation(unittest.TestCase):
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
        
    def test_game_finished(self) -> None:

        self.assertEqual(FinalPointsCalculation().getPoints(self.wall).value, 0)
        self.wall[0] = self.fullrow
        self.assertEqual(FinalPointsCalculation().getPoints(self.wall).value, 2)
        self.wall[1] = self.fullrow
        self.assertEqual(FinalPointsCalculation().getPoints(self.wall).value, 4)
        for i in range(TILES_IN_WALL):
            self.wall[i][0] = TILE_TYPES[i]
        self.assertEqual(FinalPointsCalculation().getPoints(self.wall).value, 11)
        for i in range(TILES_IN_WALL):
            self.wall[i][1] = TILE_TYPES[i]
        self.assertEqual(FinalPointsCalculation().getPoints(self.wall).value, 18)
        for i in range(TILES_IN_WALL):
            self.wall[i][2] = Tile("R")
        self.assertEqual(FinalPointsCalculation().getPoints(self.wall).value, 35)



if __name__ == '__main__':

    unittest.main()
