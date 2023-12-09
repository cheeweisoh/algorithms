#!/usr/bin/env python3

from pathlib import Path
import re

def checkScore(cards):
    ans = 0
    for winning_nums, our_nums in cards:
        temp_score = 0
        for i in our_nums:
            if i in winning_nums:
                temp_score = temp_score * 2 if temp_score else 1
        ans += temp_score
        
    return ans

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = []
        for line in file:
            card_record = re.search(r':\s*(.*)', line).group(1).strip()
            card_parts = list(card_record.split(' | '))
            test_data.append([[int(i) for i in card_parts[0].split()], [int(i) for i in card_parts[1].split()]])
            
    print(f'Test Answer: {checkScore(test_data)}')
    
    with open(here/'cards.txt') as file:
        puzzle_data = []
        for line in file:
            card_record = re.search(r':\s*(.*)', line).group(1).strip()
            card_parts = list(card_record.split(' | '))
            puzzle_data.append([[int(i) for i in card_parts[0].split()], [int(i) for i in card_parts[1].split()]])
            
    print(f'Puzzle Answer: {checkScore(puzzle_data)}')    

if __name__ == '__main__':
    main()