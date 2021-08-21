import time
from maths.vector3 import Vector3
from file_io.p3 import P3
from core.camera import Camera
from core.data_structs.config import Config
from core.scenes.random import random_scene
from core.data_structs.dimension import Dimension
from core.raytracer import render_parallel


def main() -> None:

    aspect_ratio = 3.0 / 2.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)

    lookfrom = Vector3(13, 2, 3)
    lookat = Vector3(0, 0, 0)
    vup = Vector3(0, 1, 0)
    vfov = 20.0
    dist_to_focus = 10.0
    aperture = 0.1

    camera = Camera(lookfrom,
                    lookat,
                    vup,
                    vfov,
                    aspect_ratio,
                    aperture,
                    dist_to_focus)

    dimension = Dimension(image_width, image_height)
    config = Config(max_depth=50, samples_per_pixel=500)
    world = random_scene()
    scene = render_parallel(dimension, camera, world, config)
    file_name = "images/image {}".format(time.time())
    P3(file_name).save_scene(dimension, scene)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
