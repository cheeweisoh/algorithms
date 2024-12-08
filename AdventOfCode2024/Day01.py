import sys


def part_one(lst1: list[int], lst2: list[int]) -> int:
    res = 0

    for i in range(len(lst1)):
        res += abs(lst1[i] - lst2[i])

    return res


def part_two(lst1: list[int], lst2: list[int]) -> int:
    res = 0
    counts = {}

    for i in lst2:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    for j in lst1:
        if j in counts:
            res += j * counts[j]

    return res


input = sys.stdin.read().split(sep="\n")
left, right = [], []
for s in input[:-1]:
    l, r = s.split("   ")
    left.append(int(l))
    right.append(int(r))
left.sort()
right.sort()
print(part_one(left, right))
print(part_two(left, right))
