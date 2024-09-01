"""Solves day 3 of 2021's advent of code."""


def find_most_common_bit(inputs: list[str], i: int) -> str:
    """Finds the most common bit (0 or 1) at a given position i in all input strings."""
    count_0 = sum(1 for x in inputs if x[i] == '0')
    # Since it's either 0 or 1, we can use this to get count_1
    count_1 = len(inputs) - count_0
    return '1' if count_1 >= count_0 else '0'


def find_least_common_bit(inputs: list[str], i: int) -> str:
    """Finds the least common bit (0 or 1) at a given position i in all input strings."""
    count_0 = sum(1 for x in inputs if x[i] == '0')
    count_1 = len(inputs) - count_0
    return '0' if count_0 <= count_1 else '1'


def get_all_bits_of_position_n(numbers: list[str], n: int) -> list[int]:
    """Gets all bits of a specific position column-wise."""
    all_bits = [int(x[n]) for x in numbers]
    return all_bits


def invert_binary_string(bin_str: list[int]) -> list[int]:
    """Inverts each bit of a binary string."""
    return [0 if x == 1 else 1 for x in bin_str]


def load_inputs(file_name: str) -> list[str]:
    """Loads the puzzle inputs"""
    with open(file_name, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


def convert_bin_to_dec(bin_num: list[int]):
    """Converts a binary number to decimal."""
    return int(''.join(map(str, bin_num)), 2)


def part_one(inputs: list[str]):
    """Solves part one of the problem."""
    gamma_rate = []
    for i in range(len(inputs[0])):
        gamma_rate.append(find_most_common_bit(
            get_all_bits_of_position_n(inputs, i)))
    epsilon_rate = invert_binary_string(gamma_rate)
    print(f"Gamma Rate: {gamma_rate}\nEpsilon Rate: {epsilon_rate}")
    print(convert_bin_to_dec(gamma_rate) * convert_bin_to_dec(epsilon_rate))


def remove_all_elements(bits: list[str], bit: str, i: int):
    """Removes all elements of the list which do not contain a particular bit at position i."""
    bits[:] = [elem for elem in bits if elem[i] == bit]


def find_o2_gen_rating(inputs: list[str]) -> str:
    """Finds the oxygen generator rating."""
    inputs = inputs.copy()
    i = 0
    while len(inputs) > 1:
        bit = find_most_common_bit(inputs, i)
        remove_all_elements(inputs, bit, i)
        i += 1
    return inputs[0]


def find_co2_scrub_rating(inputs: list[str]) -> str:
    """Finds the CO2 scrubber rating."""
    inputs = inputs.copy()
    i = 0
    while len(inputs) > 1:
        bit = find_least_common_bit(inputs, i)
        remove_all_elements(inputs, bit, i)
        i += 1
    return inputs[0]


def part_two(inputs: list[str]) -> int:
    """Solves part two of the problem by calculating the life support rating."""
    o2_gen_rating = find_o2_gen_rating(inputs)
    co2_scrub_rating = find_co2_scrub_rating(inputs)

    # Convert binary to decimal
    o2_gen_rating = convert_bin_to_dec(o2_gen_rating)
    co2_scrub_rating = convert_bin_to_dec(co2_scrub_rating)
    life_support_rating = o2_gen_rating * co2_scrub_rating
    return life_support_rating


if __name__ == "__main__":
    puzzle_inputs = load_inputs('day3_inputs.txt')
    part_one(puzzle_inputs)
    print(part_two(puzzle_inputs))
