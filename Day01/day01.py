from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)

# Store raw data in a file
with open("Day01/puzzle.txt", "w") as f:
    f.write(puzzle.input_data)

def load(data):
    newData = []
    for line in data:
        newData.append(line.strip())

    return newData

def getCals(data):
    sums = []
    curSum = 0
    for i, line in enumerate(data):
        if line == '' or i == (len(data)-1):
            sums.append(curSum)
            curSum = 0
        else:
            curSum += int(line)

    return sums

def part1(data):
    print("Part one:",max(getCals(data))) # 66487

def part2(data):
    calories = getCals(data)
    calories.sort(reverse=True)
    print("Part two:", sum(calories[:3])) # 197301



if __name__ == "__main__":
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))