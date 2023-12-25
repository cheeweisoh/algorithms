#!/usr/bin/env python3

from pathlib import Path

def parseInput(file: list) -> dict[int, list[list[int]]]:
    hailstones = {}
    
    for i, line in enumerate(file):
        pos, vel = line.split(' @ ')
        pos = [int(x) for x in pos.split(', ')]
        vel = [int(x) for x in vel.split(', ')]
        
        hailstones[i] = [pos, vel]
        
    return hailstones


def checkIntersecting(p1: int, p2: int, left: int, right: int, hailstones: dict[int, list[list[int]]]) -> bool:
    x1, y1, _ = hailstones[p1][0]
    x2, y2, _ = hailstones[p2][0]
    vx1, vy1, _ = hailstones[p1][1]
    vx2, vy2, _ = hailstones[p2][1]
    
    if vy2/vx2 == vy1/vx1:
        return False
    
    m1 = vy1 / vx1
    c1 = y1 - (m1 * x1)
    m2 = vy2 / vx2
    c2 = y2 - (m2 * x2)
    
    x = (c2 - c1)/(m1 - m2)
    y = (m1 * x) + c1
    
    if not (left <= x <= right) or not (left <= y <= right):
        return False
    
    t1 = (x - x1) / vx1
    t2 = (x - x2) / vx2
    
    if t1 < 0 or t2 < 0:
        return False
    
    return True


def countIntersections(hailstones: dict[int, list[list[int]]], left: int, right: int) -> int:
    hs = list(hailstones.keys())
    ans = 0
    
    for i in range(len(hs)):
        for j in range(i+1, len(hs)):
            if checkIntersecting(i, j, left, right, hailstones):
                ans += 1
                    
    return ans


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_hailstones = parseInput(test_data)
    
    with open(here/'hailstones.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_hailstones = parseInput(puzzle_data)
    
    print(f'Test Answer: {countIntersections(test_hailstones, 7, 27)}')
    print(f'Puzzle Answer: {countIntersections(puzzle_hailstones, 200000000000000, 400000000000000)}')


if __name__ == '__main__':
    main()