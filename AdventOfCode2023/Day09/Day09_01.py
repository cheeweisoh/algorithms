#!/usr/bin/env python3

from pathlib import Path
from collections import deque

def parseInput(file: list) -> list[int]:
    values = []
    
    for line in file:
        values.append([int(x) for x in line.split(' ')])
    
    return values

def calcExtrapolatedValues(values: list[int]) -> int:
    ans = 0
    
    for val in values:
        hists = deque()
        hists.append(val)
        curr_differences = val
        
        while curr_differences != ([0] * len(curr_differences)):
            new_differences = []
            for i in range(len(curr_differences)-1):
                new_differences.append(curr_differences[i+1] - curr_differences[i])
            hists.append(new_differences)
            curr_differences = new_differences
        
        curr_hist = hists.pop()
        curr_diff = 0
        
        while hists:
            curr_hist = hists.pop()
            curr_diff = curr_hist[-1] + curr_diff
        ans += curr_diff
        
    return ans

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_values = parseInput(test_data)
        
    with open(here/'value_history.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_values = parseInput(puzzle_data)

    print(f'Test Answer: {calcExtrapolatedValues(test_values)}')
    print(f'Puzzle Answer: {calcExtrapolatedValues(puzzle_values)}')

if __name__ == '__main__':
    main()