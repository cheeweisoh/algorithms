#!/usr/bin/env python3

from pathlib import Path
from queue import deque
import numpy as np

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
    size = (len(farm), len(farm[0]))
    start = findStart(farm)
    
    x_f, rem = divmod(total_steps, size[0])
    borders = [rem, rem + size[1], rem + 2*size[1]]
    
    visited = set()
    queue = deque([start])
    total = [0, 0]
    Y = []
    
    for step in range(1, borders[-1] + 1):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx, ny = x + dx, y + dy
                
                if (nx, ny) in visited or farm[nx % size[0]][ny % size[1]] == '#':
                    continue
                
                visited.add((nx, ny))
                queue.append((nx, ny))
                total[step % 2] += 1
                
        if step in borders:
            Y.append(total[step % 2])
            
    X = [0, 1, 2]
    coeffs = np.polyfit(X, Y, deg=2)
    y_f = np.polyval(coeffs, x_f)
    return int(y_f.round())


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_farm = parseInput(test_data)
    
    with open(here/'farm.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_farm = parseInput(puzzle_data)
    
    for i in (6, 10, 50, 100, 500, 1000, 5000):
        print(f'Test Answer for {i} steps: {countPlots(test_farm, i)}')
    print(f'Puzzle Answer: {countPlots(puzzle_farm, 26_501_365)}')

if __name__ == '__main__':
    main()