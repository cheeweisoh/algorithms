#!/usr/bin/env python3

from pathlib import Path

def parseInput(file: list):
    platform = []
    
    for line in file:
        platform.append(list(line))
        
    return platform

def calcIndvLoad(platform: list[list[str]], rock: tuple[int]):
    x, y = rock
    platform[x][y] = '.'
    
    while True:
        if x - 1 < 0 or platform[x-1][y] in ['O', '#']:
            platform[x][y] = 'O'
            break
        else:
            x = x - 1
            
    load = len(platform) - x
    return load

def calcLoad(platform: list[list[str]]):
    total_load = 0
    
    for i in range(len(platform)):
        for j in range(len(platform[0])):
            if platform[i][j] == 'O':
                total_load += calcIndvLoad(platform, (i, j))
                
    return total_load

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_platform = parseInput(test_data)
    
    with open(here/'platform.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_platform = parseInput(puzzle_data)
    
    print(f'Test Answer: {calcLoad(test_platform)}')
    print(f'Puzzle Answer: {calcLoad(puzzle_platform)}')

if __name__ == '__main__':
    main()