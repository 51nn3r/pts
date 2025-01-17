from __future__ import annotations
from typing import List


class Points:
    _value: int

    def __init__(self, value: int):
        self._value = value

    @property
    def reverse(self) -> Points:
        return Points(-self._value)

    @property
    def value(self) -> int:
        return self._value

    @staticmethod
    def sum(points_list: List[Points]) -> Points:
        return Points(sum((x.value for x in points_list)))

    def __str__(self) -> str:
        return str(self._value)


class Tile:
    _representation: str

    def __init__(self, representation: str):
        self._representation = representation

    def __str__(self) -> str:
        return self._representation

    def __repr__(self) -> str:
        return self._representation

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __hash__(self):
        return hash(self.__str__())


STARTING_PLAYER: Tile = Tile("S")
RED: Tile = Tile("R")
BLUE: Tile = Tile("B")
YELLOW: Tile = Tile("Y")
GREEN: Tile = Tile("G")
BLACK: Tile = Tile("L")

TILE_TYPES: List = [RED, BLUE, YELLOW, GREEN, BLACK]


class FinishRoundResult:
    _result: str

    def __init__(self, result: str):
        self._result = result

    def __str__(self):
        return self._result

    def __repr__(self):
        return self._result


NORMAL: FinishRoundResult = FinishRoundResult("N")
GAME_FINISHED: FinishRoundResult = FinishRoundResult("F")


def compress_tile_list(tiles: List[Tile]) -> str:
    return "".join([str(x) for x in tiles])
