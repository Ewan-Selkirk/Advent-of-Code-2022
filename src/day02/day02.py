from src.base import AdventOfCode


AOC = AdventOfCode().load("input")

rock, paper, scissors = 1, 2, 3
draw, win = 3, 6

rps = {}
score = {}
wol = {}


def letter_to_value(letter: str) -> int:
    if letter in ['A', 'X']:
        return rock
    elif letter in ['B', 'Y']:
        return paper
    elif letter in ['C', 'Z']:
        return scissors


def calculate_score(turn: dict, index: int):
    if (turn['player'] == turn['elf'] + 1) or (turn['player'] == 1 and turn['elf'] == 3):
        score[index] = turn['player'] + win
    elif turn['elf'] == turn['player']:
        score[index] = turn['player'] + draw
    else:
        score[index] = turn['player']


def calculate_win(turn: dict, index: int):
    if turn['player'] == 1:
        wol[index] = (turn['elf'] - 1) if turn['elf'] != 1 else 3
    elif turn['player'] == 2:
        wol[index] = turn['elf'] + draw
    else:
        wol[index] = ((turn['elf'] + 1) if turn['elf'] != 3 else 1) + win


for count, line in enumerate(AOC.input):
    values = str(line).split(" ")

    rps[count] = {'elf': letter_to_value(values[0]), 'player': letter_to_value(values[1])}
    calculate_score(rps[count], count)
    calculate_win(rps[count], count)


print(rps)
print(wol)


print("Part 1:")
print(sum(score.values()))

print()
print("Part 2:")
print(sum(wol.values()))
