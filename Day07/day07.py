from aocd.models import Puzzle
from FsNode import FsNode

puzzle = Puzzle(year=2022, day=7)

# Store raw data in a file for later
with open("Day07/puzzle.txt", "w", encoding='utf-8') as f:
    f.write(puzzle.input_data)


def load(data):
    root = FsNode("/")  # Start at root node by default

    current_line = 1  # Starting at line 1
    current_dir = root

    while current_line < len(data):
        line = data[current_line]

        if line.startswith("$ cd"):  # Change directory
            # Get the directory name
            dir_name = line.split(" ")[2]
            current_dir = current_dir.cd(dir_name)
            current_line += 1

        elif line.startswith("$ ls"):  # List directory
            current_line += 1

            # Check as long as we're not at the end of the file or the next command
            while current_line < len(data) and not data[current_line].startswith("$"):
                line = data[current_line]

                if line.startswith("dir"):
                    # Get the directory name
                    dir_name = line.split(" ")[1]
                    # Create a new FS_Node object for the directory
                    current_dir.children[dir_name] = current_dir.touch(dir_name)
                else:
                    # Get the file name and size
                    size, file_name = line.split(" ")
                    # Create a new FS_Node object for the file
                    current_dir.children[file_name] = current_dir.touch(file_name, int(size))

                current_line += 1
        else:
            raise ValueError(f"Invalid command: {line}")

    return root


def part1(root):
    MAX_SIZE = 100_000  # 100 KB

    total_size = 0
    # Get the size of each file
    for file in root.get_all_dirs():
        # If the file is not bigger than MAX_SIZE, add it to the total size
        size = file.get_size()
        if size <= MAX_SIZE:
            total_size += size

    print("Part 1:", total_size)  # 1989474


def part2(root):
    DISK_SIZE = 70_000_000  # 70 MB
    UPDATE_SIZE = 30_000_000  # 30 MB

    CURRENT_FREE_SPACE = DISK_SIZE - root.get_size()  # Get current free space

    possible_dirs = []

    # Go over all dirs
    for d in root.get_all_dirs():
        # Check if d + CURRENT_FREE_SPACE is bigger than UPDATE_SIZE MB
        if d.get_size() + CURRENT_FREE_SPACE >= UPDATE_SIZE:
            possible_dirs.append(d.get_size())

    print("Part 2:", min(possible_dirs))  # 1111607


if __name__ == "__main__":
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))
