from maths.vector3 import Vector3
from core.ray import Ray
from dataclasses import dataclass


@dataclass
class ScatterReturn:
    flag: bool
    attenuation: Vector3
    scattered: Ray
