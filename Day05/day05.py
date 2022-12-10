from aocd.models import Puzzle
from parse import parse


def save(data, name):
    with open(name, "w+", encoding='utf-8') as f:
        f.write(data)


def load(data):
    stacks = {}  # {stack: [row1, row2, row3, row4]}
    tmp_stack = []
    # Load the stacks only
    for line in data:
        tmp_stack.append(line)
        # Check if empty line
        if len(line) == 0:
            break

    # Calculate width using numbers in last line of tmp_stack
    # -2 because one is empty
    width = len(tmp_stack[len(tmp_stack) - 2].split()) - 1

    # Go through each column number and then move up at that position to get the containers
    for i in range(0, len(tmp_stack[width - 1]) - 1):
        if tmp_stack[width][i] == ' ':
            continue

        stack_number = tmp_stack[width][i]

        # Move up
        # -3 because empty line and so
        for j in range(len(tmp_stack) - 3, -1, -1):
            # Skip empty containers
            if tmp_stack[j][i] == ' ':
                continue

            container = tmp_stack[j][i]

            # Add to stack
            if stack_number in stacks:
                stacks[stack_number].append(container)
            else:
                stacks[stack_number] = [container]

    # Load move data (amount, from, to)
    moves = []
    found = False
    for line in data:
        # Skip the first x lines until an empty line is found
        if len(line) == 0:
            found = True
            continue

        if found:
            moves.append(parse("move {:d} from {:d} to {:d}", line).fixed)

    return stacks, moves


def part1(data):  # Move one container at a time
    stacks = data[0]
    moves = data[1]

    # Do the moves
    for amount, from_, to_ in moves:
        # Do amount times
        for _ in range(0, amount):
            # Get container
            container = stacks[str(from_)].pop()

            # Add to stack
            stacks[str(to_)].append(container)

    # Count containers on top
    containers = ""
    for s in stacks:
        containers += stacks[s][-1]

    print("Part 1:", containers)  # TLFGBZHCN


def part2(data):
    # move all containers at once
    stacks = data[0]
    moves = data[1]

    # Do the moves
    for amount, from_, to_ in moves:
        # Get containers from top
        containers = stacks[str(from_)][-amount:]

        # Remove containers from top of stack
        for _ in range(0, amount):
            stacks[str(from_)].pop()

        # Add to stack
        stacks[str(to_)].extend(containers)

    # Count containers on top
    containers = ""
    for s in stacks:
        containers += stacks[s][-1]

    print("Part 2:", containers)  # QRQFHFWCL


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=5)

    # Store raw data in a file for later
    save(puzzle.input_data, "Day05/puzzle.txt")

    # Execute part1 and part2
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))
