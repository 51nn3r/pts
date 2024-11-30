from __future__ import annotations

from dataclasses import dataclass

from azul.tile_source import TileSource


@dataclass(frozen=True)
class Factory(TileSource):
    pass
