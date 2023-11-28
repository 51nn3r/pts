import unittest

from azul.game import Game
from azul.simple_types import NORMAL
from azul.simple_types import GAME_FINISHED

from azul.settings import TILES_INDEXES


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
        self.source_ids.insert(0, source_id)
        self.tiles_indices.insert(0, tile_index)
        self.destinations.insert(0, dst)


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

    def test_end_game(self):
        players_count = 4
        game = SimpleGame(players_count)
        game._table_area.start_new_round()

        results = []
        for tile_index in range(1, len(TILES_INDEXES)):
            for player_index in range(1, 5):
                if player_index == 1:
                    game.add_move(1, tile_index, 0)
                else:
                    game.add_move(0, tile_index, 0)

            game._table_area._sources[1]._tiles = [
                TILES_INDEXES[tile_index],
                TILES_INDEXES[(tile_index + 1) % len(TILES_INDEXES)],
                TILES_INDEXES[(tile_index + 2) % len(TILES_INDEXES)],
                TILES_INDEXES[(tile_index + 3) % len(TILES_INDEXES)],
            ]
            results.append(game.round())
            game._starting_player = 0

        self.assertEqual(results, [NORMAL] * 4 + [GAME_FINISHED])

        for board in game._boards:
            board.compute_points_finally()

        self.assertEqual(game._boards[0]._points.value, 1 + 1 + 3 + 1 + 5 + 2)
