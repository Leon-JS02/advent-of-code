"""Solution to day 7 of 2021's advent of code."""


def load_puzzle_input(file: str) -> list[int]:
    """Loads the puzzle input as an array of integers."""
    with open(file, 'r', encoding='utf-8') as f:
        return [int(x) for x in f.readline().split(',')]


def find_midpoint(data: list[int]) -> int:
    """Finds the midpoint of the data."""
    data.sort()
    return data[len(data)//2]


def find_minimum_cost(data: list[int]) -> int:
    """Solution to part 1."""
    midpoint = find_midpoint(data)
    fuel = 0
    for crab in data:
        fuel += abs(midpoint - crab)
    return fuel


if __name__ == "__main__":
    inputs = load_puzzle_input('day_7_input.txt')
    print(find_minimum_cost(inputs))
