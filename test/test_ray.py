import unittest
from core.ray import Ray
from maths.vector3 import Vector3


class RayTester(unittest.TestCase):

    v1 = Vector3(25.5, 10, 13.4)
    v2 = Vector3(11, 22, 34.01)

    def test_constructor(self):
        r = Ray(origin=self.v1, direction=self.v2)
        self.assertTrue(r.origin() == self.v1 and r.direction() == self.v2)

    def test_at(self):
        r = Ray(origin=self.v1, direction=self.v2)
        t = 23.404
        self.assertTrue(r.at(t) == self.v1 + (t * self.v2))
