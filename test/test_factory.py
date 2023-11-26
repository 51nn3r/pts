import unittest

from azul.simple_types import RED
from azul.factory import Factory
from azul.used_tiles_manager import UsedTilesManager
from azul.bag import Bag
from azul.table_center import TableCenter

from azul.settings import TILES_IN_FACTORY
from azul.settings import TILES_INDEXES_REVERSED


class TestFactory(unittest.TestCase):
    def test_take(self):
        used_tiles_manager = UsedTilesManager()
        bag = Bag(used_tiles_manager)
        table_center = TableCenter()
        factory = Factory(
            bag=bag,
            table_center=table_center,
        )

        factory.start_new_round()
        tiles_count = factory._tiles.count(RED)
        red_index = TILES_INDEXES_REVERSED[RED.__str__()]
        tiles = factory.take(red_index)
        self.assertEqual(len(tiles), tiles_count)
        self.assertEqual(len(factory._tiles), 0)

    def test_start_new_round(self):
        used_tiles_manager = UsedTilesManager()
        bag = Bag(used_tiles_manager)
        table_center = TableCenter()
        factory = Factory(
            bag=bag,
            table_center=table_center,
        )

        self.assertEqual(len(factory._tiles), 0)
        factory.start_new_round()
        self.assertEqual(len(factory._tiles), TILES_IN_FACTORY)


if __name__ == '__main__':
    unittest.main()
