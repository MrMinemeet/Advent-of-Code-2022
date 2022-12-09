from aocd.models import Puzzle
from parse import parse

puzzle = Puzzle(year=2022, day=5)

# Store raw data in a file for later
with open("Day05/puzzle.txt", "w", encoding='utf-8') as f:
    f.write(puzzle.input_data)

def load(data):
    stacks = {} # {stack: [row1, row2, row3, row4]}
    tmpstack = []
    # Load the stacks only
    for line in data:
        tmpstack.append(line)
        # Check if empty line
        if len(line) == 0:
            break

    # Calculate width using numbers in last line of tmpstack
    # -2 because one is empty
    width = len(tmpstack[len(tmpstack) - 2].split()) - 1

    # Go through each column number and then move up at that posision to get the containers
    for i in range(0, len(tmpstack[width - 1]) - 1):
        if tmpstack[width][i] == ' ':
            continue

        stacknumber = tmpstack[width][i]

        # Move up
        # -3 because empty line and so
        for j in range(len(tmpstack) - 3, -1, -1):
            # Skip empty containers
            if tmpstack[j][i] == ' ':
                continue

            container = tmpstack[j][i]

            # Add to stack
            if stacknumber in stacks:
                stacks[stacknumber].append(container)
            else:
                stacks[stacknumber] = [container]

    # Load move data (amount, from, to)
    moves = []
    found = False
    for line in data:
        # Skip the first x lines until a empty line is found
        if len(line) == 0:
            found = True
            continue

        if found:
            moves.append(parse("move {:d} from {:d} to {:d}", line).fixed)

    return (stacks, moves)


def part1(data): # Move one container at a time
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
    containers =""
    for s in stacks:
        containers += stacks[s][-1]

    print("Part 1:", containers) # TLFGBZHCN

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
    containers =""
    for s in stacks:
        containers += stacks[s][-1]

    print("Part 2:", containers) # QRQFHFWCL


if __name__ == "__main__":
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))
