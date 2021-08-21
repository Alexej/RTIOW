from typing import List, Tuple
from core.abstract.io import IO
from core.data_structs.dimension import Dimension


class P3(IO):
    file_name_template = "{}.ppm"
    header_template = "P3\n{} {}\n{}\n"
    pixel_color_template = "{} {} {}\n"
    maximum_color_value = 255

    def __init__(self, file_name: str) -> None:
        try:
            self.file = open(self.file_name_template.format(file_name), "w")
        except OSError as exception:
            print("OS error: {0}".format(exception))

    def write_header(self, dimension: Dimension) -> None:
        self.file.write(self.header_template.format(
            dimension.width, dimension.height, self.maximum_color_value))

    def write_colors(self, scene: List[Tuple[int]]) -> None:
        for pixel in scene:
            self.file.write(self.pixel_color_template.format(*pixel))

    def save_scene(self, dimension: Dimension,
                   scene: List[Tuple[int]]) -> None:
        self.write_header(dimension)
        self.write_colors(scene)

    def __del__(self) -> None:
        self.file.close()
