#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict

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


def placeLens(string: str, boxes: defaultdict(dict)) -> None:
    if '=' in string:
        label, length = string.split('=')
    else:
        label = string[:-1]
    
    box_number = hash(label)
    
    if '=' in string:
        boxes[box_number][label] = length
    elif label in boxes[box_number].keys():
        del boxes[box_number][label]
    
    return


def initLensConfiguration(init_sequence: list[str]):
    boxes = defaultdict(dict)
    focus_power = 0
    
    for i in init_sequence:
        placeLens(i, boxes)
    
    for box_number, box in boxes.items():
        for pos, label in enumerate(box.items()):
            focus_power += (1 + box_number) * (1 + pos) * int(label[1])
    
    return focus_power


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_seq = parseInput(test_data)
    
    with open(here/'init_sequence.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_seq = parseInput(puzzle_data)
    
    print(f'Test Answer: {initLensConfiguration(test_seq)}')
    print(f'Puzzle Answer: {initLensConfiguration(puzzle_seq)}')

if __name__ == '__main__':
    main()