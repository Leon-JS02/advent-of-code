"""Solution for day 1 of 2021 advent of code."""


def read_input(file_path: str) -> list:
    """Returns a list of integers from a file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [int(line) for line in lines]


def count_number_of_increases(measurements: list[int]) -> int:
    """Counts the number of times a measurement increases compared to the previous one."""
    increases = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            increases += 1
    return increases


day_1_data = read_input('day1_input.txt')
print(count_number_of_increases(day_1_data))
