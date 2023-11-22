from typing import List, Optional
from simple_types import Tile,FinishRoundResult
class GameFinished:
    def gameFinished(wall: List[List[Optional[Tile]]])->FinishRoundResult:
        for i in wall:
            for j in i:
                if j == None: return FinishRoundResult("N")
        
        return FinishRoundResult("F")
 