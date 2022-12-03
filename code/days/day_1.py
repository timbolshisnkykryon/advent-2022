def my_solver(puzzle_input: str):
    """
    Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    :param puzzle_input: list represents the Calories of the food carried by Elves
    :return: Highest calories sum
    """
    highest = 0
    current_sum = 0
    for calories in puzzle_input.split('\n'):
        # Go on every calorie amount
        if not calories:
            if current_sum > highest:
                highest = current_sum
            current_sum = 0
        else:
            current_sum += int(calories)
    return highest