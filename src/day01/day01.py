from src.base import AdventOfCode


AOC = AdventOfCode().load("input")


index = 0
elves = {}
for line in AOC.input:
    if line != "":
        if index in elves:
            elves[index] += int(line)
        else:
            elves[index] = int(line)
    else:
        index += 1

sorted_elves = dict(sorted(elves.items(), key=lambda item: item[1], reverse=True))

print("Part 1")
print(sorted_elves[0])


print()
print("Part 2")
print(sum(list(sorted_elves)[0:3]))
