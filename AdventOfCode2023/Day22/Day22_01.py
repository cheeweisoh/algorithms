#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict


def parseInput(file: list) -> list[list[list[int]]]:
    bricks = []

    for line in file:
        start, end = line.split("~")
        start = [int(x) for x in start.split(",")]
        end = [int(x) for x in end.split(",")]

        brick = []
        sx, ex = min(start[0], end[0]), max(start[0], end[0])
        sy, ey = min(start[1], end[1]), max(start[1], end[1])
        sz, ez = min(start[2], end[2]), max(start[2], end[2])
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                for z in range(sz, ez + 1):
                    brick.append([x, y, z])

        bricks.append(brick)

    return sorted(bricks, key=lambda x: x[0][2])


def calcFall(bricks: list[list[list[int]]]) -> dict[tuple[int], int]:
    space = defaultdict(int)
    for idx, brk in enumerate(bricks, start=1):
        for subbrk in brk:
            space[tuple(subbrk)] = idx
    while True:
        fall = False

        for idx, brk in enumerate(bricks, start=1):
            # check that space below current subbrk is empty or same brk and there is still space
            if all(space[x, y, z - 1] in (0, idx) and z > 1 for x, y, z in brk):
                # check that a fall is possible (to start next iteration)
                fall = True

                # set current space to empty
                for subbrk in brk:
                    space[tuple(subbrk)] = 0
                # drop brick down by one
                for i, subbrk in enumerate(brk):
                    subbrk[2] -= 1
                # occupy new space
                for subbrk in brk:
                    space[tuple(subbrk)] = idx

        if not fall:
            break
    return space


def findSupports(bricks: list[list[list[int]]], space: dict[tuple[int], int]) -> dict[int, set[int]]:
    supporting = defaultdict(set)
    supported = defaultdict(set)

    for idx, brk in enumerate(bricks, start=1):
        supporting[idx] = set()
        for x, y, z in brk:
            # get the subbrk below current subbrk
            brk_below = space[x, y, z - 1]
            if brk_below not in (0, idx):
                supporting[brk_below].add(idx)
                supported[idx].add(brk_below)

    return supporting, supported


def findDisintegratedBricks(bricks: list[list[list[int]]]) -> int:
    space = calcFall(bricks)
    supporting, supported = findSupports(bricks, space)
    ans = 0

    for idx, supported_brks in supporting.items():
        if all(supported[brk] - {idx} for brk in supported_brks):
            ans += 1

    return ans


def main():
    here = Path(__file__).parent
    with open(here / "test.txt") as file:
        test_data = file.read().splitlines()
        test_bricks = parseInput(test_data)

    with open(here / "bricks.txt") as file:
        puzzle_data = file.read().splitlines()
        puzzle_bricks = parseInput(puzzle_data)

    print(f"Test Answer: {findDisintegratedBricks(test_bricks)}")
    print(f"Puzzle Answer: {findDisintegratedBricks(puzzle_bricks)}")


if __name__ == "__main__":
    main()

