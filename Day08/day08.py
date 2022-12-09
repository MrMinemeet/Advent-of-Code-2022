from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2022, day=8)

# Store raw data in a file for later
with open("Day08/puzzle.txt", "w", encoding='utf-8') as f:
    f.write(puzzle.input_data)


def load(data):
    # Load into an np array
    return np.array([list(line.strip()) for line in data])


# Checks if a given point is visible from the border
# This means nothing bigger obstructs the view
def is_visible_from_border(data, x, y):
    # Check if the point is on the border
    if x == 0 or x == data.shape[0] - 1 or y == 0 or y == data.shape[1] - 1:
        return True

    # Look in all directions

    # Look from point to "north"
    for i in range(x - 1, -1, -1):
        # Check if the tree is obstructing the view
        if data[i, y] >= data[x, y]:
            # If it is, break
            break
    else:
        # If we didn't break, the point is visible
        return True

    # Look from point to "south"
    for i in range(x + 1, data.shape[0]):
        # Check if the tree is obstructing the view
        if data[i, y] >= data[x, y]:
            # If it is, break
            break
    else:
        # If we didn't break, the point is visible
        return True

    # Look from point to "west"
    for i in range(y - 1, -1, -1):
        # Check if the tree is obstructing the view
        if data[x, i] >= data[x, y]:
            # If it is, break
            break
    else:
        # If we didn't break, the point is visible
        return True

    # Look from point to "east"
    for i in range(y + 1, data.shape[1]):
        # Check if the tree is obstructing the view
        if data[x, i] >= data[x, y]:
            # If it is, break
            break
    else:
        # If we didn't break, the point is visible
        return True

    # The point is not visible
    return False


def get_view_distance(data, x, y):
    scenic_score = 1
    # Check each direction and calculate how far we can see

    # North
    count = 0
    for i in range(x - 1, -1, -1):
        count += 1
        # Check if the tree is obstructing the view
        if data[i, y] >= data[x, y]:
            # If it is, break
            break

    scenic_score *= count

    # South
    count = 0
    for i in range(x + 1, data.shape[0]):
        count += 1
        # Check if the tree is obstructing the view
        if data[i, y] >= data[x, y]:
            # If it is, break
            break

    scenic_score *= count

    # West
    count = 0
    for i in range(y - 1, -1, -1):
        count += 1
        # Check if the tree is obstructing the view
        if data[x, i] >= data[x, y]:
            # If it is, break
            break

    scenic_score *= count

    # East
    count = 0
    for i in range(y + 1, data.shape[1]):
        count += 1
        # Check if the tree is obstructing the view
        if data[x, i] >= data[x, y]:
            # If it is, break
            break

    scenic_score *= count

    return scenic_score


def part1(data):
    visible = 0

    # Check each point
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            # Check if the point is visible from the border
            if is_visible_from_border(data, x, y):
                visible += 1

    print("Part 1:", visible)  # 1854


def part2(data):
    considerations = []

    # Check each point
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            considerations.append(get_view_distance(data, x, y))

    print("Part 2:", max(considerations))  # 527340


if __name__ == "__main__":
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))
