"""Solution for day 4 of 2021 advent of code."""


def parse_boards(lines: list[str]) -> list[list[str]]:
    """Parses bingo boards from the given lines."""
    boards = []
    current_board = []
    for line in lines:
        if line.strip() == "":
            boards.append(current_board)
            current_board = []
        else:
            current_board.append(line.split())

    boards.append(current_board)
    return boards


def load_puzzle_inputs(file: str) -> tuple:
    """Returns the numbers to be called, and a list of boards."""
    with open(file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    numbers = [int(x) for x in lines[0].split(',')]
    boards = parse_boards(lines[2:])
    return numbers, boards


def mark_board(board: list[list], num: int) -> list[list[int]]:
    """Marks a given number off a bingo board."""
    num_str = str(num)
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == num_str:
                board[i][j] = "!"

    return board


def call_number(number: int, boards: list[list]):
    """Calls a bingo number."""
    for board in boards:
        mark_board(board, number)


def check_win(board: list[list]) -> bool:
    """Returns true if a board has won."""
    size = len(board[0])
    for row in board:
        if all(cell == "!" for cell in row):
            return True

    for col in range(size):
        if all(board[row][col] == "!" for row in range(size)):
            return True

    return False


def calculate_score(board: list[list], number: int) -> int:
    """Calculates the score of a winning bingo board."""
    return sum(int(num) for row in board for num in row if num != "!") * number


def play_1(numbers: list[int], boards: list) -> int:
    """Simulates the game."""
    for number in numbers:
        call_number(number, boards)
        for board in boards:
            if check_win(board):
                return calculate_score(board, number)
    return 0


def play_2(numbers: list[int], boards: list) -> int:
    """Simulates the game until every board has won."""
    for number in numbers:
        call_number(number, boards)
        winning_boards = [board for board in boards if check_win(board)]
        for board in winning_boards:
            if len(boards) == 1:
                return calculate_score(board, number)
            boards.remove(board)
    return 0


if __name__ == "__main__":
    x, y = load_puzzle_inputs('day_4_inputs.txt')
    print(play_1(x, y))
    print(play_2(x, y))
