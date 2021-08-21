from maths.utils import random_in_unit_disk
from maths.vector3 import Vector3
from core.ray import Ray
from math import radians, tan


class Camera:
    def __init__(self,
                 _lookfrom: Vector3,
                 _lookat: Vector3,
                 _vup: Vector3,
                 _vfov: float,
                 _aspect_ratio: float,
                 _aperture: float,
                 _focus_dist: float) -> None:

        self.w = ~(_lookfrom - _lookat)
        self.u = ~(_vup % self.w)
        self.v = self.w % self.u
        self.lens_radius = _aperture / 2
        self.origin = _lookfrom
        self.vfov = _vfov

        theta = radians(self.vfov)
        h = tan(theta / 2)
        self.viewport_height = 2.0 * h
        self.viewport_width = _aspect_ratio * self.viewport_height
        self.horizontal = _focus_dist * self.viewport_width * self.u
        self.vertival = _focus_dist * self.viewport_height * self.v
        self.lower_left_corner = self.origin - self.horizontal / \
            2 - self.vertival / 2 - _focus_dist * self.w

    def get_ray(self, s: float, t: float) -> Ray:
        rd = self.lens_radius * random_in_unit_disk()
        offset = self.u * rd.x() + self.v * rd.y()
        return Ray(self.origin + offset,
            self.lower_left_corner + 
            s * self.horizontal + 
            t * self.vertival -
            self.origin - offset)
