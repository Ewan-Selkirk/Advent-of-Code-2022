from src.base import AdventOfCode

AOC = AdventOfCode().load("input")

files = {}
sizes = {}
cwd = []

for line in AOC.input:
    if line.startswith("$"):
        s = line.split()
        if s[1] == "cd":
            if s[2] == "/":
                cwd.append("/")
                files[tuple(cwd)] = {}
                sizes[tuple(cwd)] = 0
            elif s[2] == "..":
                cwd.pop()
            else:
                cwd.append(s[2])
    elif line.startswith("dir"):
        s = line.split()
        files[tuple(cwd + [s[1]])] = {}
        sizes[tuple(cwd + [s[1]])] = 0
    elif line[0].isdigit():
        s = line.split()
        files[tuple(cwd)][s[1]] = int(s[0])
        for d in range(len(cwd)):
            sizes[tuple(cwd[:d + 1])] += int(s[0])

print("Part 1")
print(sum(size for size in sizes.values() if size <= 100000))

print()
print("Part 2")
print(min(size for size in sizes.values() if size >= (30000000 - (70000000 - sizes[("/",)]))))
