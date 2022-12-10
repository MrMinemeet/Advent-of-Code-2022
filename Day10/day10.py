from aocd.models import Puzzle


def save(data, name):
    with open(name, "w+", encoding='utf-8') as f:
        f.write(data)


# Executes the instructions and returns a list of all cycles' signal strengths
def execute_code(instructions):
    # Register value for current cycle and it starts with 1
    reg_x = 1
    # Holds the register values for each cycle. Where cycle 0 is reg_x
    cycle = [reg_x]

    # Run through all instructions
    for instruction, value in instructions:
        cycle.append(reg_x)

        if instruction == "addx":
            cycle.append(reg_x)
            reg_x += value

    return cycle


def load(data):
    instructions = []

    for line in data:
        if line.startswith("noop"):
            instructions.append(("noop", None))  # Takes one cycle
        elif line.startswith("addx"):
            instructions.append(("addx", int(line[5:])))  # Takes two cycles
        else:
            raise ValueError("Unknown instruction")

    return instructions


def part1(instructions):
    signals = execute_code(instructions)
    # Calculate the signals at the end
    signal_strength = 0
    for i in range(len(signals)):
        if (i + 20) % 40 == 0:
            signal_strength += i * signals[i]

    print("Part 1:", signal_strength)  # 13680


def part2(instructions):
    print("Part 2:")  # PZGPKPEB but in that "CRT"-font
    signals = execute_code(instructions)

    # Remove the first signal strength as drawing starts at cycle 1
    signals = signals[1:]

    # Get a picture of the signal strength
    i = 0
    for row in range(6):
        for col in range(40):
            # Print the X if the col is in the signal strength range
            if signals[i] - 1 <= col <= signals[i] + 1:
                print("X", end=" ")
            else:
                print(" ", end=" ")
            i += 1
        print()


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=10)

    # Store raw data in a file for later
    save(puzzle.input_data, "Day10/puzzle.txt")

    # Execute part1 and part2
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))
