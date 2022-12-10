from aocd.models import Puzzle
from parse import parse  # Does the opposite of format()


def save(data, name):
    with open(name, "w+", encoding='utf-8') as f:
        f.write(data)


def load(data):
    new_data = []
    for line in data:
        new_data.append(parse("{:d}-{:d},{:d}-{:d}", line))  # Parses data into a tuple with 4 ints
    return new_data


def part1(data):
    contained = 0
    for from_1, to_1, from_2, to_2 in data:  # from_1-to_1, from_2-to_2
        # Check if one range fully contains the other (first if form1 contains form2, second if form2 contains form1)
        if (from_1 <= from_2 <= to_1 and from_1 <= to_2 <= to_1) or (
                from_2 <= from_1 <= to_2 and from_2 <= to_1 <= to_2):
            contained += 1

    print("Part 1:", contained)


def part2(data):
    overlaps = 0
    for from_1, to_1, from_2, to_2 in data:  # from_1-to_1, from_2-to_2
        # Check if the ranges overlap
        if from_2 <= to_1 and from_1 <= to_2:
            overlaps += 1
    print("Part 2:", overlaps)


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=4)

    # Store raw data in a file for later
    save(puzzle.input_data, "Day04/puzzle.txt")

    # Execute part1 and part2
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))
