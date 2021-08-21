from abc import ABC, abstractmethod
from typing import Tuple
from core.ray import Ray
from core.hit_record import HitRecord


class Hittable(ABC):
    @abstractmethod
    def hit(self, r: Ray, t_min: float, t_max: float) -> Tuple[bool, HitRecord]:
        pass
