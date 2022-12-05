from src.base import AdventOfCode

AOC = AdventOfCode().load("input")


crates = {}


def parse_instruction(instruction: str, partOne: bool):
    inst = instruction.split()
    count, was, to = [int(x) for x in inst[1::2]]

    if partOne:
        for i in range(count):
            crates[to].append(crates[was].pop())
    else:
        if len(crates[was]) >= count:
            to_append = crates[was][-count:]
            for elem in to_append:
                crates[to].append(elem)
            del crates[was][-count:]
        elif len(crates[was]) != 0:
            to_append = crates[was][-len(crates[was]):]
            for elem in to_append:
                crates[to].append(elem)
            del crates[was][-count:]

for count, line in enumerate(AOC.input):
    try:
        if line[1].isdigit():
            for i in line.split():
                crates[int(i)] = []

            for i in range(count - 1, -1, -1):
                c = [AOC.input[i][e:e + 3] for e in range(0, len(AOC.input[i]), 4)]

                for index, e in enumerate(c):
                    if e != '   ':
                        crates[index + 1].append(e)
        elif line.startswith("move"):
            parse_instruction(line, True)
    except IndexError as e:
        pass

print("Part 1")
print(crates)
print(''.join([x[-1][1] for x in crates.values()]))

crates = {}

for count, line in enumerate(AOC.input):
    try:
        if line[1].isdigit():
            for i in line.split():
                crates[int(i)] = []

            for i in range(count - 1, -1, -1):
                c = [AOC.input[i][e:e + 3] for e in range(0, len(AOC.input[i]), 4)]

                for index, e in enumerate(c):
                    if e != '   ':
                        crates[index + 1].append(e)
        elif line.startswith("move"):
            parse_instruction(line, False)
    except IndexError as e:
        pass

print()
print("Part 2")
print(crates)
print(''.join([x[-1][1] for x in crates.values()]))
