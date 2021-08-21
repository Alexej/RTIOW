from core.ray import Ray
from maths.vector3 import Vector3
from typing import Optional

class HitRecord:
    def __init__(self, _p: Optional[Vector3] = None,
                 _normal: Optional[Vector3] = None,
                 _t: Optional[float] = None,
                 _front_face: Optional[bool] = None
                 ) -> None:
        self.p = _p
        self.normal = _normal
        self.t = _t
        self.front_face = _front_face
        self.mat_ref = None

    def set_face_normal(self, r: Ray, outward_normal: Vector3) -> None:
        self.front_face = r.direction() & outward_normal < 0
        self.normal = outward_normal if self.front_face else -outward_normal
