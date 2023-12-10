#!/usr/bin/env python3

from pathlib import Path
from tqdm import tqdm
import re

def parseInput(file: list) -> (list, dict):
    seeds = [int(x) for x in re.search(r':\s*(.*)', file[0]).group(1).strip().split(' ')]
    maps = []
        
    for line in file[2:]:
        if 'map' in line:
            maps.append(dict())
        elif line != '':
            destination, source, length = [int(value) for value in line.split()]
            maps[-1][range(source, source+length)] = range(destination, destination+length)
    
    return (seeds, maps)
    

def reverse_lookup_seed(location: int, maps: list[dict]) -> int:
    value = location
    for current_map in reversed(maps):
        value = next(
            (source_range.start + (value - destination_range.start)
             for source_range, destination_range in current_map.items()
             if value in destination_range),
            value
        )
    return value

def findLowestLocation(seeds: list, maps: dict) -> int:
    seed_ranges = []
    
    for i in range(0, len(seeds)-1, 2):
        start, length = seeds[i:i+2]
        seed_ranges.append(range(start, start+length))
    
    min_loc = 0
    while True:
        potental_seed = reverse_lookup_seed(min_loc, maps)
        if any(potental_seed in seed_range for seed_range in seed_ranges):
            print(min_loc)
            break
        min_loc += 1

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = [line.rstrip('\n') for line in file]
        test_seeds, test_maps = parseInput(test_data)
    
    with open(here/'seeds_maps.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_seeds, puzzle_maps = parseInput(puzzle_data)
    
    print(f'Test Answer: {findLowestLocation(test_seeds, test_maps)}')
    print(f'Puzzle Answer: {findLowestLocation(puzzle_seeds, puzzle_maps)}')

if __name__ == '__main__':
    main()