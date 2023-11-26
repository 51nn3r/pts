from typing import List

from azul.wall_line import WallLine
from azul.settings import WALL_LINES_COUNT
from azul.settings import WALL_LINE


def define_board_wall_lines() -> List[WallLine]:
    board: List[WallLine] = []

    for i in range(WALL_LINES_COUNT):
        board.append(WallLine(apply_wall_line_offset(i)))

    for i in range(WALL_LINES_COUNT - 1):
        board[i]._down = board[i + 1]
        board[i + 1]._up = board[i]

    return board


def apply_wall_line_offset(offset: int):
    offset %= len(WALL_LINE)
    wall_line = WALL_LINE[-offset:] + WALL_LINE[:-offset]
    return wall_line.copy()
