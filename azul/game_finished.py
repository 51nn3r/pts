from typing import List, Optional
from azul.simple_types import Tile,FinishRoundResult
class GameFinished:
    def game_finished(self, wall: List[List[Optional[Tile]]]) -> FinishRoundResult:
        for i in wall:
            is_line: bool = True
            for j in i:
                if j is None:
                    is_line = False
                    break
            if is_line:
                return FinishRoundResult("F")
        return FinishRoundResult("N")