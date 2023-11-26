import unittest

from azul.bag import Bag
from azul.used_tiles_manager import UsedTilesManager

from azul.settings import TILES_COUNT


class TestUsedTilesManager(unittest.TestCase):
    def test_take(self):
        manager = UsedTilesManager()
        bag = Bag(manager)
        tiles = bag.take(1337)
        self.assertEqual(len(tiles), TILES_COUNT)
        self.assertEqual(len(bag.take(1)), 0)
        manager.give(tiles)
        n_tiles = 4
        tiles = bag.take(n_tiles)
        self.assertEqual(len(tiles), n_tiles)


if __name__ == '__main__':
    unittest.main()
