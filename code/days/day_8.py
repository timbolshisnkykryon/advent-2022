def one(puzzle_input: str):  # one took 0.23413870s to execute
    """
    Find how many trees are visible whether horizontal or vertically
    :param puzzle_input: grid of trees
    :return: number of visible trees
    """
    input_list = puzzle_input.split('\n')
    columns, rows = len(input_list[0]), len(input_list)
    visible = (columns * 2 - 4) + (rows * 2)
    for row in range(1, rows-1):

        row_list = [int(column) for column in [*input_list[row]]]
        for column in range(1, columns-1):
            column_list = [int(r) for r in [c[column] for c in input_list]]
            current_tree = row_list[column]
            if current_tree > max(column_list[:row]) or current_tree > max(column_list[row+1:]) \
                    or current_tree > max(row_list[:column]) or current_tree > max(row_list[column+1:]):
                visible += 1

    return visible


def scene_check(current_value: int, scene_range: list):
    current = 0
    for a in scene_range:
        current += 1
        if a >= current_value:
            break
    return current


def two(puzzle_input: str):  # two took 0.14425520s to execute
    """
    Find how many trees are visible whether horizontal or vertically
    :param puzzle_input: grid of trees
    :return: number of visible trees
    """
    input_list = puzzle_input.split('\n')
    columns, rows = len(input_list[0]), len(input_list)
    best_scenic = 0
    for row in range(1, rows - 1):

        row_list = [int(column) for column in [*input_list[row]]]
        for column in range(1, columns - 1):
            current_score = 1
            column_list = [int(r) for r in [c[column] for c in input_list]]
            current_tree = row_list[column]
            current_score *= scene_check(current_tree, row_list[column + 1:])
            current_score *= scene_check(current_tree, list(reversed(row_list[:column])))
            current_score *= scene_check(current_tree, list(reversed(column_list[:row])))
            current_score *= scene_check(current_tree, column_list[row+1:])

            best_scenic = current_score if current_score > best_scenic else best_scenic

    return best_scenic
