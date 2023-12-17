#!/usr/bin/env python3

from pathlib import Path
import heapq

def parseInput(file: list):
    heat_map = []
    
    for line in file:
        heat_map.append([int(x) for x in line])
        
    return heat_map


def calculate_heat(heat_map: list[list[int]]) -> int:
    seen = set()
    costs = {}
    pqueue = [(0, (0, 0), (0, 0))]
    
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while pqueue:
        curr_loss, curr_pos, prev_move = heapq.heappop(pqueue)
        
        if curr_pos == (len(heat_map)-1, len(heat_map[0])-1):
            return curr_loss
        
        if (curr_pos, prev_move) in seen:
            continue
        seen.add((curr_pos, prev_move))
        
        for next_move in dirs:
            curr_change = 0
            
            if next_move == prev_move or next_move == tuple(-x for x in prev_move):
                continue
            
            for dist in range(1, 11):
                nx = curr_pos[0] + next_move[0] * dist
                ny = curr_pos[1] + next_move[1] * dist
                
                if nx < 0 or nx >= len(heat_map) or ny < 0 or ny >= len(heat_map[0]):
                    continue
                else:
                    curr_change += heat_map[nx][ny]
                    
                    if dist < 4:
                        continue
                    
                    new_loss = curr_loss + curr_change
                    
                    if costs.get(((nx, ny), next_move), float('inf')) <= new_loss:
                        continue
                    costs[((nx, ny), next_move)] = new_loss
                    heapq.heappush(pqueue, (new_loss, (nx, ny), next_move))


def main():
    here = Path(__file__).parent
    with open(here/'test01.txt') as file:
        test_data = file.read().splitlines()
        test_map = parseInput(test_data)
    print(f'Test 1 Answer: {calculate_heat(test_map)}')
    
    with open(here/'test02.txt') as file:
        test_data = file.read().splitlines()
        test_map = parseInput(test_data)
    print(f'Test 2 Answer: {calculate_heat(test_map)}')
    
    with open(here/'map.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_map = parseInput(puzzle_data)
    print(f'Puzzle Answer: {calculate_heat(puzzle_map)}')
    

if __name__ == '__main__':
    main()


'''
111111111111
999999999991
999999999991
999999999991
999999999991
'''