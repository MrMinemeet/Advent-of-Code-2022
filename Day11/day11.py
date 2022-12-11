from aocd.models import Puzzle
from Monkey import Monkey
from parse import parse
import numpy as np

PRINT = False


def save(data, name):
    with open(name, "w+", encoding='utf-8') as f:
        f.write(data)


def load(data: str) -> list:
    monkeys = []

    monkey_blocks = []
    monkey_block = ""
    for line in data:
        if line == "":
            monkey_blocks.append(monkey_block)
            monkey_block = ""
        else:
            monkey_block += line + "\n"

    # For the last monkey (no empty line at the end)
    monkey_blocks.append(monkey_block)

    for monkey_block in monkey_blocks:
        lines = monkey_block.splitlines()
        name = parse("Monkey {:d}:", lines[0].strip()).fixed[0]
        items = parse("Starting items: {}", lines[1].strip()).fixed[0]
        operation = parse("Operation: {}", lines[2].strip()).fixed[0]
        condition = parse("Test: divisible by {:d}", lines[3].strip()).fixed[0]
        if_true = parse("If true: throw to monkey {:d}", lines[4].strip()).fixed[0]
        if_false = parse("If false: throw to monkey {:d}", lines[5].strip()).fixed[0]

        operation = operation.split("=")[1].strip()
        items = [int(item) for item in items.split(", ")]

        monkeys.append(Monkey(name, items, operation, (condition, if_true, if_false)))

    return monkeys


def calculate_monkey_business(monkeys: list, rounds: int, divisor: int, mod: int = None) -> int:
    # Counter for each monkey for how often they inspect an item
    counter = [0] * len(monkeys)

    # Do each round
    for curr_round in range(rounds):
        # Do each Monkey's turn for this round
        for monkey in monkeys:
            if PRINT:
                print(f"After round {curr_round + 1}, the monkeys are holding items with these worry levels:")

            # Do as long as the monkey has items
            while len(monkey.items) > 0:
                # Monkey takes first item from his "inventory"
                item = monkey.items.pop(0)

                # Monkey inspects item
                operation = monkey.operation.replace("old", str(item))  # Replace old with the actual worry level
                item = eval(operation)
                counter[monkey.name] += 1

                # Monkey doesn't damage item
                item = int(item / divisor)
                if mod is not None:
                    item = item % mod

                # Monkey throws item to next monkey
                test_result = (item % monkey.test[0]) == 0
                if test_result:
                    monkeys[monkey.test[1]].items.append(item)
                else:
                    monkeys[monkey.test[2]].items.append(item)

                if PRINT:
                    print(f"\tMonkey {monkey.name}: {monkey.items}")

    # Multiply the two most active monkeys
    monkey1, monkey2 = np.sort(counter)[-2:]
    return monkey1 * monkey2


def part1(monkeys: list):
    print("Part 1:", calculate_monkey_business(monkeys, 20, 3))  # 61503


def part2(monkeys: list):
    # Get the least common multiple of the test conditions. Makes the calculation much faster
    lcm = np.lcm.reduce([monkey.test[0] for monkey in monkeys])

    print("Part 2:", calculate_monkey_business(monkeys, 10000, 1, lcm))  # 14081365540


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=11)

    # Store raw data in a file for later
    save(puzzle.input_data, "Day11/puzzle.txt")

    # Execute part1 and part2
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))
