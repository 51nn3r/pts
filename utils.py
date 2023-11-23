from typing import List

from wall_line import WallLine

from settings import WALL_LINES_COUNT
from settings import WALL_LINE


def define_board_wall_lines() -> List[WALL_LINE]:
    board = []

    for i in range(WALL_LINES_COUNT):
        board.append(WallLine(apply_wall_line_offset(i)))

    return board


def apply_wall_line_offset(offset: int):
    offset %= len(WALL_LINE)
    wall_line = WALL_LINE[-offset:] + WALL_LINE[:-offset]
    return wall_line.copy()
