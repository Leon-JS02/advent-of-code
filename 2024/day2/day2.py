"""Solution to day 2 of 2024's advent of code."""


def read_input(file_path: str) -> list[list[int]]:
    """Returns a list of reports, with each report consisting of 5 levels."""
    with open(file_path, 'r', encoding="UTF-8") as f:
        return [[int(x) for x in line.strip().split(" ")] for line in f]


def report_is_safe(report: list[int]) -> bool:
    """Returns True if a report is 'safe'."""
    if not (report == sorted(report) or
            report == sorted(report, reverse=True)):
        return False

    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if diff < 1 or diff > 3:
            return False

    return True


def report_is_safe_2(report: list[int]) -> bool:
    if report_is_safe(report):
        return True
    for i in range(len(report)):
        changed_report = report[:i] + report[i+1:]
        if report_is_safe(changed_report):
            return True
    return False


if __name__ == "__main__":
    reports = read_input("day2_input.txt")
    num_safe_reports = sum(report_is_safe(x) for x in reports)
    print(f"Number of safe reports: {num_safe_reports}")
    num_safe_2 = sum(report_is_safe_2(x) for x in reports)
    print(f"Number of safe reports with leniency: {num_safe_2}")
