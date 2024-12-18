import sys
from functools import cmp_to_key


def part_one(order: list[list[str]], updates: list[list[str]]) -> int:
    res = 0

    for upd in updates:
        upd_pos = {x: i for i, x in enumerate(upd)}
        valid = True

        for s, e in order:
            if s in upd_pos and e in upd_pos:
                if upd_pos[s] > upd_pos[e]:
                    valid = False
                    break

        if valid:
            res += int(upd[len(upd) // 2])

    return res


def part_two(order: list[list[str]], updates: list[list[str]]) -> int:
    cmp = cmp_to_key(lambda x, y: -([x, y] in order))
    res = 0

    for upd in updates:
        sorted_upd = sorted(upd, key=cmp)
        if upd != sorted_upd:
            res += int(sorted_upd[len(sorted_upd) // 2])

    return res


input = sys.stdin.read().split(sep="\n\n")
order = [o.split(sep="|") for o in input[0].split(sep="\n")][:-1]
updates = [u.split(sep=",") for u in input[1].split(sep="\n")][:-1]
print(part_one(order, updates))
print(part_two(order, updates))
