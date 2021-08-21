from pathlib import Path
from typing import List
import subprocess


def autopep8_wrapper(files: List[str]) -> None:
    for file in files:
        command = "{} {}".format(
            "autopep8.exe --in-place --aggressive --aggressive", file)
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("{} {}".format(file, process.returncode))


if __name__ == '__main__':
    files = [path for path in Path('../').rglob('*.py')]
    autopep8_wrapper(files)
