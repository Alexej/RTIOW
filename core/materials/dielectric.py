from math import sqrt
from random import random
from core.ray import Ray
from core.hit_record import HitRecord
from core.abstract.material import Material
from core.data_structs.scatter_return import ScatterReturn
from maths.vector3 import Vector3
from maths.utils import refract, reflect


class Dielectric(Material):
    def __init__(self, index_of_refraction_: float) -> None:
        self.index_of_refraction = index_of_refraction_

    def scatter(self, r_in: Ray, rec: HitRecord) -> ScatterReturn:
        attenuation = Vector3(1.0, 1.0, 1.0)
        refraction_ratio = (
            1.0 / self.index_of_refraction) if rec.front_face else self.index_of_refraction
        unit_direction = ~r_in.direction()

        cos_theta = min((-unit_direction & rec.normal), 1.0)
        sin_theta = sqrt(1.0 - cos_theta * cos_theta)

        cannot_refract = (refraction_ratio * sin_theta) > 1.0
        direction = None

        if cannot_refract or self.reflectance(
                cos_theta, refraction_ratio) > random():
            direction = reflect(unit_direction, rec.normal)
        else:
            direction = refract(unit_direction, rec.normal, refraction_ratio)
        scattered = Ray(rec.p, direction)
        return ScatterReturn(True, attenuation, scattered)

    def reflectance(self, cosine: float, ref_idx: float) -> float:
        r0 = (1 - ref_idx) / (1 + ref_idx)
        r0 = r0 * r0
        return r0 + (1 - r0) * pow((1 - cosine), 5)
