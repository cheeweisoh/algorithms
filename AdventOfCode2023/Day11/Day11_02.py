#!/usr/bin/env python3

from pathlib import Path
import numpy as np

def parseInput(file: list) -> list[list[str]]:
    image = []
    
    for line in file:
        image.append(list(line))
    
    return np.array(image)

def calcDistances(image: list[list[str]]) -> int:
    filled_rows, filled_cols = [], []
    galaxies = []
    
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == '#':
                filled_cols.append(j)
                filled_rows.append(i)
                galaxies.append([i, j])
    
    empty_rows = [i for i in range(len(image)) if i not in filled_rows]
    empty_cols = [i for i in range(len(image[0])) if i not in filled_cols]
    
    ans = 0
    scale = 1000000
    
    for i in range(len(galaxies)):
        curr_x, curr_y = galaxies[i][0], galaxies[i][1]
        for j in range(i+1, len(galaxies)):
            dest_x, dest_y = galaxies[j][0], galaxies[j][1]
            empt_x = len([i for i in empty_rows if i > min(curr_x, dest_x) and i < max(curr_x, dest_x)])
            empt_y = len([i for i in empty_cols if i > min(curr_y, dest_y) and i < max(curr_y, dest_y)])
            dist = abs(curr_x - dest_x) + abs(curr_y - dest_y) + ((empt_x + empt_y) * (scale-1))
            ans += dist
    
    return ans

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_image = parseInput(test_data)
        
    with open(here/'image.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_image = parseInput(puzzle_data)
        
    print(f'Test Answer: {calcDistances(test_image)}')
    print(f'Puzzle Answer: {calcDistances(puzzle_image)}')

if __name__ == '__main__':
    main()