#!/usr/bin/env python3

from pathlib import Path
import numpy as np

def parseInput(file: list):
    all_patterns = []
    curr_pattern = []
    
    for line in file:
        if line == '':
            all_patterns.append(curr_pattern)
            curr_pattern = []
        else:
            curr_pattern.append(list(line))
    
    all_patterns.append(curr_pattern)
            
    return all_patterns

def findReflections(pattern: list[str]) -> int:
    for i in range(1, len(pattern)):
        check = 0
        for j in range(min(i, len(pattern)-i)):
            if pattern[i+j] != pattern[i-j-1]:
                break
            else:
                check += 1
        if check == min(i, len(pattern)-i):
            return i
        
    return 0

def calcReflectionTotal(patterns: list[list[str]]) -> int:
    ans = 0
    
    for pattern in patterns:
        horiz_check = findReflections(pattern)
        
        rotate_pattern = [list(i) for i in list(np.array(pattern).transpose())]
        vert_check = findReflections(rotate_pattern)
        
        ans += horiz_check * 100 + vert_check
    
    return ans

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_patterns = parseInput(test_data)
    
    with open(here/'valley.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_patterns = parseInput(puzzle_data)
    
    print(f'Test Answer: {calcReflectionTotal(test_patterns)}')
    print(f'Puzzle Answer: {calcReflectionTotal(puzzle_patterns)}')

if __name__ == '__main__':
    main()