from typing import List, Optional
from azul.simple_types import Tile, Points, TILE_TYPES
from azul.settings import TILES_IN_WALL, WALL_LINES_COUNT

class FinalPointsCalculation:
    def getPoints(self, wall: List[List[Optional[Tile]]]) -> Points:
        _color_count: List[int] = [0 for _ in range(TILES_IN_WALL)]

        points: Points = Points(0)
        
        for wallline in wall:
            t = True
            for tile in wallline:
                if tile is None:
                    t = False
                else:    
                    _color_count[TILE_TYPES.index(tile)] += 1
            if t:
                points =  Points.sum([points, Points(2)])
                
        for i in range(TILES_IN_WALL):
            t = True
            for j in range(WALL_LINES_COUNT):
                if wall[j][i] is None:
                    t = False
                    break

            if t:
                points = Points.sum([points, Points(7)])

        for i in _color_count:
            if i == TILES_IN_WALL:
                points = Points.sum([points, Points(10)])

        return points
