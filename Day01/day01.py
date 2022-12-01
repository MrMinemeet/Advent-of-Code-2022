from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)

raw_data = puzzle.input_data

# Store raw data in a file
with open("Day01/puzzle.txt", "w") as f:
    f.write(raw_data)


data = raw_data.split("\n")

for i, d in enumerate(data):
    data[i] = data[i].strip()


sums = []
curSum = 0
for i, line in enumerate(data):
    if line == '' or i == (len(data)-1):
        sums.append(curSum)
        curSum = 0
    else:
        curSum += int(line)

print("Part one:",max(sums)) # 66487

sums.sort(reverse=True)
print("Part two:", sum(sums[:3])) # 197301

