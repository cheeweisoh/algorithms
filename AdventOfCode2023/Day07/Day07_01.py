#!/usr/bin/env python3

from pathlib import Path
from collections import Counter, defaultdict

def parseInput(file: list) -> dict:
    test_data = {}
    rank_map = {'2': 'A', '3': 'B', '4': 'C', '5': 'D', '6': 'E', '7': 'F', '8': 'G', '9': 'H', 'T': 'I', 'Q': 'K', 'K': 'L', 'A': 'M'}
    
    for line in file:
        hand, bid = line.split(' ')
        remap_hand = ''.join(rank_map.get(i, i) for i in hand)
        test_data[remap_hand] = bid
    
    return test_data

def calcTotalWinnings(bids: dict) -> int:
    hands = list(bids.keys())
    hand_scores = defaultdict(list)
    
    for hand in hands:
        card_count = sorted(Counter(hand).values())
        if card_count == [5]:
            hand_scores[7].append(hand)
        elif card_count == [1, 4]:
            hand_scores[6].append(hand)
        elif card_count == [2, 3]:
            hand_scores[5].append(hand)
        elif card_count == [1, 1, 3]:
            hand_scores[4].append(hand)
        elif card_count == [1, 2, 2]:
            hand_scores[3].append(hand)
        elif card_count == [1, 1, 1, 2]:
            hand_scores[2].append(hand)
        else:
            hand_scores[1].append(hand)
    
    curr_pos = len(hands)
    total_score = 0
    for score in sorted(hand_scores.keys(), reverse=True):
        curr_hands = sorted(hand_scores[score], reverse=True)
        
        for hand in curr_hands:
            total_score += curr_pos * int(bids[hand])
            curr_pos -= 1
            
    return total_score

def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = parseInput(file.read().splitlines())
    
    with open(here/'bids.txt') as file:
        puzzle_data = parseInput(file.read().splitlines())
    
    print(f'Test Answer: {calcTotalWinnings(test_data)}')
    print(f'Puzzle Answer: {calcTotalWinnings(puzzle_data)}')

if __name__ == '__main__':
    main()