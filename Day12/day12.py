from aocd.models import Puzzle
import numpy as np
import networkx as nx


def save(data: str, name: str) -> None:
    with open(name, "w+", encoding='utf-8') as f:
        f.write(data)


def load(data) -> np.array:
    array = []
    for line in data.splitlines():
        # Convert to list of chars
        array.append(list(line))

    # Convert array of chars to an array of ints
    for y, rows in enumerate(array):
        for x, col in enumerate(rows):
            array[y][x] = ord(col)

    array = np.array(array)
    return array


def get_start_end(heightmap: np.array):
    start = None
    end = None

    for y, rows in enumerate(heightmap):
        for x, col in enumerate(rows):
            if col == ord('S'):
                start = (y, x)
            elif col == ord('E'):
                end = (y, x)

    if start is None or end is None:
        raise Exception("Start or end not found")

    return start, end


def generate_graph(heightmap: np.array):
    # Obviously there is a module for that in python. Created that myself before cleanup 😅
    graph = nx.DiGraph()  # Create directed graph

    # Go through all points in the heightmap and create a graph
    for x in range(heightmap.shape[0]):
        for y in range(heightmap.shape[1]):
            pos = (x, y)
            cur = heightmap[pos]

            # For each direction, check if the next position is valid
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Up, down, right, left
            for direction in directions:
                next_pos = (pos[0] + direction[0], pos[1] + direction[1])

                # Check if any next pos is out of bounds
                if next_pos[0] < 0 or next_pos[0] >= heightmap.shape[0] or next_pos[1] < 0 or next_pos[1] >= \
                        heightmap.shape[1]:
                    continue

                # Check if the next position is at most 1 larger
                if cur <= heightmap[next_pos] + 1:
                    # Add edge to graph
                    graph.add_edge(next_pos, pos)

    return graph


def part1(heightmap: np.array):
    start, end = get_start_end(heightmap)

    # Set starting and end point values into heightmap starting at the lowest going up to highest
    heightmap[start] = ord('a')
    heightmap[end] = ord('z')

    graph = generate_graph(heightmap)

    print("Part 1:", nx.shortest_path_length(graph, start, end))  # 490


def part2(heightmap: np.array):
    start, end = get_start_end(heightmap)

    # Set starting and end point values into heightmap starting at the lowest going up to highest
    heightmap[start] = ord('a')
    heightmap[end] = ord('z')

    graph = generate_graph(heightmap)

    # Get all points in heightmap that are ord('a')
    nodes = []
    for node in graph.nodes:
        if heightmap[node] == ord('a'):
            nodes.append(node)

    # Get the shortest path for each starting point
    shortest_paths = []
    for starting_node in nodes:
        if nx.has_path(graph, starting_node, end):
            shortest_paths.append(nx.shortest_path_length(graph, starting_node, end))

    print("Part 2:", min(shortest_paths))  # 488


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=12)

    # Store raw data in a file for later
    save(puzzle.input_data, "Day12/puzzle.txt")

    # Execute part1 and part2
    part1(load(puzzle.input_data))
    part2(load(puzzle.input_data))
