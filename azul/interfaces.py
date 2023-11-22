from __future__ import annotations
from typing import List
from azul.simple_types import Tile


class UsedTilesGiveInterface:
    def give(self, tiles: List[Tile]) -> None:
        pass


class GameInterface:
    def take(
            self,
            player_id: int,
            source_id: int,
            tile_representation: str,
            dst: int,
    ) -> bool:
        pass


class ObserverInterface:
    def register_observer(
            self,
            observer: ObserverInterface,
    ) -> None:
        pass

    def cancel_observer(
            self,
            observer: ObserverInterface,
    ) -> None:
        pass
