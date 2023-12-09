#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict

def countEngineParts(engine_schema):
    ans = 0
    curr_num = ''
    incl_indicator = ()
    gear_mem = defaultdict(list)
    
    for i in range(len(engine_schema)):
        for j in range(len(engine_schema[0])):
            curr_char = engine_schema[i][j]
            
            if curr_char.isdigit():
                curr_num += curr_char
                
                offsets = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)) 
                
                for di, dj in offsets:
                    ni, nj = i+di, j+dj
                    if (ni >= 0) & (ni < len(engine_schema)) & (nj >= 0) & (nj < len(engine_schema[0])):
                        new_char = engine_schema[ni][nj]
                        
                        if new_char == '*':
                            incl_indicator = (ni, nj)
            else:
                if incl_indicator and curr_num:
                    gear_mem[incl_indicator].append(curr_num)
                    incl_indicator = ()
                curr_num = ''
        if incl_indicator and curr_num:
            gear_mem[incl_indicator].append(curr_num)
        curr_num = ''
        incl_indicator = ()
    
    for gears in gear_mem.values():
        if len(gears) == 2:
            ans += (int(gears[0]) * int(gears[1]))
    return ans

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = [list(line.strip()) for line in file]
        
    print(f'Test Answer: {countEngineParts(test_data)}')
    
    with open(here/'engine_schema.txt') as file:
        puzzle_data = [list(line.strip()) for line in file]
    
    print(f'Puzzle Answer: {countEngineParts(puzzle_data)}')

if __name__ == '__main__':
    main()