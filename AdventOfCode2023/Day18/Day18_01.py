#!/usr/bin/env python3

from pathlib import Path

def parseInput(file: list):
    plan = []
    
    for line in file:
        dir, dist, color = line.split(' ')
        plan.append([dir, int(dist), color.lstrip('(').rstrip(')')])
    
    return plan


def calcCapacity(plan: list[list[str]]):
    dirs = {'U': -1, 'D': 1, 'R': 1j, 'L': -1j}
    curr_point = 0
    area = 0
    perimeter = 0
    
    for dir, dist, _ in plan:
        new_point = curr_point + dirs[dir] * dist
        area = area + (curr_point.real * new_point.imag) - (curr_point.imag * new_point.real)
        perimeter += dist
        curr_point = new_point
    
    area = int(abs(area) + perimeter) // 2 + 1
    
    return area


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_plan = parseInput(test_data)
    
    with open(here/'digplan.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_plan = parseInput(puzzle_data)
    
    print(f'Test Answer: {calcCapacity(test_plan)}')
    print(f'Puzzle Answer: {calcCapacity(puzzle_plan)}')

if __name__ == '__main__':
    main()