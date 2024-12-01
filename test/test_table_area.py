import unittest
from typing import List

from azul.simple_types import TILE_TYPES
from azul.table_area import TableArea
from azul.bag import Bag
from azul.randomizer import Randomizer
from azul.used_tiles_manager import UsedTilesManager


class SimpleRandomizer(Randomizer):
    @staticmethod
    def shuffle_array(arr: List):
        return arr


class TestTableArea(unittest.TestCase):
    def setUp(self):
        self.randomizer = SimpleRandomizer()
        self.bag = Bag(
            used_tiles_manager=UsedTilesManager.get_start_instance(),
            tiles=TILE_TYPES * 100,
            randomizer=self.randomizer,
        )

        self.factories_count = 5
        self.table_area = TableArea.get_start_instance(
            bag=self.bag,
            factories_count=self.factories_count,
        )

    def test_initial_state(self):
        self.assertEqual(len(self.table_area.sources), self.factories_count + 1)
        self.assertTrue(all(source.is_empty() for source in self.table_area.sources))

    def test_take_from_source(self):
        table_area = self.table_area.start_new_round()
        tiles, new_area = table_area.take(source_index=0, idx=1)
        self.assertTrue(len(tiles) > 0)
        self.assertNotEqual(table_area, new_area)

    def test_round_end(self):
        self.assertTrue(self.table_area.is_round_end())

    def test_start_new_round(self):
        new_area = self.table_area.start_new_round()
        self.assertIsNotNone(new_area)


if __name__ == '__main__':
    unittest.main()
