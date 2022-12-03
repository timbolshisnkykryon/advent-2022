def one(puzzle_input: str):
    """
    What would your total score be if everything goes exactly according to your strategy guide?
    :param puzzle_input: list of RPS rounds
    :return: total score
    """
    total_score = 0
    for turn in puzzle_input.split('\n'):
        elf, me = turn.split()  # Format the round
        total_score += {'X': 1, 'Y': 2, 'Z': 3}[me]
        if {'A': 'X', 'B': 'Y', 'C': 'Z'}[elf] == me:  # DRAW
            total_score += 3
        elif {'X': 'C', 'Y': 'A', 'Z': 'B'}[me] == elf:  # WON
            total_score += 6

    return total_score


# 0.00151980s
def two(puzzle_input: str):
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

