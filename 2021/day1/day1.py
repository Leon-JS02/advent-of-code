"""Solution for day 1 of 2021 advent of code."""


def read_input(file_path: str) -> list:
    """Returns a list of integers from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return [int(line) for line in lines]


def count_number_of_single_increases(measurements: list[int]) -> int:
    """Counts the number of times a measurement increases compared to the previous one."""
    increases = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            increases += 1
    return increases


def count_number_of_window_increases(measurements: list[int]) -> int:
    """Counts the number of times a measurement increases with a sliding window of 3."""
    window_sums = []
    for i in range(len(measurements) - 2):
        window_sums.append(sum([measurements[i],
                           measurements[i+1], measurements[i+2]]))

    return count_number_of_single_increases(window_sums)


day_1_data = read_input('day1_input.txt')
print(count_number_of_single_increases(day_1_data))
print(count_number_of_window_increases(day_1_data))
