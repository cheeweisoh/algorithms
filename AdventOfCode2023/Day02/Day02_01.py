#!/usr/bin/env python3

from pathlib import Path
import re

def checkPossibleGames(game_records):
    ans = 0
    
    for i in range(len(game_records)):
        max_nums = {'red': 0, 'green': 0, 'blue': 0}
        
        for draw in game_records[i]:
            for color, quantity in draw.items():
                max_nums[color] = max(max_nums[color], quantity)
                
        if max_nums['red'] <= 12 and max_nums['green'] <= 13 and max_nums['blue'] <= 14:
            ans += i+1
                    
    return ans

def main():
    here = Path(__file__).parent
    with open(here/'test01.txt') as file:
        test_data = []
        for line in file:
            line_data = []
            game_record = re.search(r':\s*(.*)', line).group(1).strip()
            games = [i.strip() for i in game_record.split(';')]
            
            for game in games:
                game_data = {}
                items = [i.strip() for i in game.split(',')]
                
                for item in items:
                    quantity, color = re.match(r'(\d+)\s+(\w+)', item).groups()
                    game_data[color] = int(quantity)
                
                line_data.append(game_data)
            test_data.append(line_data)
    
    test_answer = checkPossibleGames(test_data)
    
    print(f"Test Answer: {test_answer}")
    
    with open(here/'game_record.txt') as file:
        puzzle_data = []
        for line in file:
            line_data = []
            game_record = re.search(r':\s*(.*)', line).group(1).strip()
            games = [i.strip() for i in game_record.split(';')]
            
            for game in games:
                game_data = {}
                items = [i.strip() for i in game.split(',')]
                
                for item in items:
                    quantity, color = re.match(r'(\d+)\s+(\w+)', item).groups()
                    game_data[color] = int(quantity)
                
                line_data.append(game_data)
            puzzle_data.append(line_data)
    
    puzzle_answer = checkPossibleGames(puzzle_data)
    
    print(f"Final Answer: {puzzle_answer}")
    
    return

if __name__ == "__main__":
    main()