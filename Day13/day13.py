from aocd.models import Puzzle


def save(data: str, name: str) -> None:
    with open(name, "w+", encoding='utf-8') as f:
        f.write(data)


def load(data) -> list:
    chunks = data.split("\n\n")

    package_chunks = []
    for chunk in chunks:
        split = chunk.split("\n")
        # Put the two chunks as a tuple in a list
        package_chunks.append((eval(split[0]), eval(split[1])))

    return package_chunks


# Returns true if both are equal, None if next value should be checked, False if not equal
def equal(chunk1: list | int, chunk2: list | int) -> bool | None:
    if isinstance(chunk1, list) and isinstance(chunk2, list):
        # Chunks are both lists
        for i in range(len(chunk1)):

            # Check if at end of chunk2
            if i == len(chunk2):
                return False

            # Check if the values are equal at the same index
            res = equal(chunk1[i], chunk2[i])
            if res is not None:
                return res

        # Check if chunks are equally long
        if len(chunk1) == len(chunk2):
            return None
        else:
            return True

    elif isinstance(chunk1, int) and isinstance(chunk2, int):
        # Chunks are both ints
        if chunk1 == chunk2:
            return None
        return chunk1 < chunk2

    elif isinstance(chunk1, list) and isinstance(chunk2, int):
        # Chunk1 is a list and chunk2 is an int
        return equal(chunk1, [chunk2])

    elif isinstance(chunk1, int) and isinstance(chunk2, list):
        # Chunk1 is an int and chunk2 is a list
        return equal([chunk1], chunk2)


def sort(data: list):
    # Sort the list of tuples using bubblesort in place
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if not equal(data[j], data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]


def part1(data: list):
    valid = []
    for i, chunk in enumerate(data):
        # Check if they are equal
        if equal(chunk[0], chunk[1]):
            valid.append(i + 1)

    print("Part 1:", sum(valid))  # 5292


def part2(data: list):
    new_data = []
    for chunk in data:
        new_data.append(chunk[0])
        new_data.append(chunk[1])
    data = new_data

    # Add divider packets
    data.append([2])
    data.append([6])

    # Sort the list of tuples
    sort(data)

    # Get decoder key
    key = (data.index([2]) + 1) * (data.index([6]) + 1)

    print("Part 2:", key)  # 23868


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=13)

    # Store raw data in a file for later
    save(puzzle.input_data, "Day13/puzzle.txt")

    # Execute part1 and part2
    part1(load(puzzle.input_data))
    part2(load(puzzle.input_data))
