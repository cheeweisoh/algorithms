#!/usr/bin/env python3

from pathlib import Path
import numpy as np
import warnings

warnings.filterwarnings('ignore')

def parseInput(file: list):
    platform = np.array([[x for x in line] for line in file])
        
    return platform


def tilt_platform(arr: np.array(str), order: int):
    edg = np.where(np.diff(np.hstack(([False], (arr == '.') | (arr == 'O'), [False]))))[0]
    for i in range(0, len(edg), 2):
        arr[edg[i] : edg[i + 1]] = np.sort(arr[edg[i] : edg[i + 1]])[::order]


def cycle(platform: np.array(np.array(str))):
    rows, cols = platform.shape
    
    for col in range(cols):
        tilt_platform(platform[:, col], -1)
    
    for row in range(rows):
        tilt_platform(platform[row, :], -1)
    
    for col in range(cols):
        tilt_platform(platform[:, col], 1)
    
    for row in range(rows):
        tilt_platform(platform[row, :], 1)
    
    return platform


def cycleDetection(platform: np.array(np.array(str))):
    hist = []
    hist.append(platform.copy())
    
    for i in range(1_000_000_000):
        cycle(platform)
        period = (0, 0, 0)
        
        for j, histplat in enumerate(hist, start=1):
            if np.all(platform == histplat):
                period = (i-j+1, j, i)
                break
        if period[0] > 0:
            break
        hist.append(platform.copy())
    
    return period


def calcFinalLoad(platform: np.array(np.array(str))):
    total_load = 0
    period = cycleDetection(platform)
    remain = (1_000_000_000 - period[2]) % period[0]
    
    for i in range(period[2]+remain-2):
        cycle(platform)
        
    for i in range(len(platform)):
        num_rocks = np.sum(platform[i] == 'O')
        total_load += num_rocks * (len(platform) - i)
    
    return total_load


def temp(mat):
    total_load = 0
    res = []
    res.append(mat.copy())
    period = (0, 0, 0)
    for i in range(1, 10000000):
        cycle(mat)
        # printmat(mat, str(i))
        period = (0, 0, 0)
        for n, origmat in enumerate(res, start=1):
            if np.all(mat == origmat):
                period = (i - n + 1, n, i)
                res.append(mat.copy())
                print(res)
                break
        if period[0] > 0:
            break
        res.append(mat.copy())
    print(period)

    residuum = (1_000_000_000 - period[2]) % period[0]
    print(f"{residuum=}")
    for i in range(residuum):
        cycle(mat)
    
    for i in range(len(mat)):
        num_rocks = np.sum(mat[i] == 'O')
        # print(num_rocks, (len(platform) - i))
        total_load += num_rocks * (len(mat) - i)
    
    return total_load


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_platform = parseInput(test_data)
    
    with open(here/'platform.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_platform = parseInput(puzzle_data)
    
    print(f'Test Answer: {calcFinalLoad(test_platform)}')
    print(f'Puzzle Answer: {calcFinalLoad(puzzle_platform)}')

if __name__ == '__main__':
    main()
    
# I have no idea why there is a need to subtract 2 in the puzzle solution.