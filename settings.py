from simple_types import Tile
from simple_types import Points

TILES_COUNT = 10
TILES_IN_FACTORY = 4

PLAYERS_TO_FACTORIES = {
    2: 5,
    3: 7,
    4: 9,
}

TILES_INDEXES = {
    0: 'S',
    1: 'R',
    2: 'B',
    3: 'Y',
    4: 'G',
    5: 'L',
}

WALL_LINES_COUNT = 5

WALL_LINE = [
    [
        Tile('B'),
        Tile('Y'),
        Tile('R'),
        Tile('L'),
        Tile('G'),
    ],
]

_points_pattern = [1, 1, 2, 2, 2, 3, 3]
points_pattern = [Points(i) for i in _points_pattern]
