import unittest

from azul.simple_types import STARTING_PLAYER
from azul.used_tiles_manager import UsedTilesManager
from azul.bag import Bag
from azul.table_center import TableCenter
from azul.factory import Factory

from azul.settings import TILES_IN_FACTORY
from azul.settings import TILE_TYPES


class TestTableCenter(unittest.TestCase):
    def test_add_take(self):
        table_center = TableCenter()
        table_center.start_new_round()
        used_tiles_manager = UsedTilesManager()
        bag = Bag(used_tiles_manager)

        self.assertEqual(len(table_center._tiles), 1)
        tiles_count = 5
        tiles = bag.take(tiles_count)
        table_center.add(tiles)
        self.assertEqual(len(table_center._tiles), tiles_count + 1)
        tiles = table_center.take(1)
        self.assertIn(STARTING_PLAYER, tiles)

    def test_factory_connection(self):
        table_center = TableCenter()
        table_center.start_new_round()
        used_tiles_manager = UsedTilesManager()
        bag = Bag(used_tiles_manager)
        factory = Factory(
            bag=bag,
            table_center=table_center,
        )

        factory.start_new_round()
        factory_tiles = factory.take(1)
        self.assertEqual(len(factory._tiles), 0)

        table_tiles = []
        for i in range(1, len(TILE_TYPES) + 1):
            table_tiles.extend(table_center.take(i))

        self.assertIn(STARTING_PLAYER, table_tiles)
        self.assertEqual(len(table_tiles) + len(factory_tiles), TILES_IN_FACTORY + 1)
