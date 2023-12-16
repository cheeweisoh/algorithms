#!/usr/bin/env python3

from pathlib import Path

def parseInput(file: list):
    file = file[0].split(',')
    
    return file


def hash(string: str) -> int:
    hash_value = 0
    
    for i in string:
        i_ascii = ord(i)
        
        hash_value += i_ascii
        hash_value *= 17
        hash_value %= 256
    
    return hash_value


def sumInitSequence(init_sequence: list[str]) -> int:
    hash_sum = 0
    
    for i in init_sequence:
        hash_sum += hash(i)
        
    return hash_sum


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_seq = parseInput(test_data)
    
    with open(here/'init_sequence.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_seq = parseInput(puzzle_data)
    
    print(f'Test Answer: {sumInitSequence(test_seq)}')
    print(f'Puzzle Answer: {sumInitSequence(puzzle_seq)}')

if __name__ == '__main__':
    main()