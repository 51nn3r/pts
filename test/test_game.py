import unittest

from azul.game import Game
from azul.used_tiles_manager import UsedTilesManager
from azul.bag import Bag

from azul.settings import TILES_IN_FACTORY
from azul.settings import TILES_INDEXES
from azul.settings import TILES_INDEXES_REVERSED


class SimpleGame(Game):
    def __init__(self, players_count):
        super().__init__(players_count)

        self.source_ids = []
        self.tiles_indices = []
        self.destinations = []

    def read_source_id(self, ) -> int:
        if not self.source_ids:
            raise "no source ids"

        return self.source_ids.pop(-1)

    def read_tile_index(self) -> int:
        if not self.tiles_indices:
            raise "no indices"

        return self.tiles_indices.pop(-1)

    def read_dst(self) -> int:
        if not self.destinations:
            raise "no destinations"

        return self.destinations.pop(-1)

    def add_move(self, source_id, tile_index, dst):
        self.source_ids.append(source_id)
        self.tiles_indices.append(tile_index)
        self.destinations.append(dst)


class TestGame(unittest.TestCase):
    def test_put1(self):
        players_count = 4
        game = SimpleGame(players_count)

        for i in range(1, 5):
            game.add_move(i, i, i)

        game._table_area.start_new_round()
        game._table_area._sources[1]._tiles = [
            TILES_INDEXES[3],
            TILES_INDEXES[2],
            TILES_INDEXES[2],
            TILES_INDEXES[4],
        ]

        game.turn(0, 1, 3, 0)
        game.turn(0, 0, 2, 1)

        self.assertEqual(game._boards[0]._pattern_lines[0]._tiles, [TILES_INDEXES[3]])

        game._boards[0].finish_round()
        self.assertEqual(game._boards[0]._points.value, 1 + 2 - 1)

        game._table_area._sources[0]._tiles.clear()
        game._table_area._sources[0].start_new_round()

        game._table_area._sources[1]._tiles = [
            TILES_INDEXES[2],
            TILES_INDEXES[4],
            TILES_INDEXES[4],
            TILES_INDEXES[1],
        ]

        game.turn(0, 1, 2, 0)
        game.turn(0, 0, 4, 1)

        game._boards[0].finish_round()
        self.assertEqual(game._boards[0]._points.value, 1 + 2 - 1 + 2 + 3 - 1)

    def test_put2(self):
        players_count = 4
        game = SimpleGame(players_count)

        for i in range(1, 5):
            game.add_move(i, i, i)

        game._table_area.start_new_round()
        game._table_area._sources[1]._tiles = [
            TILES_INDEXES[2],
            TILES_INDEXES[3],
            TILES_INDEXES[3],
            TILES_INDEXES[1],
        ]

        game.turn(0, 1, 2, 0)
        game._boards[0].finish_round()
        self.assertEqual(game._boards[0]._points.value, 1)

        game._table_area._sources[0]._tiles.clear()
        game._table_area._sources[0].start_new_round()

        game._table_area._sources[1]._tiles = [
            TILES_INDEXES[5],
            TILES_INDEXES[3],
            TILES_INDEXES[3],
            TILES_INDEXES[2],
        ]

        game._table_area._sources[2]._tiles = [
            TILES_INDEXES[2],
            TILES_INDEXES[3],
            TILES_INDEXES[1],
            TILES_INDEXES[1],
        ]

        game.turn(0, 2, 2, 0)
        game.turn(0, 1, 5, 0)
        game.turn(0, 0, 1, 1)
        game._boards[0].finish_round()
        self.assertEqual(game._boards[0]._points.value, 1 + 1 + 2 - 1 - 1)
