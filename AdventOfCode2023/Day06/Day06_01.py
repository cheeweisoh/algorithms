#!/usr/bin/env python3

from pathlib import Path
import re

def parseInput(file: list) -> (list[int], list[int]):
    times = [int(x) for x in re.split(r'\s+', re.search(r':\s*(.*)', file[0]).group(1).strip())]
    distances = [int(x) for x in re.split(r'\s+', re.search(r':\s*(.*)', file[1]).group(1).strip())]
    
    return (times, distances)

def numWaysToBeatRecord(times: list[int], distances: list[int]) -> int:
    ans = 1
    
    for i in range(len(times)):
        curr_ans = 0
        curr_time = times[i]
        curr_record = distances[i]
        
        for j in range(curr_time + 1):
            new_dist = j * (curr_time - j)
            
            if new_dist > curr_record:
                curr_ans = j
                break
        
        ans *= ((curr_time - curr_ans) - curr_ans + 1)
    
    return ans

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_times, test_distances = parseInput(test_data)
    
    with open(here/'time_distance.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_times, puzzle_distances = parseInput(puzzle_data)
    
    print(numWaysToBeatRecord(test_times, test_distances))
    print(numWaysToBeatRecord(puzzle_times, puzzle_distances))

if __name__ == '__main__':
    main()