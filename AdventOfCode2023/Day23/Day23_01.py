#!/usr/bin/env python3

from pathlib import Path
from queue import deque


def parseInput(file: list) -> list[list[str]]:
    new_map = []

    for line in file:
        new_line = list(line)
        new_map.append(new_line)

    return new_map


def findLongestPath(new_map: list[list[str]]) -> int:
    sx, sy = 0, new_map[0].index(".")
    ex, ey = len(new_map) - 1, new_map[-1].index(".")
    ans = []

    queue = deque()
    queue.append((sx, sy, [(sx, sy)]))

    slopes = {">": [0, 1], "v": [1, 0]}

    while queue:
        # print(queue)
        x, y, pathset = queue.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy

            if (nx, ny) in pathset:
                continue

            if nx == ex and ny == ey:
                ans.append(len(pathset))

            if nx in range(len(new_map)) and ny in range(len(new_map[0])):
                ntile = new_map[nx][ny]
                new_pathset = [x for x in pathset]

                if ntile != "#":
                    if (ntile == ">" and (dx, dy) == (0, -1)) or (ntile == "v" and (dx, dy) == (-1, 0)):
                        continue

                    new_pathset.append((nx, ny))
                    if ntile in slopes.keys():
                        nx, ny = nx + slopes[ntile][0], ny + slopes[ntile][1]
                        new_pathset.append((nx, ny))

                    queue.append((nx, ny, new_pathset))

    return max(ans)


def main():
    here = Path(__file__).parent
    with open(here / "test.txt") as file:
        test_data = file.read().splitlines()
        test_map = parseInput(test_data)

    with open(here / "map.txt") as file:
        puzzle_data = file.read().splitlines()
        puzzle_map = parseInput(puzzle_data)

    print(f"Test Answer: {findLongestPath(test_map)}")
    print(f"Puzzle Answer: {findLongestPath(puzzle_map)}")


if __name__ == "__main__":
    main()
