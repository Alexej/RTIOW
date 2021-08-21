from maths.utils import random_in_unit_sphere, reflect
from maths.vector3 import Vector3
from core.ray import Ray
from core.abstract.material import Material
from core.hit_record import HitRecord
from core.data_structs.scatter_return import ScatterReturn


class Metal(Material):
    def __init__(self, a: Vector3, _fuzz: float) -> None:
        self.alebrdo = a
        self.fuzz = _fuzz if _fuzz < 1 else 1

    def scatter(self, r_in: Ray, rec: HitRecord) -> ScatterReturn:
        reflected = reflect(~r_in.direction(), rec.normal)
        scattered = Ray(rec.p, reflected + self.fuzz * random_in_unit_sphere())
        return ScatterReturn(
            (scattered.direction() & rec.normal) > 0, self.alebrdo, scattered)
