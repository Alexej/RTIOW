import subprocess
import cv2
import glob
from typing import List


path_to_pypy = r"C:\Users\alexe\Desktop\python\pypy3.7-v7.3.5-win64\pypy3.7-v7.3.5-win64\pypy3"
path_to_main = r"main.py"

def render_scenes(seconds: int, fps: int) -> None:
    templ = "{} {} {}"
    for i in range(0, seconds * fps):
        step = i / 10
        command = templ.format(path_to_pypy, path_to_main, templ.format(-step, step, step))
        process = subprocess.Popen(command, shell=True)
        process.wait()


def create_image_array(image_path: str, image_format: str) -> List:
    img_array = []
    for image in glob.glob('{}/*.{}'.format(image_path, image_format)):
        img = cv2.imread(image)
        img_array.append(img)
    return img_array


def create_video(img_arr: List, file_name: str, fps: int) -> None:
    height, width, _ = img_arr[0].shape
    out = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(
        *'DIVX'), fps, (width, height))
    for i in range(len(img_arr)):
        out.write(img_arr[i])
    out.release()


if __name__ == '__main__':
    fps = 24
    seconds = 5
    #render_scenes(seconds, fps)
    img_arr = create_image_array("images", "ppm")
    create_video(img_arr, "video2.avi", 60)
