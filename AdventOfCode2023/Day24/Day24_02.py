#!/usr/bin/env python3

from pathlib import Path
import numpy as np

def parseInput(file: list) -> dict[int, list[list[int]]]:
    hailstones = []
    
    for i, line in enumerate(file):
        pos, vel = line.split(' @ ')
        pos = [int(x) for x in pos.split(', ')]
        vel = [int(x) for x in vel.split(', ')]
        
        hailstones.append(pos+vel)
        
    return hailstones

def calcs(x1: int, y1: int, z1: int, vx1: int, vy1: int, vz1: int, x2: int, y2: int, z2: int, vx2: int, vy2: int, vz2: int) -> (list[list[int]], list[int]):
    sub_A = []
    sub_b = []
    
    sub_A.append([vy2 - vy1, vx1 - vx2, 0.0, y1 - y2, x2 - x1, 0.0])
    sub_A.append([vz2 - vz1, 0.0, vx1 - vx2, z1 - z2, 0.0, x2 - x1])
    sub_A.append([0.0, vz2 - vz1, vy1 - vy2, 0.0, z1 - z2, y2 - y1])
    
    sub_b.append((y1 * vx1 - y2 * vx2) - (x1 * vy1 - x2 * vy2))
    sub_b.append((z1 * vx1 - z2 * vx2) - (x1 * vz1 - x2 * vz2))
    sub_b.append((z1 * vy1 - z2 * vy2) - (y1 * vz1 - y2 * vz2))
    
    return sub_A, sub_b


def findRockPosition(hailstones: list[list[int]]) -> int:
    A = []
    b = []
    
    for i in range(1,3):
        x1, y1, z1, vx1, vy1, vz1 = hailstones[0]
        x2, y2, z2, vx2, vy2, vz2 = hailstones[i]
        
        sub_A, sub_b = calcs(x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2)
        A.extend(sub_A)
        b.extend(sub_b)
    
    A = np.array(A)
    b = np.array(b)
    
    ans = np.linalg.solve(A, b)
    
    return round(ans[0] + ans[1] + ans[2])


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_hailstones = parseInput(test_data)
    
    with open(here/'hailstones.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_hailstones = parseInput(puzzle_data)
    
    print(f'Test Answer: {findRockPosition(test_hailstones)}')
    print(f'Puzzle Answer: {findRockPosition(puzzle_hailstones)}')


if __name__ == '__main__':
    main()