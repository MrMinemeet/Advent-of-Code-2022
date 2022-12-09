from aocd.models import Puzzle
from parse import parse
import numpy as np

puzzle = Puzzle(year=2022, day=9)

# Store raw data in a file for later
with open("Day09/puzzle.txt", "w", encoding='utf-8') as f:
    f.write(puzzle.input_data)

def load(data):
    movement = []

    for line in data:
        move_data = parse("{direction} {distance}", line.strip())
        movement.append((move_data["direction"], int(move_data["distance"])))

    return movement

# Get how many "fields" a knot visits
def get_visited(movement, knot_amount):
    visited = set()
    # x,y coordinates of the knots
    knots = [(0,0) for _ in range(knot_amount)]

    # Go through all movements
    for direction, steps in movement:
        # Do a move step at a time
        for _ in range(steps):
            # Move head 
            if direction == "U":
                knots[0] = tuple(np.add(knots[0], (0, 1)))
            elif direction == "D":
                knots[0] = tuple(np.add(knots[0], (0, -1)))
            elif direction == "L":
                knots[0] = tuple(np.add(knots[0], (-1, 0)))
            elif direction == "R":
                knots[0] = tuple(np.add(knots[0], (1, 0)))

            # Move the rest of the knots
            for i in range(1, knot_amount):
                # Check if the knot is neighboring the previous knot
                if not is_neighboring(knots[i], knots[i - 1]):
                    # Move knot to the previous knot
                    # Subtract the distance between the knots and add the sign of the vector to the i-th knot
                    knots[i] = tuple(np.add(knots[i], np.sign(np.subtract(knots[i-1], knots[i]))))

            # Store the tail knot in the visited set
            visited.add(knots[-1])

    return len(visited)

def is_neighboring(knot1, knot2):
    return (np.abs(np.subtract(knot1, knot2)) <= 1).all()

def part1(movement):
    print("Part 1:", get_visited(movement, 2)) # 6464

def part2(movement):
    print("Part 2:", get_visited(movement, 10)) # 2604


if __name__ == "__main__":
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))
