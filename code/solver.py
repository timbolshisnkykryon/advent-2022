import timeit

from utils.timer import timer
from utils.input import *
from utils.output import *


DAY = 2


@timer
def my_solver(puzzle_input: str):
    """
    What would your total score be if everything goes exactly according to your strategy guide?
    :param puzzle_input: list of RPS rounds
    :return: total score
    """
    total_score = 0
    for turn in puzzle_input.split('\n'):
        elf, result = turn.split()  # Format the round
        total_score += {'X': 0, 'Y': 3, 'Z': 6}[result]  # Round score
        total_score += {
            ('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
            ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
            ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1
        }[(elf, result)]
    return total_score


print(f"[DAY {DAY} SOLUTION]: {write_output(DAY, output=my_solver(read_input(DAY)))}")
