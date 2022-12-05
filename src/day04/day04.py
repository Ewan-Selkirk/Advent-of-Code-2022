from src.base import AdventOfCode

AOC = AdventOfCode().load("input")

assignments = {}
total = 0

for count, line in enumerate(AOC.input):
    elves = line.split(',')

    assignments[count] = {'first': [x for x in range(int(elves[0].split('-')[0]), int(elves[0].split('-')[1]) + 1)],
                          'second': [x for x in range(int(elves[1].split('-')[0]), int(elves[1].split('-')[1]) + 1)]}

    if set(assignments[count]['first']).issubset(assignments[count]['second']) \
            or set(assignments[count]['second']).issubset(assignments[count]['first']):
        total += 1

print("Part 1")
print(total)


overlap = 0

for i in assignments.values():
    con = True

    for v in i['first']:
        if v in i['second']:
            overlap += 1
            con = False
            break

    if con:
        for v in i['second']:
            if v in i['first']:
                overlap += 1
                break

print()
print("Part 2")
print(overlap)
