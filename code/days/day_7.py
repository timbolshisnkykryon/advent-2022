
def get_from_dict(d: dict, path: [str]):
    return reduce(operator.getitem, path, d)


def set_in_dict(d: dict, path: [str], value, size=None) -> None:
    if not size:
        get_from_dict(d, path[:-1])[path[-1]][value] = {}
    else:
        get_from_dict(d, path[:-1])[path[-1]][value] = int(size)


def summer(d: dict, sums: list=None) -> int:
    global findings
    if not d or all([isinstance(value, int) for value in d.values()]):
        # If dict is non-continuous
        c_sum = sum(list(d.values()) if d else [])
        findings.append(c_sum if c_sum < 100000 else 0)
        return c_sum

    c_sum = sum([value for value in d.values() if isinstance(value, int)])
    # c_sum = c_sum if c_sum < 100000 else 0
    other_sums = [summer(value) for value in d.values() if isinstance(value, dict) and value]
    if (c_sum + sum(other_sums)) < 100000:
        findings.append(c_sum + sum(other_sums))
    return c_sum + sum(other_sums)

    # if (c_sum + sum(other_sums)) < 100000:
    #     return c_sum + (2 * sum(other_sums))
    # return sum(other_sums)


def one(puzzle_input: str):
    global findings
    """
    Find all of the directories with a total size of at most 100000.
    What is the sum of the total sizes of those directories?
    :param puzzle_input: Device's system command line
    :return: Sum of all of the directories with size < 100,000
    """
    storage = {"/": {}}
    current_path = []
    # First lets go through commands and fill the storage dict
    for line in puzzle_input.split('\n'):
        if not line.startswith('$'):
            if line.split()[0] == 'dir':
                set_in_dict(storage, current_path, line.split()[1])
            else:
                set_in_dict(storage, current_path, line.split()[1], size=line.split()[0])
        command = line.split()[1]
        if command == 'cd':
            argument = line.split()[2]
            if argument != "..":
                current_path.append(argument)
                # reduce(dict.__getitem__, current_directory_path, storage).update({})
                d = storage.setdefault(argument, {})
            else:
                current_path.pop()

    summer(storage, [])
    return sum(findings)


def summer_two(d: dict, sums: list=None) -> int:
    global findings
    if not d or all([isinstance(value, int) for value in d.values()]):
        # If dict is non-continuous
        c_sum = sum(list(d.values()) if d else [])
        # findings.append(c_sum)
        return c_sum

    c_sum = sum([value for value in d.values() if isinstance(value, int)])
    # c_sum = c_sum if c_sum < 100000 else 0
    other_sums = [summer(value) for value in d.values() if isinstance(value, dict) and value]
    # if (c_sum + sum(other_sums)) < 100000:
    findings.append(c_sum + sum(other_sums))
    return c_sum + sum(other_sums)

    # if (c_sum + sum(other_sums)) < 100000:
    #     return c_sum + (2 * sum(other_sums))
    # return sum(other_sums)


def two(puzzle_input: str):
    global findings
    """
    Find all of the directories with a total size of at most 100000.
    What is the sum of the total sizes of those directories?
    :param puzzle_input: Device's system command line
    :return: Sum of all of the directories with size < 100,000
    """
    storage = {"/": {}}
    current_path = []
    # First lets go through commands and fill the storage dict
    for line in puzzle_input.split('\n'):
        if not line.startswith('$'):
            if line.split()[0] == 'dir':
                set_in_dict(storage, current_path, line.split()[1])
            else:
                set_in_dict(storage, current_path, line.split()[1], size=line.split()[0])
        command = line.split()[1]
        if command == 'cd':
            argument = line.split()[2]
            if argument != "..":
                current_path.append(argument)
                # reduce(dict.__getitem__, current_directory_path, storage).update({})
                d = storage.setdefault(argument, {})
            else:
                current_path.pop()

    summer(storage, [])
    ds = sorted(findings)
    for directory in ds:
        if (70000000 - sum(findings) + directory) > 30000000:
            return directory