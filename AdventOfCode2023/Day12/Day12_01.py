#!/usr/bin/env python3

from pathlib import Path
import re

def parseInput(file: list):
    springs = []
    hints = []
    
    for line in file:
        spring, hint = line.split(' ')
        springs.append(spring)
        hint = [int(x) for x in hint.split(',')]
        hints.append(hint)
        
    return springs, hints

def checkPossibleCombinations(springs: list[str], hints: list[int]) -> int:
    ans = 0
    
    def f(dots, blocks, i, bi, current):
        key = (i, bi, current)
        if key in DP:
            return DP[key]
        if i==len(dots):
            if bi==len(blocks) and current==0:
                return 1
            elif bi==len(blocks)-1 and blocks[bi]==current:
                return 1
            else:
                return 0
        ans = 0
        for c in ['.', '#']:
            if dots[i]==c or dots[i]=='?':
                if c=='.' and current==0:
                    ans += f(dots, blocks, i+1, bi, 0)
                elif c=='.' and current>0 and bi<len(blocks) and blocks[bi]==current:
                    ans += f(dots, blocks, i+1, bi+1, 0)
                elif c=='#':
                    ans += f(dots, blocks, i+1, bi, current+1)
        DP[key] = ans
        return ans

    for i in range(len(springs)):
        DP = {}
        spring = springs[i]
        hint = hints[i]
        
        ans += f(spring, hint, 0, 0, 0)
    
    return ans
        

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_springs, test_hints = parseInput(test_data)
    
    with open(here/'arrangements.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_springs, puzzle_hints = parseInput(puzzle_data)
    
    print(f'Test Answer: {checkPossibleCombinations(test_springs, test_hints)}')
    print(f'Puzzle Answer: {checkPossibleCombinations(puzzle_springs, puzzle_hints)}')

if __name__ == '__main__':
    main()