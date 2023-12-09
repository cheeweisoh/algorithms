#!/usr/bin/env python3

from pathlib import Path
import re

def checkScore(cards):
    card_mem = [1] * len(cards)
    
    for i in range(len(card_mem)):
        winning_nums, our_nums = cards[i]
        score = len(set(winning_nums).intersection(our_nums))
        
        for j in range(score):
            card_mem[i+1+j] += card_mem[i]

    return sum(card_mem)

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