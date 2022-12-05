from src.base import AdventOfCode


AOC = AdventOfCode().load("input")


item = {}
priority = {}


def get_item_priority(i: str) -> int:
    if i.isupper():
        return ord(i) - 38
    else:
        return ord(i) - 96


for count, line in enumerate(AOC.input):
    compartments = [line[:len(line)//2], line[len(line)//2:]]

    for i in list(compartments[0]):
        if i in compartments[1]:
            item[count] = i
            break

    for i in item.values():
        priority[count] = get_item_priority(i)

print("Part 1")
print(sum(priority.values()))


item.clear()
priority.clear()
groups = [AOC.input[i:i + 3] for i in range(0, len(AOC.input), 3)]
for count, g in enumerate(groups):
    for i in list(g[0]):
        if i in list(g[1]) and i in list(g[2]):
            item[count] = i
            break

    for i in item.values():
        priority[count] = get_item_priority(i)


print()
print("Part 2")
print(sum(priority.values()))
