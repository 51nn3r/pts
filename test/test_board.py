import unittest

from azul.simple_types import Tile
from azul.used_tiles_manager import UsedTilesManager
from azul.board import Board


class TestBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.used_tiles_manager = UsedTilesManager()
        self.board = Board(self.used_tiles_manager)


    def test_board(self) -> None:
        self.board.put(0,[Tile("B")])
        self.board.finish_round()
        self.assertEqual(self.board._points.value, 1)
        
        self.board.put(1,[Tile("G"),Tile("G")])
        self.board.finish_round()
        self.assertEqual(self.board._points.value, 3)

        self.board.put(2,[Tile("L"),Tile("L"),Tile("L")])
        self.board.finish_round()
        self.assertEqual(self.board._points.value, 6)

        self.board.put(3,[Tile("R"),Tile("R"),Tile("R"),Tile("R")])
        self.board.finish_round()
        self.assertEqual(self.board._points.value, 10)

        self.board.put(4,[Tile("Y"),Tile("Y"),Tile("Y"),Tile("Y"),Tile("Y")])
        self.board.finish_round()
        self.assertEqual(self.board._points.value, 15)

        self.board.put(0,[Tile("Y")])
        self.board.finish_round()
        self.assertEqual(self.board._points.value, 17)

        self.board.put(0,[Tile("R")])
        self.board.finish_round()
        self.assertEqual(self.board._points.value, 20)

        self.board.put(0,[Tile("L")])
        self.assertEqual(self.board.finish_round().__str__(),"N")

        self.assertEqual(self.board._points.value, 24)

        self.board.put(0,[Tile("G"),Tile("G"),Tile("G")])
        self.assertEqual(self.board.finish_round().__str__(),"F")

        self.assertEqual(self.board._points.value, 27)

        print(self.board.compute_points_finally())
        self.assertEqual(self.board._points.value, 36)


if __name__ == '__main__':

    unittest.main()
