import math
from maths.vector3 import Vector3
from core.ray import Ray
from core.hit_record import HitRecord
from core.abstract.material import Material
from core.abstract.hittable import Hittable
from core.data_structs.hit_return import HitReturn


class Sphere(Hittable):
    def __init__(
            self,
            _center: Vector3 = None,
            radius: int = None,
            _mat_ref: Material = None) -> None:
        self.center = _center
        self.radius = radius
        self.mat_ref = _mat_ref

    def hit(self, r: Ray, t_min: float, t_max: float) -> HitReturn:
        oc = r.origin() - self.center
        a = r.direction().length_squared()
        half_b = oc & r.direction()
        c = oc.length_squared() - self.radius * self.radius
        discriminant = (half_b * half_b) - (a * c)

        if discriminant < 0:
            return HitReturn(flag=False, record=None)
        sqrtd = math.sqrt(discriminant)

        root = (-half_b - sqrtd) / a

        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return HitReturn(flag=False, record=None)

        rec = HitRecord()
        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        rec.mat_ref = self.mat_ref

        return HitReturn(flag=True, record=rec)
