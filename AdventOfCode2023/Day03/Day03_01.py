#!/usr/bin/env python3

from pathlib import Path

def countEngineParts(engine_schema):
    ans = 0
    curr_num = ''
    incl_indicator = False
    
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
                        
                        if (not new_char.isdigit()) & (new_char != '.'):
                            incl_indicator = True
            else:
                if incl_indicator and curr_num:
                    ans += int(curr_num.strip())
                    incl_indicator = False
                curr_num = ''
        if incl_indicator and curr_num:
            ans += int(curr_num.strip())
        curr_num = ''
        incl_indicator = False
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