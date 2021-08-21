import math
import random
from maths.vector3 import Vector3


def random_in_unit_sphere() -> Vector3:
    while True:
        p = random_vec(-1, 1)
        if p.length_squared() < 1:
            return p


def clamp(x: float, min: float, max: float) -> float:
    if x < min:
        return min
    if x > max:
        return max
    return x


def random_vec(min: float = 0, max: float = 1) -> Vector3:
    return Vector3(
        random.uniform(
            min, max), random.uniform(
            min, max), random.uniform(
                min, max))


def random_unit_vector() -> Vector3:
    return ~random_in_unit_sphere()


def random_in_hemisphere(normal: Vector3) -> Vector3:
    in_unit_sphere = random_in_unit_sphere()

    if in_unit_sphere & normal > 0.0:
        return in_unit_sphere
    else:
        return -in_unit_sphere


def near_zero(vec: Vector3) -> bool:
    s = 1e-8
    return (
        math.fabs(
            vec.x()) < s) and (
        math.fabs(
            vec.y()) < s) and (
        math.fabs(
            vec.z()) < s)


def reflect(v: Vector3, n: Vector3) -> Vector3:
    return v - 2 * (v & n) * n


def refract(uv: Vector3, n: Vector3, etai_over_etat: float) -> Vector3:
    cos_theta = min(-uv & n, 1.0)
    r_out_perp = etai_over_etat * (uv + cos_theta * n)
    r_out_parallel = - \
        math.sqrt(math.fabs(1.0 - r_out_perp.length_squared())) * n
    return r_out_perp + r_out_parallel


def random_in_unit_disk() -> Vector3:
    while True:
        p = Vector3(random.uniform(-1, 1), random.uniform(-1, 1), 0)
        if p.length_squared() >= 1:
            continue
        return p
