import random
from maths.utils import random_vec
from core.materials.metal import Metal
from core.hittable_list import HittableList
from core.geom_objects.sphere import Sphere
from core.materials.dielectric import Dielectric
from core.materials.lambertian import Lambertian
from maths.vector3 import Vector3


def random_scene(min=-11, max=11) -> HittableList:
    world = HittableList()
    ground_material = Lambertian(Vector3(0.5, 0.5, 0.5))
    world.add(Sphere(Vector3(0, -1000, 0), 1000, ground_material))

    for a in range(min, max):
        for b in range(min, max):
            choose_mat = random.random()
            center = Vector3(a + 0.9 * random.random(), 0.2, b + 0.9 * random.random())
            if (center - Vector3(4, 0.2, 0)).length() > 0.9:
                if choose_mat < 0.8:
                    albedo = random_vec() ** random_vec()
                    sphere_material = Lambertian(albedo)
                    world.add(Sphere(center, 0.2, sphere_material))
                elif choose_mat < 0.95:
                    albedo = random_vec(0.5, 1)
                    sphere_material = Lambertian(albedo)
                    world.add(Sphere(center, 0.2, sphere_material))
                else:
                    sphere_material = Dielectric(1.5)
                    world.add(Sphere(center, 0.2, sphere_material))

    material1 = Dielectric(1.5)
    world.add(Sphere(Vector3(0, 1, 0), 1.0, material1))

    material2 = Lambertian(Vector3(0.4, 0.2, 0.1))
    world.add(Sphere(Vector3(-4, 1, 0), 1.0, material2))

    material3 = Metal(Vector3(0.7, 0.6, 0.5), 0.0)
    world.add(Sphere(Vector3(4, 1, 0), 1.0, material3))
    return world
