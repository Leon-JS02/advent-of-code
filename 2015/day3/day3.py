"""Solution to Day 3 of 2015's advent of code."""


def load_input(filename: str) -> list[str]:
    """Loads the puzzle inputs for the day."""
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline()
    return list(line)


def process_direction(direction: str, current_loc: tuple[int, int]) -> tuple[int, int]:
    """Processes a single direction command and returns the new location."""
    x, y = current_loc
    direction_map = {
        "^": lambda x, y: (x, y + 1),
        ">": lambda x, y: (x + 1, y),
        "v": lambda x, y: (x, y - 1),
        "<": lambda x, y: (x - 1, y)
    }
    x, y = current_loc
    new_dir = direction_map[direction](x, y)
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


def extract_unique_locations(locations1: dict, locations2) -> int:
    """Returns the number of unique locations between two dictionaries."""
    total = list(locations1.keys()) + list(locations2.keys())
    return set(total)


def process_direction_string_robo(directions: list[str]) -> dict:
    """Returns a dictionary of house locations for both robo and Santa."""
    santa_list = directions[::2]
    robo_list = directions[1::2]
    santa_visits = process_direction_string(santa_list)
    robo_visits = process_direction_string(robo_list)
    return extract_unique_locations(santa_visits, robo_visits)


if __name__ == "__main__":
    inputs = load_input('day3_inputs.txt')
    house_map = process_direction_string(inputs)
    print(f"Number of houses visited: {len(house_map)}")
    visited_houses = process_direction_string_robo(inputs)
    print(len(visited_houses))
