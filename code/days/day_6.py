def one(puzzle_input: str):  # one took 0.00034210s to execute
    """
    How many characters need to be processed before the first start-of-packet marker is detected?
    :param puzzle_input: datastream buffer
    :return: The index at the end of the marker
    """
    for index, char_index in enumerate(range(3, len(puzzle_input))):
        if len({puzzle_input[char_index],
                puzzle_input[char_index - 1],
                puzzle_input[char_index - 2],
                puzzle_input[char_index - 3]}) == 4:
            return char_index + 1


def two(puzzle_input: str):  # two took 0.00270280s to execute
    """
    How many characters need to be processed before the first start-of-packet marker is detected?
    :param puzzle_input: datastream buffer
    :return: The index at the end of the marker
    """
    marker_length = 14
    for char_index in range(marker_length-1, len(puzzle_input)):
        if len({puzzle_input[char_index-n] for n in range(marker_length)}) == marker_length:
            return char_index + 1
