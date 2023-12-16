#!/usr/bin/env python3

from pathlib import Path

def parseInput(file: list):
    lens_table = []
    
    for line in file:
        lens_table.append([x for x in line])
    
    return lens_table


def countEnergised(lens_table: list[list[str]]) -> int:
    board = {i + 1j * j: x for i, l in enumerate(lens_table) for j, x in enumerate(l)}
    queue = [(0 - 1j, 1j)]
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


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_table = parseInput(test_data)
    
    with open(here/'board.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_table = parseInput(puzzle_data)
    
    print(f'Test Answer: {countEnergised(test_table)}')
    print(f'Puzzle Answer: {countEnergised(puzzle_table)}')
    
if __name__ == '__main__':
    main()


'''
\
 0 + 1j ->  1 + 0j
-1 + 0j ->  0 - 1j
 0 - 1j -> -1 + 0j
 1 + 0j ->  0 + 1j

/
 0 + 1j -> -1 + 0j
-1 + 0j ->  0 + 1j
 0 - 1j ->  1 + 0j
 1 + 0j ->  0 - 1j

'''