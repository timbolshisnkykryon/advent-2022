from pathlib import Path
from typing import Any


def write_output(day: int, output: Any):
    outputs_path = Path.cwd().parent / "outputs"
    with open(outputs_path / f"day_{day}.txt", "w") as output_file:
        output_file.write(str(output))
    return output