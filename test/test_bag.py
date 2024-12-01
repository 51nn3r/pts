import unittest
from typing import List

from azul.simple_types import TILE_TYPES, Tile
from azul.bag import Bag
from azul.randomizer import Randomizer
from azul.used_tiles_manager import UsedTilesManager


class SimpleRandomizer(Randomizer):
    @staticmethod
    def shuffle_array(arr: List):
        return arr


class TestBag(unittest.TestCase):
    def setUp(self):
        self.randomizer = Randomizer()
        self.bag = Bag.get_start_instance(
            used_tiles_manager=UsedTilesManager(TILE_TYPES * 100),
            randomizer=self.randomizer,
        )

    def test_initial_state(self):
        self.assertTrue(len(self.bag.tiles) > 0)

    def test_take_tiles(self):
        tiles, new_bag = self.bag.take(5)
        self.assertEqual(len(tiles), 5)
        self.assertNotEqual(self.bag.tiles, new_bag.tiles)

    def test_give_used_tiles(self):
        used_tiles = [Tile('B'), Tile('Y')]
        new_bag = self.bag.give_used_tiles(used_tiles)
        all_tiles_count = len(self.bag.tiles + self.bag.used_tiles_manager.used_tiles)
        bag_tiles, _ = self.bag.take(all_tiles_count * 2)
        new_bag_tiles, _ = new_bag.take(all_tiles_count * 2)
        self.assertGreater(len(new_bag_tiles), len(bag_tiles))


if __name__ == '__main__':
    unittest.main()
