import math


class Vector3:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.points = []
        self.points.append(x)
        self.points.append(y)
        self.points.append(z)

    def __getitem__(self, index: int) -> float:
        return self.points[index]

    def x(self) -> float:
        return self[0]

    def y(self) -> float:
        return self[1]

    def z(self) -> float:
        return self[2]

    def __sub__(self, v2: 'Vector3') -> 'Vector3':
        return Vector3(self[0] - v2[0], self[1] - v2[1], self[2] - v2[2])

    def __neg__(self) -> 'Vector3':
        return Vector3(-self[0], -self[1], -self[2])

    def __add__(self, v2: 'Vector3') -> 'Vector3':
        return Vector3(self[0] + v2[0], self[1] + v2[1], self[2] + v2[2])

    def __mul__(self, scalar: float) -> 'Vector3':
        return Vector3(self[0] * scalar, self[1] * scalar, self[2] * scalar)

    def __rmul__(self, scalar: float) -> 'Vector3':
        return Vector3(self[0] * scalar, self[1] * scalar, self[2] * scalar)

    def __truediv__(self, scalar: float) -> 'Vector3':
        return self * (1 / scalar)

    def __itruediv__(self, scalar: float) -> 'Vector3':
        self.points[0] /= scalar
        self.points[1] /= scalar
        self.points[2] /= scalar
        return self

    def __iadd__(self, v2: 'Vector3') -> 'Vector3':
        self.points[0] += v2[0]
        self.points[1] += v2[1]
        self.points[2] += v2[2]
        return self

    def __imul__(self, scalar: float) -> 'Vector3':
        self.points[0] *= scalar
        self.points[1] *= scalar
        self.points[2] *= scalar
        return self

    def __str__(self):
        return "{} {} {}".format(*self.points)

    def length_squared(self) -> float:
        return self & self

    def length(self) -> float:
        return math.sqrt(self.length_squared())

    def __eq__(self, v2: 'Vector3'):
        return self[0] == v2[0] and self[1] == v2[1] and self[2] == v2[2]

    # mul by el
    def __pow__(self, v2: 'Vector3') -> 'Vector3':
        return Vector3(self[0] * v2[0], self[1] * v2[1], self[2] * v2[2])

    #dot product
    def __and__(self, v2: 'Vector3') -> float:
        return self[0] * v2[0] + self[1] * v2[1] + self[2] * v2[2]

    #cross product
    def __mod__(self, v2: 'Vector3') -> float:
        return Vector3(self[1] * v2[2] - self[2] * v2[1],
                    self[2] * v2[0] - self[0] * v2[2],
                    self[0] * v2[1] - self[1] * v2[0])

    #unit vector
    def __invert__(v: 'Vector3') ->  'Vector3':
        return v / v.length()
