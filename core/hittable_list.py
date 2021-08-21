from core.ray import Ray
from core.abstract.hittable import Hittable
from core.data_structs.hit_return import HitReturn
from typing import Optional

class HittableList(Hittable):
    def __init__(self, objs : Optional[Hittable]=None) -> None:
        self.object_list = []
        if objs:
            self.object_list.append(objs)

    def clear(self) -> None:
        self.objs = []

    def size(self) -> int:
        return len(self.object_list)

    def add(self, objs) -> None:
        self.object_list.append(objs)

    def hit(self, r: Ray, t_min: float, t_max: float) -> HitReturn:
        rec = None
        hit_anything = False
        closest_so_far = t_max

        for obj in self.object_list:
            hit_ret = obj.hit(r, t_min, closest_so_far)
            if hit_ret.flag:
                hit_anything = True
                closest_so_far = hit_ret.record.t
                rec = hit_ret.record

        return HitReturn(flag=hit_anything, record=rec)
