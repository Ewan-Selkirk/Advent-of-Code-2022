from src.base import AdventOfCode

AOC = AdventOfCode().load("input")

cycle = 0
x = 1
values = {}
crt = [["."] * 40] * 6

for line in AOC.input:
    instruction, value = line.split() if len(line.split()) > 1 else (line, None)

    if instruction == "addx":
        for _ in range(2):
            cycle += 1
            values[cycle] = x
        x += int(value)

    else:
        cycle += 1
        values[cycle] = x


print("Part 1")
print(sum([list(values.values())[i - 1] * i for i in [20, 60, 100, 140, 180, 220]]))

print()
print("Part 2")
[print(''.join(l)) for l in crt]
