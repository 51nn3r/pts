from __future__ import annotations

from dataclasses import dataclass
from typing import List

from random import shuffle


@dataclass(frozen=True)
class Randomizer:
    @staticmethod
    def shuffle_array(arr: List):
        arr_copy = arr.copy()
        shuffle(arr_copy)
        return arr_copy
