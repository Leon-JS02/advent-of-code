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


if __name__ == "__main__":
    inputs = load_inputs('day1_input.txt')
    print(building_floor(inputs))
