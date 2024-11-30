from typing import List

from azul.simple_types import FinishRoundResult
from azul.simple_types import NORMAL
from azul.simple_types import GAME_FINISHED
from azul.interfaces import GameInterface
from azul.table_state import TableState
from azul.used_tiles_manager import UsedTilesManager
from azul.bag import Bag
from azul.board import Board
from azul.game_observer import GameObserver
from azul.randomizer import Randomizer


class Game(GameInterface):
    _starting_player: int
    _players_count: int
    _used_tiles_manager: UsedTilesManager
    _bag: Bag
    _table_state: TableState
    _boards: List[Board]
    _observer: GameObserver

    def __init__(self, players_count: int):
        self._starting_player = 0
        self._players_count = players_count
        self._used_tiles_manager = UsedTilesManager.get_start_instance()
        self._table_state = TableState.get_start_instance(
            players_count=players_count,
            randomizer=Randomizer(),
        )

        self._boards: List[Board] = []
        self._observer = GameObserver()
        for _ in range(players_count):
            self._boards.append(Board(self._used_tiles_manager))
            self._observer.register_observer(GameObserver())

    def game_loop(self):
        self._table_state.start_new_round()

        while self.round() is NORMAL:
            if self._table_state.is_round_end:
                self._table_state = self._table_state.start_new_round()

        for board in self._boards:
            board.compute_points_finally()

    def round(self) -> FinishRoundResult:
        next_starting_player = None

        for _player_idx in range(self._players_count):
            player_idx = (_player_idx + self._starting_player) % self._players_count
            self._observer.notify(f'[*] {player_idx} player\'s turn')
            source_id = self.read_source_id()
            tile_idx = self.read_tile_index()
            dst = self.read_dst()

            if self.turn(
                    player_idx=player_idx,
                    source_id=source_id,
                    tile_idx=tile_idx,
                    dst=dst,
            ):
                next_starting_player = player_idx

        if next_starting_player is not None:
            self._starting_player = next_starting_player

        return self.finish_round()

    def turn(
            self,
            player_idx: int,
            source_id: int,
            tile_idx: int,
            dst: int,
    ) -> bool:
        tiles, self._table_state = self._table_state.take(source_id, tile_idx)
        return self._boards[player_idx].put(dst, tiles)

    def start_round(self):
        self._table_state = self._table_state.start_new_round()

    def finish_round(self) -> FinishRoundResult:
        finished = False

        for player_idx in range(self._players_count):
            round_result = self._boards[player_idx].finish_round()
            if round_result == GAME_FINISHED:
                finished = True

        if finished:
            return GAME_FINISHED

        return NORMAL

    def read_source_id(self) -> int:
        """ method to overwrite """
        pass

    def read_tile_index(self) -> int:
        """ method to overwrite """
        pass

    def read_dst(self) -> int:
        """ method to overwrite """
        pass
