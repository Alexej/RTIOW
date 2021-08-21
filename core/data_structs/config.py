from dataclasses import dataclass


@dataclass
class Config:
    max_depth: int
    samples_per_pixel: int
