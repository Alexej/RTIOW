import math
import random
from typing import List, Tuple
from core.ray import Ray
from core.camera import Camera
from core.hittable_list import HittableList
from core.data_structs.config import Config
from core.data_structs.dimension import Dimension
from maths.utils import clamp
from maths.vector3 import Vector3
from tqdm import tqdm
import multiprocessing
from joblib import Parallel, delayed


def ray_color(r: Ray, world: HittableList, depth: float) -> Vector3:
    if depth <= 0:
        return Vector3(0, 0, 0)

    hit_ret = world.hit(r, 0.001, math.inf)
    if hit_ret.flag:
        sc_ret = hit_ret.record.mat_ref.scatter(r, hit_ret.record)
        if sc_ret.flag:
            return sc_ret.attenuation ** ray_color(sc_ret.scattered, world, depth - 1)
        return Vector3(0, 0, 0)

    unit_direction = ~r.direction()
    t = 0.5 * (unit_direction.y() + 1.0)
    return ((1.0 - t) * Vector3(1.0, 1.0, 1.0)) + (t * Vector3(0.5, 0.7, 1.0))

def get_pixel_color(pixel: Vector3, samples_per_pixel) -> Tuple[int, int, int]:
    r = pixel.x()
    g = pixel.y()
    b = pixel.z()

    scale = 1.0 / samples_per_pixel

    r = math.sqrt(scale * r)
    g = math.sqrt(scale * g)
    b = math.sqrt(scale * b)

    return (int(256 * clamp(r, 0.0, 0.999)),
            int(256 * clamp(g, 0.0, 0.999)),
            int(256 * clamp(b, 0.0, 0.999)))

def merge_parallel_return(parts : List) -> List[Tuple[float]]:
    merged = []
    parts.sort(key=lambda x: x[0], reverse=True)
    [merged.extend(part[1]) for part in parts]
    return merged

def render_scene_p(dimension: Dimension, camera: Camera, world: HittableList, config: Config, j: int) -> Tuple[int, List[Tuple[float]]]:
    scene = []
    for i in range(0, dimension.width):
        pixel_color = Vector3(0, 0, 0)
        for _ in range(0, config.samples_per_pixel):
            u = (i + random.random()) / (dimension.width - 1)
            v = (j + random.random()) / (dimension.height - 1)
            r = camera.get_ray(u, v)
            pixel_color += ray_color(r, world, config.max_depth)
        scene.append(get_pixel_color(pixel_color, config.samples_per_pixel))
    return (j, scene)


def render_parallel(dimension: Dimension,
                 camera: Camera,
                 world: HittableList,
                 config: Config) -> List[Tuple[float]]:
    num_of_proc = multiprocessing.cpu_count()
    parts = Parallel(n_jobs=num_of_proc)(delayed(render_scene_p)
    (dimension, camera, world, config, j) for j in tqdm(range(dimension.height - 1, -1, -1), desc="Rendering Scene"))
    return merge_parallel_return(parts)
