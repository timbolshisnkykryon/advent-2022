
def one(puzzle_input: str):
    """
    Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?
    :param puzzle_input: rucksack content, 2 compartments, each half of the content
    :return: sum of the priorities
    """
    sum_priorities = 0
    for rucksack in puzzle_input.split('\n'):
        # Each rucksack can be divided into two even compartments
        common = ord(set(rucksack[:int(len(rucksack)/2)]).intersection(rucksack[int(len(rucksack)/2):]).pop())
        sum_priorities += common - 96 if common > 96 else common - 38

    return sum_priorities


def two(puzzle_input: str):
    """
    Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?
    :param puzzle_input: rucksack content, 2 compartments, each half of the content
    :return: sum of the priorities
    """
    sum_priorities = 0
    rucksacks = puzzle_input.split('\n')
    for group in range(0, int(len(rucksacks)), 3):
        common = ord(set(rucksacks[group]).intersection(rucksacks[group+1]).intersection(rucksacks[group+2]).pop())
        sum_priorities += common - 96 if common > 96 else common - 38

    return sum_priorities
