from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=3)

# Store raw data in a file for later
with open("Day03/puzzle.txt", "w", encoding='utf-8') as f:
    f.write(puzzle.input_data)


def load(data):
    newData = []
    for line in data:
        newData.append(line.strip())

    return newData

def convertToPriority(letter):
    # Converts a letter to a priority
    # lowercase -> 1 - 26
    # uppercase -> 27 - 52
    if('a' <= letter <= 'z'):
        return ord(letter) - 96
    elif('A' <= letter <= 'Z'):
        return ord(letter) - 38
    else:
        raise Exception("Unknown letter")

def findInBoth(list1, list2):
    # Returs a list of items that are in both lists
    return list(set(list1) & set(list2))


def part1(data):
    sumOfPriorities = 0

    for line in data:
        # Split line into two equal parts
        firstHalf = line[:len(line)//2]
        secondHalf = line[len(line)//2:]

        # Chec kfor duplicates in both halves
        duplicates = findInBoth(firstHalf, secondHalf)

        # Add the priorities of the duplicates
        for duplicate in duplicates:
            sumOfPriorities += convertToPriority(duplicate)

    print("Part 1:", sumOfPriorities)


def part2(data):
    sumOfPriorities = 0

    # Group data to 3 line chunks
    newData = []
    for i in range(0, len(data), 3):
        newData.append(data[i:i+3])
        
    for chunk in newData:
        # Find the duplicates in the three lines
        duplicates = findInBoth(chunk[0], chunk[1])
        duplicates = findInBoth(duplicates, chunk[2])

        # Add the priorities of the duplicates
        for duplicate in duplicates:
            sumOfPriorities += convertToPriority(duplicate)
    

    print("Part 2:", sumOfPriorities)



if __name__ == "__main__":
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))