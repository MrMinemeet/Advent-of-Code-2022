from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=2)

# Store raw data in a file for later
with open("Day02/puzzle.txt", "w") as f:
    f.write(puzzle.input_data)


# "Enum"s for readability but didn't feel to import something for this
ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 1
DRAW = 2
WIN = 3

# Map for mapping oponent's move to desired move
WIN_MAP = {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK} # Key: opponent, value: me
LOSE_MAP = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER} # Key: opponent, value: me


def load(data):
    newData = []
    for line in data:
        opponent, me = line.split(" ")
        newData.append((convToPoints(opponent), convToPoints(me)))

    return newData

def convToAppropMove(opponent, outcome):
    if outcome == WIN:
        return WIN_MAP[opponent]
    elif outcome == LOSE:
        return LOSE_MAP[opponent]
    else:
        return opponent

def convToPoints(letter):
    # Rock 		1 A X
    # Paper 	2 B Y
    # Scissors 	3 C Z
    if letter == "A" or letter == "X":
        return 1
    elif letter == "B" or letter == "Y":
        return 2
    elif letter == "C" or letter == "Z":
        return 3
    else:
        raise Exception("Unknown letter")


# Tie condition: opponent == me
# Win condition: ROCK == PAPER, PAPER == SCISSORS, SCISSORS == ROCK
# Lose condition: everything else
def calcResult(opponent, me):
    # Draw
    if opponent == me:
        return 3
    # Wins
    elif opponent == ROCK and me == PAPER:
        return 6
    elif opponent == PAPER and me == SCISSORS:
        return 6
    elif opponent == SCISSORS and me == ROCK:
        return 6
    # Losses
    else:
        return 0


# Part 1
def part1(data):
    points = 0
    for opponent, me in data:
        points += calcResult(opponent, me) + me # gameRes + me

    print("Part one:", points) # 15422


# Part 2
def part2(data):
    points = 0
    for opponent, outcome in data:
        me = convToAppropMove(opponent, outcome)
        points += calcResult(opponent, me) + me # gameRes + me

    print("Part two:", points) # 15442, yes it's the same as part 1 with my input




if __name__ == "__main__":
    part1(load(puzzle.input_data.splitlines()))
    part2(load(puzzle.input_data.splitlines()))