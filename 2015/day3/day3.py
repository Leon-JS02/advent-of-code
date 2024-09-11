"""Solution to Day 3 of 2015's advent of code."""


def load_input(filename: str) -> list[str]:
    """Loads the puzzle inputs for the day."""
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline()
    return list(line)


def process_direction(direction: str, current_loc: tuple[int, int]) -> tuple[int, int]:
    """Processes a single direction command and returns the new location."""
    x, y = current_loc
    match direction:
        case "^":
            new_dir = (x, y + 1)
        case ">":
            new_dir = (x + 1, y)
        case "v":
            new_dir = (x, y - 1)
        case "<":
            new_dir = (x - 1, y)
    return new_dir


def process_direction_string(directions: list[str]) -> dict:
    """Returns a dictionary of house location -> num visits."""
    current_location = (0, 0)
    visited_locations = {current_location: 1}
    for direction in directions:
        current_location = process_direction(direction, current_location)
        visited_locations[current_location] = visited_locations.get(
            current_location, 0) + 1
    return visited_locations


if __name__ == "__main__":
    inputs = load_input('day3_inputs.txt')
    house_map = process_direction_string(inputs)
    print(f"Number of houses visited: {len(house_map)}")
