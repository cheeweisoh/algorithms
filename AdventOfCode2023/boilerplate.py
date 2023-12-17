#!/usr/bin/env python3

from pathlib import Path

def parseInput(file: list):
    pass

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test = parseInput(test_data)
    
    with open(here/'puzzle.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle = parseInput(puzzle_data)
    
    print(test_data)
    
    # print(f'Test Answer: {}')
    # print(f'Puzzle Answer: {}')

if __name__ == '__main__':
    main()