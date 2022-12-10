def update_tail(ground, head_x, head_y, tail_x, tail_y) -> (int, int):
    """
    Update the tail location according to the head
    :return:
    """
    if abs(head_x - tail_x) > 1:
        tail_x += head_x - tail_x + (-1 if (head_x - tail_x) > 0 else +1)
        if abs(head_y - tail_y) > 0:
            tail_y += head_y - tail_y

    elif abs(head_y - tail_y) > 1:
        tail_y += head_y - tail_y + (-1 if (head_y - tail_y) > 0 else +1)
        if abs(head_x - tail_x) > 0:
            tail_x += head_x - tail_x

    ground[(tail_y, tail_x)] = "#"
    return ground, tail_x, tail_y, head_y


def one(puzzle_input: str):  # one took 0.01163960s to execute

    """
    :param puzzle_input:
    :return:
    """
    ground = {}
    tail_x, tail_y = 0, 0
    head_x, head_y = 0, 0

    for move in puzzle_input.split('\n'):
        direction, steps = move.split(' ')[0], int(move.split(' ')[1])
        match direction:
            case "R":
                for i in range(steps):
                    head_x += 1
                    ground, tail_x, tail_y, head_y = update_tail(ground, head_x, head_y, tail_x, tail_y)
            case "U":
                for i in range(steps):
                    head_y -= 1
                    ground, tail_x, tail_y, head_y = update_tail(ground, head_x, head_y, tail_x, tail_y)
            case "L":
                for i in range(steps):
                    head_x -= 1
                    ground, tail_x, tail_y, head_y = update_tail(ground, head_x, head_y, tail_x, tail_y)
            case "D":
                for i in range(steps):
                    head_y += 1
                    ground, tail_x, tail_y, head_y = update_tail(ground, head_x, head_y, tail_x, tail_y)
    return len(ground)


"""TWO"""


def two_update_tail(head_y, head_x, tail_y, tail_x) -> (int, int):
    """
    Update the tail location according to the head
    :return:
    """
    if abs(head_x - tail_x) > 1 and abs(head_y - tail_y) > 1:
        tail_x += head_x - tail_x + (-1 if (head_x - tail_x) > 0 else +1)
        tail_y += head_y - tail_y + (-1 if (head_y - tail_y) > 0 else +1)
    elif abs(head_x - tail_x) > 1:
        tail_x += head_x - tail_x + (-1 if (head_x - tail_x) > 0 else +1)
        if abs(head_y - tail_y) > 0:
            tail_y += head_y - tail_y

    elif abs(head_y - tail_y) > 1:
        tail_y += head_y - tail_y + (-1 if (head_y - tail_y) > 0 else +1)
        if abs(head_x - tail_x) > 0:
            tail_x += head_x - tail_x

    return tail_y, tail_x


def follower_trails(snail: list[list], number: int, stop_at: int = None) -> list[list]:
    if stop_at and number == stop_at:
        return snail
    elif not stop_at and number == 9:  # Ran on all the snail
        return snail
    snail[number + 1][0], snail[number + 1][1] = two_update_tail(snail[number][0], snail[number][1],
                                                                 snail[number + 1][0], snail[number + 1][1])
    return follower_trails(snail, number + 1, stop_at)


def move_head(snail, move) -> list[list]:
    match move.split(' ')[0]:
        case "R":
            snail[0][1] += 1
        case "U":
            snail[0][0] -= 1
        case "L":
            snail[0][1] -= 1
        case "D":
            snail[0][0] += 1
    return snail


def two(puzzle_input: str):  # two took 0.09857180s to execute
    """
    :param puzzle_input:
    :return:
    """
    marks = {}
    snail = [[0, 0] for i in range(10)]
    # total_moves = 0
    for move in puzzle_input.split('\n'):

        for _ in range(int(move.split(' ')[1])):
            # total_moves += 1
            c = snail.count([0, 0])
            # Perform head's movement the number of time
            snail = move_head(snail, move)
            c = snail.count([0, 0])
            if c > 1:
                snail = follower_trails(snail, 0, stop_at=10 - c)  # Perform the recursion on all others
            else:
                snail = follower_trails(snail, 0)
            marks[(snail[9][0], snail[9][1])] = '#'
    return len(marks)
