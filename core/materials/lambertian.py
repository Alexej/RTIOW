from maths.vector3 import Vector3
from maths.utils import near_zero, random_unit_vector
from core.ray import Ray
from core.abstract.material import Material
from core.hit_record import HitRecord
from core.data_structs.scatter_return import ScatterReturn


class Lambertian(Material):
    def __init__(self, a: Vector3) -> None:
        self.albedo = a

    def scatter(self, r_in: Ray, rec: HitRecord) -> ScatterReturn:
        scatter_direction = rec.normal + random_unit_vector()
        if near_zero(scatter_direction):
            scatter_direction = rec.normal
        return ScatterReturn(True, self.albedo, Ray(rec.p, scatter_direction))
