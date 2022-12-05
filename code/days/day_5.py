def one(puzzle_input: str):  # 0.00101790s
    """
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    :param puzzle_input: starting point, different container arrangements
    :return: string of all top container
    """
    stacks = {1: []}
    for container_row in puzzle_input.split('\n'):
        if not container_row or container_row[1] == '1':  # If finished reading the containers
            break
        for container, item_index in enumerate(range(1, len(container_row), 4)):  # Collect items in each row
            if container_row[item_index] != " ":  # If not empty spot
                if container + 1 not in stacks:
                    stacks[container + 1] = [container_row[item_index]]
                else:
                    stacks[container + 1].insert(0, container_row[item_index])

    for action in puzzle_input.split('\n'):
        if not action or action[0] != 'm':  # If not an action (prob containers input)
            continue
        action = action.split()
        amount, from_container, to_container = int(action[1]), int(action[3]), int(action[5])
        for _ in range(amount):
            stacks[to_container].append(stacks[from_container].pop())
    stacks = dict(sorted(stacks.items()))  # Took me 20 minutes to figure this bug
    return "".join([container[-1] for container in list(stacks.values())])  # Return final string


def two(puzzle_input: str):  # 0.00079470s
    """
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    :param puzzle_input: starting point, different container arrangements
    :return: string of all top container
    """
    stacks = {1: []}
    for container_row in puzzle_input.split('\n'):
        if not container_row or container_row[1] == '1':  # If finished reading the containers
            break
        for container, item_index in enumerate(range(1, len(container_row), 4)):  # Collect items in each row
            if container_row[item_index] != " ":  # If not empty spot
                if container + 1 not in stacks:
                    stacks[container + 1] = [container_row[item_index]]
                else:
                    stacks[container + 1].insert(0, container_row[item_index])

    for action in puzzle_input.split('\n'):
        if not action or action[0] != 'm':  # If not an action (prob containers input)
            continue
        action = action.split()
        amount, from_container, to_container = int(action[1]), int(action[3]), int(action[5])
        stacks[to_container].extend(stacks[from_container][-amount:])  # Move last 'amount' elements
        del stacks[from_container][len(stacks[from_container]) - amount:]  # Remove from original list
    stacks = dict(sorted(stacks.items()))  # Took me 20 minutes to figure this bug
    return "".join([container[-1] for container in list(stacks.values())])  # Return final string
