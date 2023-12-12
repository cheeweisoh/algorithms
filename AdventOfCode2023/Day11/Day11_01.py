#!/usr/bin/env python3

from pathlib import Path
import numpy as np

def parseInput(file: list) -> list[list[str]]:
    image = []
    
    for line in file:
        image.append(list(line))
    
    return np.array(image)

def expansion(image: list[list[str]]) -> list[list[str]]:
    new_image = []
    
    for row in image:
        if '#' in row:
            new_image.append(row)
        else:
            new_image.extend(row for _ in range(2))
    
    new_image = np.array(new_image).transpose()
    new_new_image = []
    
    for col in new_image:
        if '#' in col:
            new_new_image.append(col)
        else:
            new_new_image.extend(col for _ in range(2))
    
    new_new_image = list(np.array(new_new_image).transpose())
    
    return new_new_image

def calcDistances(image: list[list[str]]) -> int:
    expanded_image = expansion(image)
    galaxies = []
    ans = 0
    
    for i in range(len(expanded_image)):
        for j in range(len(expanded_image[0])):
            if expanded_image[i][j] == '#':
                for x, y in galaxies:
                    ans += abs(y-j) + abs(x-i)
                galaxies.append([i, j])
                
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