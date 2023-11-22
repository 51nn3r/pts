from typing import List

from azul.simple_types import Tile
from azul.simple_types import FinishRoundResult
from azul.simple_types import NORMAL
from azul.simple_types import GAME_FINISHED
from azul.interfaces import GameInterface
from azul.used_tiles_manager import UsedTilesManager
from azul.bag import Bag
from azul.table_area import TableArea
from azul.board import Board
from azul.game_observer import GameObserver


class Game(GameInterface):
    _players_count: int
    _used_tiles_manager: UsedTilesManager
    _bag: Bag
    _table_area: TableArea
    _boards: List[Board]
    _observer: GameObserver

    def __init__(self, players_count: int):
        self._players_count = players_count
        self._used_tiles_manager = UsedTilesManager()
        self._bag = Bag(self._used_tiles_manager)
        self._table_area = TableArea(
            players_count=players_count,
            bag=self._bag,
        )
        self._boards: List[Board] = []
        for _ in range(players_count):
            self._boards.append(Board(self._used_tiles_manager))

        self._observer = GameObserver()

    def game_loop(self):
        while self.round() is NORMAL:
            pass

    def round(self) -> FinishRoundResult:
        for player_idx in range(self._players_count):
            print(f'[*] {player_idx} player\'s turn')
            source_id = int(input('[>] input source id: '))
            tile_idx = int(input('[>] input tile index: '))
            dst = int(input('[>] input destination: '))

            self.turn(
                player_idx=player_idx,
                source_id=source_id,
                tile_idx=tile_idx,
                dst=dst,
            )

        return self.finish_round()

    def turn(
            self,
            player_idx: int,
            source_id: int,
            tile_idx: int,
            dst: int,
    ):
        tiles: List[Tile] = self._table_area.take(source_id, tile_idx)
        self._boards[player_idx].put(dst, tiles)

    def finish_round(self) -> FinishRoundResult:
        finished = False

        for player_idx in range(self._players_count):
            round_result = self._boards[player_idx].finish_round()
            if round_result == GAME_FINISHED:
                finished = True

        if finished:
            return GAME_FINISHED

        return NORMAL
