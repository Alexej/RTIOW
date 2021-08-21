from core.hit_record import HitRecord
from dataclasses import dataclass
from typing import Optional

@dataclass
class HitReturn:
    flag: Optional[bool]
    record: Optional[HitRecord]
