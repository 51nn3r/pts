from typing import List

from azul.simple_types import Points
from azul.simple_types import Tile
from azul.simple_types import FinishRoundResult
from azul.simple_types import NORMAL
from azul.simple_types import GAME_FINISHED
from azul.simple_types import STARTING_PLAYER
from azul.pattern_line import PatternLine
from azul.wall_line import WallLine
from azul.used_tiles_manager import UsedTilesManager
from azul.floor import Floor
from azul.final_points_calculation import FinalPointsCalculation
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
            used_tiles_manager: UsedTilesManager
    ):
        self._points = Points(0)
        self._pattern_lines: List[PatternLine] = []
        self._wall_lines: List[WallLine] = []
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
    ) -> bool:
        if dst_idx >= len(self._pattern_lines):
            raise "invalid dst index"

        starting_next = False
        _tiles = tiles.copy()
        if STARTING_PLAYER in _tiles:
            _tiles.remove(STARTING_PLAYER)
            self._floor.put([STARTING_PLAYER])
            starting_next = True

        self._pattern_lines[dst_idx].put(_tiles)

        return starting_next

    def finish_round(self) -> FinishRoundResult:
        finished = False
        points: Points = Points(0)
        for pattern_line in self._pattern_lines:
            points = Points.sum(points_list=[
                points,
                pattern_line.finish_round(),
            ])
            finished = finished or pattern_line.finished

        floor_points = self._floor.finish_round().reverse

        points = points.sum([points, floor_points])
        if points.value > 0:
            self._points = self._points.sum([self._points, points])

        if finished:
            return GAME_FINISHED

        return NORMAL

    def compute_points_finally(self) -> Points:
        final_points_calculation = FinalPointsCalculation()
        self._points = self._points.sum([
            self._points,
            final_points_calculation.getPoints(self.as_matrix)
        ])

        return self._points

    @property
    def as_matrix(self):
        return [wall_line.tiles for wall_line in self._wall_lines]

    def state(self) -> str:
        return self.__str__()
