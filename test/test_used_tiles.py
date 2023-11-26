import unittest

from azul.bag import Bag
from azul.used_tiles_manager import UsedTilesManager


class TestUsedTilesManager(unittest.TestCase):
    def test_take(self):
        manager = UsedTilesManager()
        bag = Bag(manager)
        tiles = bag.take(4)
        manager.give(tiles)
        tmp_tiles = bag.take(5)
        tiles.extend(tmp_tiles)
        manager.give(tmp_tiles)
        self.assertEqual(manager.take_all(), tiles)
        self.assertEqual(manager.take_all(), [])


if __name__ == '__main__':
    unittest.main()
