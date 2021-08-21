from abc import ABC, abstractmethod
from typing import Tuple, List
from core.data_structs.dimension import Dimension


class IO(ABC):
    @abstractmethod
    def save_scene(self, dimension: Dimension,
                   scene: List[Tuple[int]]) -> None:
        pass
