from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)

# Store raw data in a file
with open("Day01/puzzle.txt", "w", encoding='utf-8') as f:
    f.write(puzzle.input_data)


def load(data):
    new_data = []
    for line in data:
        new_data.append(line.strip())

    return new_data


def get_calories(data):
    sums = []
    curSum = 0
    for i, line in enumerate(data):
        if line == '' or i == (len(data) - 1):
            sums.append(curSum)
            curSum = 0
        else:
            curSum += int(line)

    return sums


def part1(data):
    print("Part one:", max(get_calories(data)))  # 66487


def part2(data):
    calories = get_calories(data)
    calories.sort(reverse=True)
    print("Part two:", sum(calories[:3]))  # 197301


if __name__ == "__main__":
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))
