#!/usr/bin/env python3

from pathlib import Path
from math import lcm

def parseInput(file: list) -> (str, dict):
    dirs = file[0]
    maps = {}
    
    for line in file[2:]:
        node, adj_nodes = line.split(' = ')
        adj_nodes = adj_nodes[1:-1].split(', ')
        maps[node] = adj_nodes
    
    return (dirs, maps)

def calcSteps(dirs: str, maps: dict) -> int:
    curr_nodes = [node for node in maps.keys() if node[-1] == 'A']
    first_encounters = []
    
    for node in curr_nodes:
        curr_node = node
        steps = 0
        while curr_node[-1] != 'Z':
            steps += 1
            next_step = dirs[(steps % len(dirs)) - 1]
            
            if next_step == 'L':
                curr_node = maps[curr_node][0]
            else:
                curr_node = maps[curr_node][1]
        
        first_encounters.append(steps)

    return lcm(*first_encounters)

def main():
    here = Path(__file__).parent
    with open(here/'test02.txt') as file:
        test_data = file.read().splitlines()
        test_dirs, test_maps = parseInput(test_data)
    
    with open(here/'map.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_dirs, puzzle_maps = parseInput(puzzle_data)
    
    print(f'Test Answer: {calcSteps(test_dirs, test_maps)}')
    print(f'Puzzle Answer: {calcSteps(puzzle_dirs, puzzle_maps)}')

if __name__ == '__main__':
    main()