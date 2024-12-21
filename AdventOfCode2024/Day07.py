import sys


def dfs(ans: int, comp: list[int], curr_sum, curr_idx, part) -> bool:
    if curr_sum == ans and curr_idx == len(comp):
        return True
    if curr_idx == len(comp):
        return False

    add = dfs(ans, comp, curr_sum + comp[curr_idx], curr_idx + 1, part)
    mult = dfs(ans, comp, curr_sum * comp[curr_idx], curr_idx + 1, part)
    conc = dfs(ans, comp, int(str(curr_sum) + str(comp[curr_idx])), curr_idx + 1, part)

    if part == 1:
        return add or mult
    else:
        return add or mult or conc


def part_one(answers: list[int], components: list[list[int]]) -> int:
    res = 0

    for i in range(len(answers)):
        if dfs(answers[i], components[i], components[i][0], 1, 1):
            res += answers[i]

    return res


def part_two(answers: list[int], components: list[list[int]]) -> int:
    res = 0

    for i in range(len(answers)):
        if dfs(answers[i], components[i], components[i][0], 1, 2):
            res += answers[i]

    return res


input = sys.stdin.read().split(sep="\n")
answers = [int(line.split(sep=":")[0]) for line in input[:-1]]
components = [[int(i) for i in line.split(sep=":")[1].split()] for line in input[:-1]]
print(part_one(answers, components))
print(part_two(answers, components))
