"""Solution to day 7 of 2021's advent of code."""


def load_puzzle_input(file: str) -> list[int]:
    """Loads the puzzle input as an array of integers."""
    with open(file, 'r', encoding='utf-8') as f:
        return [int(x) for x in f.readline().split(',')]


def find_midpoint(data: list[int]) -> int:
    """Finds the midpoint of the data."""
    data.sort()
    return data[len(data)//2]


def calculate_fuel_needed(crab_position: int, point: int) -> int:
    """Calculates the amount of fuel needed to move a crab's
    position from one point to another."""
    distance = abs(crab_position - point)
    fuel_cost = (distance * (distance + 1)) // 2
    return fuel_cost


def find_minimum_cost(data: list[int]) -> int:
    """Solution to part 1."""
    midpoint = find_midpoint(data)
    fuel = 0
    for crab in data:
        fuel += calculate_fuel_needed(crab, midpoint)
    return fuel


if __name__ == "__main__":
    inputs = load_puzzle_input('day_7_input.txt')
    print(find_minimum_cost(inputs))
    print(calculate_fuel_needed(16, 5))
