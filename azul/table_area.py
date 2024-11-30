from __future__ import annotations

from dataclasses import dataclass
from typing import List

from azul.simple_types import Tile, STARTING_PLAYER
from azul.bag import Bag
from azul.tile_source import TileSource
from azul.table_center import TableCenter
from azul.factory import Factory

from azul.settings import TILES_IN_FACTORY


@dataclass(frozen=True)
class TableArea:
    bag: Bag
    sources: List[TileSource]

    def take(
            self,
            source_index: int,
            idx: int
    ) -> (List[Tile], TableArea):

        if source_index >= len(self.sources):
            raise "invalid source index"

        tiles, other_tiles = self.sources[source_index].take(idx)
        if source_index == 0:
            # TableCenter
            sources = [TableCenter(other_tiles)] + self.sources[1:]
            bag = self.bag.give_used_tiles(other_tiles)
        else:
            # Factory
            sources = self.sources[:source_index] + [Factory([])] + self.sources[source_index + 1:]
            bag = self.bag
            sources[0] = TableCenter(self.table_center.tiles + other_tiles)

        return (
            tiles,
            TableArea(
                bag=bag,
                sources=sources,
            )
        )

    def update_bag(
            self,
            bag: Bag,
    ) -> TableArea:
        return TableArea(
            bag=bag,
            sources=self.sources,
        )

    def is_round_end(self) -> bool:
        for source in self.sources:
            if not source.is_empty():
                return False

        return True

    def start_new_round(
            self,
    ) -> TableArea | None:
        tiles_count = (len(self.sources) - 1) * TILES_IN_FACTORY
        tiles, bag = self.bag.take(tiles_count)

        if len(tiles) != tiles_count:
            return None

        sources = [TableCenter([STARTING_PLAYER])]
        for source_idx in range(1, len(self.sources)):
            sources.append(Factory(tiles[:TILES_IN_FACTORY]))
            tiles = tiles[TILES_IN_FACTORY:]

        return TableArea(
            bag=bag,
            sources=sources,
        )

    def state(self) -> str:
        return self.__str__()

    @staticmethod
    def get_start_instance(
            bag: Bag,
            factories_count: int,
    ) -> TableArea:
        sources = [TableCenter([])]
        for source_idx in range(factories_count):
            sources.append(Factory([]))

        table_area = TableArea(
            bag=bag,
            sources=sources,
        )

        return table_area

    @property
    def table_center(self) -> TableCenter | None:
        if len(self.sources) == 0:
            return None

        table_center = self.sources[0]
        if not isinstance(table_center, TableCenter):
            raise "tile source with index 0 must be a table center"

        return table_center
