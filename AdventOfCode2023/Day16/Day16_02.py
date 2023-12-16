#!/usr/bin/env python3

from pathlib import Path

def parseInput(file: list):
    lens_table = []
    
    for line in file:
        lens_table.append([x for x in line])
    
    return lens_table


def countEnergised(lens_table: list[list[str]], start: tuple[complex]) -> int:
    board = {i + 1j * j: x for i, l in enumerate(lens_table) for j, x in enumerate(l)}
    queue = [start]
    seen = set()
    
    while queue:
        pos, dir = queue.pop()
        
        if (pos, dir) in seen:
            continue
        seen.add((pos, dir))
        
        new_pos = pos + dir
        if new_pos not in board.keys():
            continue
        
        match board[new_pos]:
            case '|' if dir.imag:
                new = [1, -1]
            case '-' if dir.real:
                new = [1j, -1j]
            case '\\':
                new = [(dir * -1j).conjugate()]
            case '/':
                new = [(dir * 1j).conjugate()]
            case _:
                new = [dir]
        
        for new_dir in new:
            queue.append([new_pos, new_dir])
    
    return len(set([x[0] for x in seen])) - 1


def findMostEnergised(lens_table: list[list[str]]) -> int:
    count = 0
    
    for i in range(len(lens_table)):
        count = max(count, countEnergised(lens_table, (i - 1j, 1j)))
        count = max(count, countEnergised(lens_table, (i + len(lens_table[0]) * 1j, -1j)))
    
    for k in range(len(lens_table[0])):
        count = max(count, countEnergised(lens_table, (-1 + k * 1j, 1)))
        count = max(count, countEnergised(lens_table, (len(lens_table) + k * 1j, -1)))
    
    return count
    
    


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_table = parseInput(test_data)
    
    with open(here/'board.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_table = parseInput(puzzle_data)
    
    print(f'Test Answer: {findMostEnergised(test_table)}')
    print(f'Puzzle Answer: {findMostEnergised(puzzle_table)}')
    
if __name__ == '__main__':
    main()