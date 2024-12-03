import re


def load_input(file_name: str) -> str:
    """Returns the puzzle input as a string."""
    with open(file_name, 'r', encoding="UTF-8") as f:
        content = f.readlines()
    return "".join(content)


def find_all_muls(text: str) -> list[tuple]:
    """Returns a list of mul tuples in the input string."""
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, text)
    return matches


def parse_instructions(text: str) -> list[str]:
    """Extracts only the valid instructions (do, don't, mul)."""
    pattern = r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)'
    return re.findall(pattern, text)


def sum_valid_muls(instructions: list[str]) -> int:
    """Processes instructions and returns the sum of valid mul products."""
    enabled = True
    total_sum = 0

    for i in instructions:
        if i == "do()":
            enabled = True
        elif i == "don't()":
            enabled = False
        elif enabled and i.startswith("m"):
            nums = re.findall(r'\d{1,3}', i)
            total_sum += int(nums[0]) * int(nums[1])

    return total_sum


def sum_muls(muls: list[tuple]) -> int:
    """Returns the sum of the multiplication tuples."""
    return sum(int(mul[0]) * int(mul[1]) for mul in muls)


if __name__ == "__main__":
    inputs = load_input("day3_input.txt")
    muls_tuples = find_all_muls(inputs)
    print(f"Sum of all 'mul' instructions: {sum_muls(muls_tuples)}")
    instrs = parse_instructions(inputs)
    valid_mul_sum = sum_valid_muls(instrs)
    print(f"Sum of all valid 'mul' instructions: {valid_mul_sum}")
