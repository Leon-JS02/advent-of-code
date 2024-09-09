"""Solution to day 6 of 2021's Advent of Code."""


def load_initial_state(file: str) -> list[int]:
    """Loads the initial state from the filepath."""
    with open(file, 'r', encoding='utf-8') as f:
        line = f.readline()
    return [int(x) for x in line.split(',')]


def tick(states: list[int]) -> list[int]:
    """Simulates a single day."""
    new_states = []
    for i, state in enumerate(states):
        if state > 0:
            states[i] -= 1
        else:
            states[i] = 6
            new_states.append(8)

    return states + new_states


def revised_part_2(initial_state: list[int], num_days: int) -> dict:
    """Revised version of tick to account for exponential growth."""
    state_counts = {i: 0 for i in range(9)}
    for fish in initial_state:
        state_counts[fish] += 1
    for _ in range(num_days):
        new_state_counts = {i: 0 for i in range(9)}
        for i in range(9):
            if i == 0:
                new_state_counts[6] += state_counts[0]
                new_state_counts[8] += state_counts[0]
            else:
                new_state_counts[i - 1] += state_counts[i]
        state_counts = new_state_counts

    return sum(state_counts.values())


if __name__ == "__main__":
    state = load_initial_state('day_6_input.txt')
    num_days = 256
    print(revised_part_2(state, num_days))
