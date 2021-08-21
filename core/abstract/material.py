from abc import ABC, abstractmethod
from core.hit_record import HitRecord
from core.ray import Ray
from core.data_structs.scatter_return import ScatterReturn


class Material(ABC):
    @abstractmethod
    def scatter(self, r_in: Ray, rec: HitRecord) -> ScatterReturn:
        pass
