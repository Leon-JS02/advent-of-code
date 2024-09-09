"""Solution to day 1 of 2015's Advent of Code."""


def load_inputs(filepath: str) -> list[str]:
    """Returns the puzzle inputs."""
    with open(filepath, "r", encoding='utf-8') as f:
        line = f.readline()
    return list(line)


def building_floor(floors: list[str]) -> int:
    """Returns the building floor from a list of instructions."""
    current_floor = 0
    for floor in floors:
        current_floor += 1 if floor == '(' else -1
    return current_floor


def first_basement_entrance(floors: list[str]) -> int:
    """Returns the position of the character which first causes
    entrance into the basement."""
    current_floor = 0
    position = 0
    for floor in floors:
        position += 1

        if floor == '(':
            current_floor += 1
        elif floor == ')':
            current_floor -= 1

        if current_floor == -1:
            return position

    return -1


if __name__ == "__main__":
    inputs = load_inputs('day1_input.txt')
    print(building_floor(inputs))
    print(first_basement_entrance(inputs))
