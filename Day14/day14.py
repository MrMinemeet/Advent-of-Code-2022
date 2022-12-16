from aocd.models import Puzzle
import numpy as np
from parse import parse

AIR = '.'
ROCK = '#'
SAND = 'o'


def save(data: str, name: str) -> None:
    with open(name, "w+", encoding='utf-8') as f:
        f.write(data)


def print_cave(cave) -> None:
    for row in cave:
        print("".join(row))


def drop_sand(cave: np.array, x: int = 500, y: int = 0) -> bool:
    """
    Drops sand from the given position and returns true if the sand was placed successfully
    """

    # Check if sand piled up to sand source
    if cave[y, x] == SAND:
        return False

    # Get the max height and width of the cave
    max_height, max_width = cave.shape

    # Go down and check if for next place
    while y + 1 < max_height:
        if cave[y + 1, x] == AIR:
            # Move straight down
            y += 1

        elif x > 0 and cave[y + 1, x - 1] == AIR:
            # Move left down if air and not at left edge
            x -= 1
            y += 1

        elif x + 1 < max_width and cave[y + 1, x + 1] == AIR:
            # Move right down if air and not at right edge
            x += 1
            y += 1
        else:
            # Blocked
            break

    # Check if it is at the bottom of the cave
    if y + 1 >= max_height:
        # Fell into the void
        return False

    # Was placed somewhere
    cave[y, x] = SAND
    return True


def load(data) -> np.array:
    # Contains the extracted paths (a list of points it goes through)
    paths = []
    for path in data.splitlines():
        # Split the path into each line
        lines = path.split("->")
        # Get the coordinates of each point in the path
        point_coord = []
        for line in lines:
            # Get the coordinates of the point
            point_coord.append(parse("{:d},{:d}", line.strip()).fixed)
        paths.append(point_coord)

    # Get max x and y
    max_x = float("-inf")
    for path in paths:
        for point in path:
            max_x = max(max_x, point[0])
    max_y = float("-inf")
    for path in paths:
        for point in path:
            max_y = max(max_y, point[1])

    # Create cave map as matrix filled with air
    # Do extra 500 columns to be sure it won't hit a wall (as drop-off is 500 by default)
    cave_map = np.full((max_y + 1, max_x + 500), AIR, dtype=str)

    # Fill in the cave map with the paths
    for path in paths:
        # Add path to cave map
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            # Get the direction of the path
            x1, x2 = sorted((x1, x2))
            y1, y2 = sorted((y1, y2))

            # Fill in the path from (y1 to y2 + 1) and (x1 to x2 + 1)
            cave_map[y1: y2 + 1, x1: x2 + 1] = ROCK

    return cave_map


def part1(cave_map: np.array):
    successful_drops = 0
    while drop_sand(cave_map):
        successful_drops += 1

    print(f"Part 1: {successful_drops}")  # 1133


def part2(cave_map: np.array):
    # Add two extra rows to the bottom of the cave map
    cave_map = np.pad(cave_map, ((0, 2), (0, 0)), 'constant', constant_values=AIR)

    # Set bottom row to rock
    cave_map[-1, :] = ROCK

    # Drop sand until it can't drop anymore
    successful_drops = 0
    while drop_sand(cave_map):
        successful_drops += 1

    print(f"Part 2: {successful_drops}")  # 27566


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=14)

    # Store raw data in a file for later
    save(puzzle.input_data, "Day14/puzzle.txt")

    # Execute part1 and part2
    part1(load(puzzle.input_data))
    part2(load(puzzle.input_data))
