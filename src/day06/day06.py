from src.base import AdventOfCode

AOC = AdventOfCode().load("input")


for index, c in enumerate(AOC.input[0]):
    if len(set(AOC.input[0][index:index + 4])) == 4:
        print("Part 1")
        print(index + 4)
        break

for index, c in enumerate(AOC.input[0]):
    if len(set(AOC.input[0][index:index + 14])) == 14:
        print()
        print("Part 2")
        print(index + 14)
        break
