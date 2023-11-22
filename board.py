from typing import List

from azul.simple_types import Points
from azul.simple_types import Tile
from azul.simple_types import FinishRoundResult
from azul.simple_types import NORMAL
from azul.simple_types import GAME_FINISHED
from azul.pattern_line import PatternLine
from azul.wall_line import WallLine
from azul.used_tiles_manager import UsedTilesManager
from azul.floor import Floor
from azul.utils import define_board_wall_lines

from azul.settings import points_pattern
from azul.settings import WALL_LINES_COUNT


class Board:
    _points: Points
    _pattern_lines: List[PatternLine]
    _wall_lines: List[WallLine]
    _used_tiles_manager: UsedTilesManager
    _floor: Floor

    def __init__(
            self,
            used_tiles_manager: UsedTilesManager()
    ):
        self._used_tiles_manager = used_tiles_manager
        self._floor = Floor(points_pattern.copy(), used_tiles_manager)

        for capacity, wall_line in zip(range(1, WALL_LINES_COUNT + 1), define_board_wall_lines()):
            pattern_line = PatternLine(
                capacity=capacity,
                wall_line=wall_line,
                floor=self._floor,
                used_tiles=self._used_tiles_manager,
            )

            self._pattern_lines.append(pattern_line)
            self._wall_lines.append(wall_line)

    def put(
            self,
            dst_idx: int,
            tiles: List[Tile],
    ):
        if dst_idx >= len(self._pattern_lines):
            raise "invalid dst index"

        self._pattern_lines[dst_idx].put(tiles)

    def finish_round(self) -> FinishRoundResult:
        finished = False
        for pattern_line in self._pattern_lines:
            self._points = Points.sum(points_list=[
                self._points,
                pattern_line.finish_round(),
            ])
            finished = finished or pattern_line.finished

        if finished:
            return GAME_FINISHED

        return NORMAL

    def state(self) -> str:
        return self.__str__()
