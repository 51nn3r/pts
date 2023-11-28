from azul.simple_types import Points
from azul.simple_types import STARTING_PLAYER
from azul.simple_types import TILE_TYPES
from azul.simple_types import Tile

TYPED_TILES_COUNT = 10
TILES_COUNT = len(TILE_TYPES) * TYPED_TILES_COUNT
TILES_IN_FACTORY = 4

PLAYERS_TO_FACTORIES = {
    2: 5,
    3: 7,
    4: 9,
}

TILES_INDEXES = {0: STARTING_PLAYER}
TILES_INDEXES.update({i + 1: TILE_TYPES[i] for i in range(len(TILE_TYPES))})

TILES_INDEXES_REVERSED = {v: k for k, v in TILES_INDEXES.items()}

WALL_LINES_COUNT = 5

WALL_LINE = [
    Tile('B'),
    Tile('Y'),
    Tile('R'),
    Tile('L'),
    Tile('G'),
]

TILES_IN_WALL = len(WALL_LINE)

_points_pattern = [1, 1, 2, 2, 2, 3, 3]
points_pattern = [Points(i) for i in _points_pattern]
