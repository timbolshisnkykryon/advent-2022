def one(puzzle_input: str):
    """
    In how many assignment pairs does one range fully contain the other?
    :param puzzle_input: Pairs of assigment ranges
    :return: The amount of pairs that include one assigment in the other's range
    """
    amount = 0
    for pair in puzzle_input.split('\n'):
        ranges = [range(int(r.split('-')[0]), int(r.split('-')[1]) + 1) for r in pair.split(',')]
        if ranges[0].start in ranges[1] and ranges[0][-1] in ranges[1] \
                or ranges[1].start in ranges[0] and ranges[1][-1] in ranges[0]:
            amount += 1
    return amount


def two(puzzle_input: str):
    """
    In how many assignment pairs does one range fully contain the other?
    :param puzzle_input: Pairs of assigment ranges
    :return: The amount of pairs that include one assigment in the other's range
    """
    amount = 0
    for pair in puzzle_input.split('\n'):
        ranges = [range(int(r.split('-')[0]), int(r.split('-')[1]) + 1) for r in pair.split(',')]
        if ranges[0].start in ranges[1] or ranges[0][-1] in ranges[1] \
                or ranges[1].start in ranges[0] or ranges[1][-1] in ranges[0]:
            amount += 1
    return amount
