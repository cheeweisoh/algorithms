#!/usr/bin/env python3

from pathlib import Path
import re

def parseInput(file: list):
    pass

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
    
    print(test_data)

if __name__ == '__main__':
    main()