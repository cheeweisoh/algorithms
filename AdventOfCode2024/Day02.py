import sys


def check_rep(rep: list[int]) -> int:
    for i in range(1, len(rep)):
        if 0 < rep[i] - rep[i - 1] < 4:
            continue
        else:
            return False
    return True


def check_rep_replacement(rep: list[int]) -> int:
    for i in range(1, len(rep)):
        if 0 < rep[i] - rep[i - 1] < 4:
            continue
        else:
            if any(check_rep(rep[:j] + rep[j + 1 :]) for j in (i - 1, i)):
                continue
            else:
                return False
    return True


def part_one(reports: list[list[int]]) -> int:
    res = 0

    for rep in reports:
        if check_rep(rep) or check_rep(rep[::-1]):
            res += 1

    return res


def part_two(reports: list[list[int]]) -> int:
    res = 0

    for rep in reports:
        if check_rep_replacement(rep) or check_rep_replacement(rep[::-1]):
            res += 1

    return res


input = sys.stdin.read().split(sep="\n")
reports = []
for line in input[:-1]:
    rep = list(map(int, line.split(sep=" ")))
    reports.append(rep)
print(part_one(reports))
print(part_two(reports))
