"""Solution to 2015's Day 2 of Advent of Code"""


def get_dimensions_from_string(dim_str: str) -> list[int]:
    """Gets the dimensions from a string."""
    dimensions = dim_str.split("x")
    return [int(x) for x in dimensions]


def calculate_area_of_smallest_side(dims: list[int]) -> int:
    """Returns the area of the smallest side."""
    dims.remove(max(dims))
    return dims[0] * dims[1]


def calculate_surface_area(dims: list[int]) -> int:
    """Returns the surface area of the dimensions."""
    surface = 2 * (dims[0] * dims[1])
    surface += 2 * (dims[1] * dims[2])
    surface += 2 * (dims[0] * dims[2])
    return surface


def calculate_paper_needed(dim_str: str) -> int:
    """Calculates the amount of paper needed to wrap the present."""
    dimensions = get_dimensions_from_string(dim_str)
    surface = calculate_surface_area(dimensions)
    surface += calculate_area_of_smallest_side(dimensions)
    return surface


def load_inputs(file_name: str) -> list[str]:
    """Loads the inputs."""
    with open(file_name, "r", encoding="utf-8") as file:
        return file.readlines()


def get_shortest_length_around_sides(dims: list[int]) -> int:
    """Gets the length of the shortest path around the sides of the gift."""
    dims.remove(max(dims))
    return (2 * dims[0]) + (2 * dims[1])


def get_length_of_ribbon(dims: list[int]) -> int:
    """Gets the length of the ribbon needed."""
    return dims[0] * dims[1] * dims[2]


def calculate_total_ribbon_needed(dims_str: str) -> int:
    """Calculates the total ribbon needed."""
    dims = get_dimensions_from_string(dims_str)
    return get_length_of_ribbon(dims) + get_shortest_length_around_sides(dims)


if __name__ == "__main__":
    puzzle_inputs = load_inputs('day2_inputs.txt')
    total_paper = 0
    for line in puzzle_inputs:
        total_paper += calculate_paper_needed(line)
    print(total_paper)
    total_ribbon = 0
    for line in puzzle_inputs:
        total_ribbon += calculate_total_ribbon_needed(line)
    print(total_ribbon)
