import sys
import re


def part_one(s: str) -> int:
    r = re.findall(r"mul\((\d+),(\d+)\)", s)

    res = 0
    for a, b in r:
        res += int(a) * int(b)

    return res


def part_two(s: str) -> int:
    r = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", s)

    res = 0
    curr = 1
    for a, b, c in r:
        if a == "don't()":
            curr = 0
        elif a == "do()":
            curr = 1
        else:
            if curr:
                res += int(b) * int(c)

    return res


input = sys.stdin.read().split(sep="\n")[:-1]
s = "".join(input)
print(part_one(s))
print(part_two(s))
