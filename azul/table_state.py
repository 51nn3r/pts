from __future__ import annotations

from typing import List
from dataclasses import dataclass

from azul.randomizer import Randomizer
from azul.table_area import TableArea
from azul.bag import Bag

from azul.simple_types import Tile

from azul.settings import PLAYERS_TO_FACTORIES
from azul.used_tiles_manager import UsedTilesManager


@dataclass(frozen=True)
class TableState:
    bag: Bag
    table_area: TableArea
    players_count: int

    def take(
            self,
            source_idx: int,
            idx: int,
    ) -> (List[Tile], TableState):
        tiles, table_area = self.table_area.take(
            source_index=source_idx,
            idx=idx,
        )
        return (
            tiles,
            TableState(
                bag=table_area.bag,
                table_area=table_area,
                players_count=self.players_count,
            ),
        )

    def give_used_tiles(
            self,
            tiles: List[Tile]
    ) -> TableState:
        bag = self.bag.give_used_tiles(tiles)
        return TableState(
            bag=bag,
            table_area=self.table_area.update_bag(bag),
            players_count=self.players_count,
        )

    def start_new_round(self) -> TableState | None:
        if not self.table_area.is_round_end():
            raise "round is not finished"

        table_area = self.table_area.start_new_round()
        if table_area is None:
            return None

        return TableState(
            bag=table_area.bag,
            table_area=table_area,
            players_count=self.players_count,
        )

    @staticmethod
    def get_start_instance(
            players_count: int,
            randomizer: Randomizer
    ) -> TableState:
        if players_count not in PLAYERS_TO_FACTORIES:
            raise "invalid players count"

        bag = Bag.get_start_instance(
            used_tiles_manager=UsedTilesManager.get_start_instance(),
            randomizer=randomizer,
        )

        return TableState(
            bag=bag,
            table_area=TableArea.get_start_instance(bag, PLAYERS_TO_FACTORIES[players_count]),
            players_count=players_count,
        )

    @property
    def factories_count(self) -> int:
        return PLAYERS_TO_FACTORIES[self.players_count]

    @property
    def is_round_end(self) -> bool:
        return self.table_area.is_round_end()
