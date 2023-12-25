#!/usr/bin/env python3

from pathlib import Path
import heapq

def parseInput(file: list) -> list[list[str]]:
    farm = []
    
    for line in file:
        farm.append(list(line))
        
    return farm


def findStart(farm: list[list[str]]) -> tuple[int]:
    for i in range(len(farm)):
        for j in range(len(farm[0])):
            if farm[i][j] == 'S':
                return (i, j)


def countPlots(farm: list[list[str]], total_steps: int) -> int:
    start = findStart(farm)
    visited = set()
    queue = [(0, start)]
    ans = [start,] if total_steps % 2 == 0 else []
    
    while queue:
        steps, curr_pos = heapq.heappop(queue)
        
        if curr_pos in visited:
            continue
        visited.add(curr_pos)
        
        if steps in range(1, total_steps + 1):
            if (total_steps % steps == 0 and steps % 2 == 0):
                ans.append((curr_pos, steps))
            elif (total_steps - steps) % 2 == 0:
                ans.append((curr_pos, steps))
                
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            new_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
            if new_pos[0] in range(len(farm)) and new_pos[1] in range(len(farm[0])) and farm[new_pos[0]][new_pos[1]] != '#':
                heapq.heappush(queue, (steps+1, new_pos))
    
    return len(ans)


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_farm = parseInput(test_data)
    
    with open(here/'farm.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_farm = parseInput(puzzle_data)
    
    print(f'Test Answer: {countPlots(test_farm, 6)}')
    print(f'Puzzle Answer: {countPlots(puzzle_farm, 64)}')

if __name__ == '__main__':
    main()