from aocd.models import Puzzle


def save(data, name):
    with open(name, "w+", encoding='utf-8') as f:
        f.write(data)


def load(data):
    return data[0]


def chunk(data, size):
    # Split data into chunks of size with a step of 1 between them
    return [data[i:i + size] for i in range(0, len(data), 1)]


def solve(data, size):
    chunks = chunk(data, size)
    for group in chunks:
        if len(group) == len(set(group)):  # Check if all chars in chunk are unique
            return data.index(group) + size


def part1(data):
    print("Part 1:", solve(data, 4))  # 1238


def part2(data):
    print("Part 2:", solve(data, 14))  # 3037


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=6)

    # Store raw data in a file for later
    save(puzzle.input_data, "Day06/puzzle.txt")

    # Execute part1 and part2
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))
