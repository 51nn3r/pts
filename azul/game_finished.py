from typing import List, Optional
from simple_types import Tile,FinishRoundResult
class GameFinished:
    def gameFinished(self, wall: List[List[Optional[Tile]]]) -> FinishRoundResult:
        r: FinishRoundResult = FinishRoundResult("N")
        for i in wall:
            is_line: bool = True
            for j in i:
                if j is None:
                    is_line = False
                    break
            if is_line:
                return FinishRoundResult("F")
 