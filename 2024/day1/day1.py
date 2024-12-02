"""Solution to day 1 of 2024's Advent of Code."""


def read_input(file_path: str) -> tuple[list, list]:
    """Reads the input file and returns a tuple of the left and right lists."""
    with open(file_path, 'r', encoding='UTF-8') as f:
        content = [line.strip().split("   ") for line in f]
    first_list, last_list = zip(*content)
    return list(first_list), list(last_list)


def sum_elementwise_difference(l1: list[int], l2: list[int]) -> int:
    """Returns the elementwise sum of the difference between numbers in two sorted lists."""
    diff = 0
    for i in range(len(l1)):
        diff += abs(int(l2[i]) - int(l1[i]))
    return diff


def return_list_frequency(n: int, l2: list[int]) -> int:
    """Returns the number of times n appears in the list."""
    return sum(x == n for x in l2)


def sum_similarity_scores(l1: list[int], l2: list[int]) -> int:
    """Returns the sum of the similarity scores from the two lists."""
    sim = 0
    for i in range(len(l1)):
        sim += int(l1[i]) * return_list_frequency(l1[i], l2)
    return sim


if __name__ == "__main__":
    l1, l2 = read_input('day1_input.txt')
    total_diff = sum_elementwise_difference(sorted(l1), sorted(l2))
    print(f"Total difference: {total_diff}")
    total_sim = sum_similarity_scores(l1, l2)
    print(f"Total similarity score: {total_sim}")
