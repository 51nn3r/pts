from typing import List, Optional

from azul.simple_types import Tile, Points, TILE_TYPES


class FinalPointsCalculation:
    def getPoints(self, wall: List[List[Optional[Tile]]]) -> Points:
        _color_count: List[int] = []
        points: Points = Points(0)
        for wallline in wall:
            t = True
            for tile in wallline:
                _color_count[TILE_TYPES.index(tile)] += 1
                if tile is None:
                    t = False
                    break
            if t:
                points = Points.sum([points, Points(2)])

        for i in range(0, len(wall[0])):
            t = True
            for j in range(0, len(wall)):
                if wall[j][i] is None:
                    t = False
                    break

            if t:
                points = points = Points.sum([points, Points(7)])

        for i in _color_count:
            if i > 10:
                points = points = Points.sum([points, Points(10)])
