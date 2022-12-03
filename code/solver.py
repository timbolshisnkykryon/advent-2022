import timeit

from utils.timer import timer, dads_timer
from utils.input import *
from utils.output import *


DAY = 4


@dads_timer
def my_solver(puzzle_input: str):
    """
    :param puzzle_input:
    :return:
    """


print(f"[DAY {DAY} SOLUTION]: {write_output(DAY, output=my_solver(read_input(DAY)))}")
