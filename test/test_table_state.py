import unittest

from typing import List

from azul.bag import Bag
from azul.settings import TILES_INDEXES
from azul.simple_types import TILE_TYPES
from azul.table_area import TableArea
from azul.table_center import TableCenter
from azul.table_state import TableState
from azul.randomizer import Randomizer
from azul.used_tiles_manager import UsedTilesManager


class SimpleRandomizer(Randomizer):
    @staticmethod
    def shuffle_array(arr: List):
        return arr


class Test(unittest.TestCase):
    def test_table_center_add_tiles(self):
        table_state = TableState.get_start_instance(
            players_count=2,
            randomizer=SimpleRandomizer(),
        ).start_new_round()
        factory = table_state.table_area.sources[1]
        factory_tiles = factory.tiles
        table_tiles_count = len(factory_tiles) - factory_tiles.count(TILES_INDEXES[1]) + 1
        tiles, table_state = table_state.take(1, 1)
        self.assertEqual(len(table_state.table_area.table_center.tiles), table_tiles_count)

        factory = table_state.table_area.sources[2]
        factory_tiles = factory.tiles
        table_tiles_count += len(factory_tiles) - factory_tiles.count(TILES_INDEXES[2])
        tiles, table_state = table_state.take(2, 2)
        self.assertEqual(len(table_state.table_area.table_center.tiles), table_tiles_count)

    def test_table_center_get_tiles(self):
        tmp_state = TableState.get_start_instance(2, SimpleRandomizer())
        tmp_state.start_new_round()

        factories = tmp_state.table_area.sources[1:]
        my_table_center = TableCenter(TILE_TYPES[1:])
        bag = Bag(
            used_tiles_manager=UsedTilesManager.get_start_instance(),
            tiles=TILE_TYPES[:2],
            randomizer=SimpleRandomizer()
        )

        table_state = TableState(
            bag=bag,
            table_area=TableArea(
                bag=bag,
                sources=[my_table_center] + factories
            ),
            players_count=2,
        )

        self.assertEqual(len(table_state.bag.tiles), len(TILE_TYPES[:2]))
        tiles, table_state = table_state.take(0, 2)
        self.assertEqual(tiles, [TILES_INDEXES[2]])

        bag = table_state.bag
        tiles_from_bag, bag = bag.take(1337)
        self.assertEqual(tiles_from_bag, TILE_TYPES)

        table_state = table_state.give_used_tiles(tiles_from_bag)
        tiles, bag = table_state.bag.take(1337)
        self.assertEqual(tiles, TILE_TYPES * 2)
        self.assertEqual(bag.tiles, [])
