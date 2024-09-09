"""Solution to day 2 of 2021's Advent of Code."""


def read_input(file_path: str) -> list[str]:
    """Processes and returns the input for day 2."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()


def process_command(command: str, magnitude: int,
                    current_h: int, current_d: int) -> tuple:
    """Processes a command and returns the resulting horizontal
    and depth. current_h: current height current_d: current depth"""
    if command == 'forward':
        current_h += magnitude
    elif command == 'down':
        current_d += magnitude
    else:
        current_d -= magnitude

    return (current_h, current_d)


def process_command_revised(command, magnitude, aim, h, d):
    """Revised version of process command for part two,"""
    if command == 'down':
        aim += magnitude
    elif command == 'up':
        aim -= magnitude
    else:
        h += magnitude
        d += (aim * magnitude)

    return (aim, h, d)


def split_command(command: str) -> tuple:
    """Splits a command string into a separate command and magnitude."""
    command, magnitude = command.split(" ")
    return (command, int(magnitude))


def part_one(commands: list[str]) -> int:
    """Solves the first part of day 2."""
    current_h = 0
    current_d = 0
    for command in commands:
        c, m = split_command(command)
        current_h, current_d = process_command(c, m, current_h, current_d)
    return current_h * current_d


def part_two(commands: list[str]) -> int:
    """Solves the second part of day 2."""
    current_h = current_d = aim = 0
    for command in commands:
        c, m = split_command(command)
        aim, current_h, current_d = process_command_revised(
            c, m, aim, current_h, current_d)
    return current_h * current_d


if __name__ == "__main__":
    inputs = read_input('day2-input.txt')
    print(part_one(inputs))
    print(part_two(inputs))
