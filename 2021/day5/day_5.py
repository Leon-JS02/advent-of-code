"""Solution to 2021 day 5 advent of code."""


def load_puzzle_input(file: str) -> list[str]:
    """Returns a list of lines from the puzzle input."""
    with open(file, 'r', encoding='utf-8') as f:
        return [x.strip() for x in f.readlines()]


def get_x1_y1(line: str) -> tuple:
    """Returns x1 and y1 from a line string."""
    x1y1 = line.split('->')[0]
    x1y1 = x1y1.split(',')

    return (int(x1y1[0]), int(x1y1[1]))


def get_x2_y2(line: str) -> tuple:
    """Returns x2 and y2 from a line string."""
    x2y2 = line.split('->')[1]
    x2y2 = x2y2.split(',')

    return (int(x2y2[0]), int(x2y2[1]))


def draw_line(line: str, line_map: dict) -> dict:
    """Adds a line to the map."""
    x1, y1 = get_x1_y1(line)
    x2, y2 = get_x2_y2(line)
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            line_map[(x1, y)] = line_map.get((x1, y), 0) + 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            line_map[(x, y1)] = line_map.get((x, y1), 0) + 1

    return line_map


if __name__ == "__main__":
    lines = load_puzzle_input('day_5_inputs.txt')
    vent_map = {}
    for l in lines:
        vent_map = draw_line(l, vent_map)
    print(sum([1 for x in vent_map.values() if x >= 2]))
