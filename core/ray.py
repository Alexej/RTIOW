from maths.vector3 import Vector3


class Ray:
    def __init__(self, origin: Vector3, direction: Vector3) -> None:
        self.orig = origin
        self.dir = direction

    def origin(self) -> Vector3:
        return self.orig

    def direction(self) -> Vector3:
        return self.dir

    def at(self, t: int) -> Vector3:
        return self.orig + t * self.dir
