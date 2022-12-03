import os
from pathlib import Path


def read_input(day: int):
    inputs_path = Path.cwd().parent / "inputs"

    with open(inputs_path / f'day_{day}.txt', 'r') as input_file:
        data = input_file.read()
    return data

