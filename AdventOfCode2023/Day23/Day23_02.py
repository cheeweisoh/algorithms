#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict


def parseInput(file: list) -> list[list[str]]:
    new_map = []

    for line in file:
        new_line = list(line)
        new_map.append(new_line)

    return new_map


def getIntersection(pos: tuple[int], dir: int, new_map: list[list[str]]):
    next_dirs = []
    
    for ddir in [1, -1, 1j, -1j]:
        if ddir == -dir:
            continue
        
        new_pos = pos + ddir
        x, y = int(new_pos.real), int(new_pos.imag)
        if x in range(len(new_map)) and y in range(len(new_map[0])) and new_map[x][y] != '#':
            next_dirs.append(ddir)
            
    return next_dirs


def getAdjacencyMap(new_map: list[list[str]]) -> (dict[int, list[tuple[int]]], int, int):
    start = new_map[0].index(".") * 1j
    end = (len(new_map) - 1) + (new_map[-1].index(".")) * 1j

    visited = set()
    nodes = defaultdict(list)
    queue = [(start, 1)]
    
    while queue:
        node, dir = queue.pop()
        
        if (node, dir) in visited:
            continue
        visited.add((node, dir))
        
        curr_pos = node
        steps = 0
        count = 0
        while True:
            count += 1
            steps += 1
            curr_pos += dir
            next_dirs = getIntersection(curr_pos, dir, new_map)
            
            if len(next_dirs) > 1 or curr_pos == end:
                nodes[node].append((curr_pos, steps))
                nodes[curr_pos].append((node, steps))
                visited.add((curr_pos, -dir))
                
                for ddir in next_dirs:
                    if (curr_pos, ddir) not in visited:
                        queue.append((curr_pos, ddir))
                break
            dir = next_dirs[0]
                
    return nodes, start, end


def findLongestPath(new_map: list[list[str]]) -> int:
    adj_map, start, end = getAdjacencyMap(new_map)
    mem = {}
    visited = set()
    visited.add(start)
    queue = [(start, 0, frozenset(visited))]
    ans = 0
    
    while queue:
        curr_pos, steps, visited = queue.pop()
        
        if curr_pos == end and steps > ans:
            ans = steps
            print(ans)
            continue
        
        if mem.get((curr_pos, visited), -1) >= steps:
            continue
        
        mem[(curr_pos, visited)] = steps
        new_visited = set(visited)
        new_visited.add(curr_pos)
        new_visited = frozenset(new_visited)
        
        for next_pos, next_steps in adj_map[curr_pos]:
            if next_pos in new_visited:
                continue
            new_steps = steps + next_steps
            if mem.get((next_pos, new_visited), 0) >= new_steps:
                continue
            queue.append((next_pos, new_steps, new_visited))
    
    return ans
        

def main():
    here = Path(__file__).parent
    with open(here / "test.txt") as file:
        test_data = file.read().splitlines()
        test_map = parseInput(test_data)

    with open(here / "map.txt") as file:
        puzzle_data = file.read().splitlines()
        puzzle_map = parseInput(puzzle_data)

    print(f"Test Answer: {findLongestPath(test_map)}")
    print(f"Puzzle Answer: {findLongestPath(puzzle_map)}")


if __name__ == "__main__":
    main()
