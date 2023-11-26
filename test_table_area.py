import unittest

from azul.simple_types import RED
from azul.table_area import TableArea
from azul.used_tiles_manager import UsedTilesManager
from azul.bag import Bag

from azul.settings import TILES_IN_FACTORY
from azul.settings import TILES_INDEXES_REVERSED


class TestTableArea(unittest.TestCase):
    def test_take(self):
        used_tiles_manager = UsedTilesManager()
        bag = Bag(used_tiles_manager)

        players_count = 4
        table_area = TableArea(
            players_count=players_count,
            bag=bag,
        )

        table_area.start_new_round()

        tiles_count = table_area._sources[1]._tiles.count(RED)
        red_index = TILES_INDEXES_REVERSED[RED.__str__()]
        tiles = table_area.take(1, red_index)
        self.assertEqual(len(tiles), tiles_count)
        self.assertGreater(len(table_area._sources[0]._tiles), 0)
        self.assertEqual(len(table_area._sources[0]._tiles) + len(tiles), TILES_IN_FACTORY + 1)
