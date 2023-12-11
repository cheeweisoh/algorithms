#!/usr/bin/env python3

from pathlib import Path
import re

def parseInput(file: list) -> list[list[str]]:
    maze = []
    
    for line in file:
        maze.append(list(line))
        
    return maze

def findStart(maze: list[list[str]]) -> (int, int):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                return (i, j)

def nextTile(maze: list[list[str]], curr_pos: (int, int), direction: str) -> (int, int, str):
    x, y = curr_pos
    curr_pipe = maze[x][y]
    dir_map = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE'}
    
    if curr_pipe in dir_map.keys():
        change = dir_map[curr_pipe]
        if direction == change[0]:
            new_direction = change[1]
        elif direction == change[1]:
            new_direction = change[0]
        else:
            return
        
        if new_direction == 'N':
            new_pos = (x-1, y)
            next_direction = 'S'
        elif new_direction == 'S':
            new_pos = (x+1, y)
            next_direction = 'N'
        elif new_direction == 'E':
            new_pos = (x, y+1)
            next_direction = 'W'
        else:
            new_pos = (x, y-1)
            next_direction = 'E'
        
        return (new_pos, next_direction)
        
    else:
        return

def mapDistances(maze: list[list[str]]) -> int:
    x, y = findStart(maze)
    # print(f'start: {x},{y}')
    distances = [[0] * len(maze[0]) for _ in range(len(maze))]
    
    
    def helper(x, y, dir, steps):
        # print(x, y, dir, steps)
        if maze[x][y] == '.':
            return
        if x < 0 or x > len(maze):
            return
        if y < 0 or y > len(maze[0]):
            return
        
        steps += 1
        if distances[x][y] != 0 and distances[x][y] < steps:
            print(distances[x][y], steps)
            return
        
        distances[x][y] = min(distances[x][y], steps) if distances[x][y] != 0 else steps
        # print(distances)
        
        # print((x,y), dir)
        next_pos = nextTile(maze, (x, y), dir)
        # print(next_pos)
        if next_pos:
            next_coord, next_direction = next_pos
            
            if maze[next_coord[0]][next_coord[1]] == 'S':
                # print('back to start')
                return
            else:
                helper(next_coord[0], next_coord[1], next_direction, steps)
            
        else:
            # print('deadend')
            return
    
    helper(x-1, y, 'S', 0)
    helper(x+1, y, 'N', 0)
    helper(x, y-1, 'E', 0)
    helper(x, y+1, 'W', 0)
    
    return max(max(row) for row in distances)

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_maze = parseInput(test_data)
    
    with open(here/'maze.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_maze = parseInput(puzzle_data)
    
    # print(f'Test Answer: {mapDistances(test_maze)}')
    # print(nextTile(puzzle_maze, (84,129), 'E'))
    print(f'Puzzle Answer: {mapDistances(puzzle_maze)}')

if __name__ == '__main__':
    main()