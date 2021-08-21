import math
import unittest
from maths.vector3 import Vector3


def compare_vectors(v1: Vector3, v2: Vector3) -> bool:
    return v1.points[0] == v2.points[0] and v1.points[1] == v2.points[1] and v1.points[2] == v2.points[2]


class Vector3Tester(unittest.TestCase):
    scalar: float = 3.4564363456736576
    x1: float = 4756835.45745613241341636
    y1: float = 9785.456456456
    z1: float = 1324134

    x2: float = 2345
    y2: float = 0.00005345
    z2: float = 235234523452.5234524535

    vec2_str: str = "4756835.457456132 9785.456456456 1324134"

    def test_index_operator(self):
        vec = Vector3(self.x1, self.y1, self.z1)
        self.assertTrue(vec[0] == self.x1 and vec[1] ==
                        self.y1 and vec[2] == self.z1)

    def test_empty_constructor(self):
        vec = Vector3()
        self.assertTrue(compare_vectors(vec, Vector3(0, 0, 0)))

    def test_constructor(self):
        vec = Vector3(self.x1, self.y1, self.z1)
        self.assertTrue(vec.points[0] == self.x1 and vec.points[1]
                        == self.y1 and vec.points[2] == self.z1)

    def test_getters(self):
        vec = Vector3(self.x1, self.y1, self.z1)
        self.assertTrue(vec.x() == self.x1 and vec.y() ==
                        self.y1 and vec.z() == self.z1)

    def test_subtraction(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec2 = Vector3(self.x2, self.y2, self.z2)
        vec_test = Vector3(self.x1 - self.x2, self.y1 -
                           self.y2, self.z1 - self.z2)
        vec3 = vec1 - vec2
        self.assertTrue(compare_vectors(vec3, vec_test))

    def test_negation(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec_test = Vector3(-self.x1, -self.y1, -self.z1)
        vec1 = -vec1
        self.assertTrue(compare_vectors(vec1, vec_test))

    def test_addition(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec2 = Vector3(self.x2, self.y2, self.z2)
        vec3 = vec1 + vec2
        vec_test = Vector3(self.x1 + self.x2, self.y1 +
                           self.y2, self.z1 + self.z2)
        self.assertTrue(compare_vectors(vec3, vec_test))

    def test_short_addition(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec2 = Vector3(self.x2, self.y2, self.z2)
        vec1 += vec2
        vec_test = Vector3(self.x1 + self.x2, self.y1 +
                           self.y2, self.z1 + self.z2)
        self.assertTrue(compare_vectors(vec1, vec_test))

    def test_short_multiplication(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec1 *= self.scalar
        vec_test = Vector3(self.x1 * self.scalar, self.y1 *
                           self.scalar, self.z1 * self.scalar)
        self.assertTrue(compare_vectors(vec1, vec_test))

    def test_division(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec1 = vec1 / self.scalar
        vec_test = Vector3(self.x1 / self.scalar, self.y1 /
                           self.scalar, self.z1 / self.scalar)
        self.assertTrue(compare_vectors(vec1, vec_test))

    def test_short_division(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec1 /= self.scalar
        vec_test = Vector3(self.x1 / self.scalar, self.y1 /
                           self.scalar, self.z1 / self.scalar)
        self.assertTrue(compare_vectors(vec1, vec_test))

    def test_multiplication_left(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec1 = vec1 * self.scalar
        vec_test = Vector3(self.x1 * self.scalar, self.y1 *
                           self.scalar, self.z1 * self.scalar)
        self.assertTrue(compare_vectors(vec1, vec_test))

    def test_multiplication_right(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec1 = self.scalar * vec1
        vec_test = Vector3(self.x1 * self.scalar, self.y1 *
                           self.scalar, self.z1 * self.scalar)
        self.assertTrue(compare_vectors(vec1, vec_test))

    def test_string(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        self.assertEqual(
            vec1.__str__(), self.vec2_str)

    def test_length_squared(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        self.assertTrue(vec1.length_squared(), self.x1 *
                        self.x1 + self.y1 * self.y1 + self.z1 * self.z1)

    def test_length(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        self.assertTrue(vec1.length(), math.sqrt(
            self.x1 * self.x1 + self.y1 * self.y1 + self.z1 * self.z1))

    def test_cross_product(self):
        vec1 = Vector3(2, 3, 4)
        vec2 = Vector3(5, 6, 7)
        vec3 = vec1 % vec2
        self.assertTrue(vec3[0] == -3 and vec3[1] == 6 and vec3[2] == -3)

    def test_dot_product(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec2 = Vector3(self.x2, self.y2, self.z2)
        self.assertEqual(vec1 & vec2, self.x1 * self.x2 +
                         self.y1 * self.y2 + self.z1 * self.z2)

    def test_mul_by_el(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec2 = Vector3(self.x2, self.y2, self.z2)
        vec3 = vec1 ** vec2
        vec_test = Vector3(
            self.x1 * self.x2,
            self.y1 * self.y2,
            self.z1 * self.z2)
        self.assertTrue(compare_vectors(vec3, vec_test))

    def test_unit_vector(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        unit_v = ~vec1
        self.assertEqual(unit_v.length(), 1)

    def test_equal(self):
        vec1 = Vector3(self.x1, self.y1, self.z1)
        vec2 = Vector3(self.x1, self.y1, self.z1)
        self.assertTrue(vec1 == vec2)


'''
if __name__ == '__main__':
    unittest.main()
'''
# python -m unittest -v
