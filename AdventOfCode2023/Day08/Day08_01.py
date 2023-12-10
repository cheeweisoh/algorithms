#!/usr/bin/env python3

from pathlib import Path

def parseInput(file: list) -> (str, dict):
    dirs = file[0]
    maps = {}
    
    for line in file[2:]:
        node, adj_nodes = line.split(' = ')
        adj_nodes = adj_nodes[1:-1].split(', ')
        maps[node] = adj_nodes
    
    return (dirs, maps)

def calcSteps(dirs: str, maps: dict) -> int:
    curr_node = 'AAA'
    steps = 0
    
    while curr_node != 'ZZZ':
        steps += 1
        next_step = dirs[(steps % len(dirs)) - 1]
        
        if next_step == 'L':
            curr_node = maps[curr_node][0]
        else:
            curr_node = maps[curr_node][1]

    return steps

def main():
    here = Path(__file__).parent
    with open(here/'test01.txt') as file:
        test_data = file.read().splitlines()
        test_dirs, test_maps = parseInput(test_data)
    
    with open(here/'map.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_dirs, puzzle_maps = parseInput(puzzle_data)
    
    print(f'Test Answer: {calcSteps(test_dirs, test_maps)}')
    print(f'Puzzle Answer: {calcSteps(puzzle_dirs, puzzle_maps)}')

if __name__ == '__main__':
    main()