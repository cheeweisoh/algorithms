#!/usr/bin/env python3

from pathlib import Path
import re

def parseInput(file: list) -> (list, dict):
    seeds = [int(x) for x in re.search(r':\s*(.*)', file[0]).group(1).strip().split(' ')]
    maps = {}
        
    for line in file[1:]:
        if line == '':
            continue
        elif ':' in line:
            titles = line.split(' ')[0].split('-')
            source = titles[0]
            destination = titles[-1]
            maps[source] = {destination: []}
        else:
            values = [int(x) for x in line.split(' ')]
            maps[source][destination].append(values)
    
    return (seeds, maps)
    

def findNextMap(curr_map: dict, num: int) -> (str, int):
    next_key = next(iter(curr_map.keys()), None)
    ans = -1
    
    for dr, sr, rl in sorted(curr_map[next_key], key=lambda x: x[1]):
        if num < sr:
            break
        if num > sr + rl:
            continue
        ans = dr + (num-sr)
    
    ans = ans if ans != -1 else num
    return (next_key, ans)

def findLowestLocation(seeds: list, maps: dict) -> int:
    lowest_location = float('inf')
    
    for i in seeds:
        curr_key = 'seed'
        num = i
        while curr_key != 'location':
            curr_key, num = findNextMap(maps[curr_key], num)
        lowest_location = min(lowest_location, num)
    
    return lowest_location

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = [line.rstrip('\n') for line in file]
        test_seeds, test_maps = parseInput(test_data)
    
    with open(here/'seeds_maps.txt') as file:
        puzzle_data = [line.rstrip('\n') for line in file]
        puzzle_seeds, puzzle_maps = parseInput(puzzle_data)
    
    print(f'Test Answer: {findLowestLocation(test_seeds, test_maps)}')
    print(f'Puzzle Answer: {findLowestLocation(puzzle_seeds, puzzle_maps)}')
    
    
    
if __name__ == '__main__':
    main()