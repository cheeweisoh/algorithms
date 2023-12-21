#!/usr/bin/env python3

from pathlib import Path

def parseInput(file: list) -> dict:
    config = {}
    
    for line in file:
        module, dest = line.split(' -> ')
        dest = dest.split(', ')
        if module == 'broadcaster':
            config[module] = ['b', dest, '']
        elif module[0] == '%':
            config[module[1:]] = [module[0], dest, False]
        elif module[0] == '&':
            config[module[1:]] = [module[0], dest, {}]
    
    for module in config.keys():
        for dest in config[module][1]:
            if dest in config.keys() and config[dest][0] == '&':
                config[dest][2][module] = False
            
    return config


def processPulse(mod_to: str, mod_from: str, pulse_type: str, queue: list, config: dict) -> None:
    if mod_to not in config.keys():
        return
    
    mod_type, dest, mem = config[mod_to]
    
    if mod_type == 'b':
        for d in dest:
            queue.append((d, mod_to, pulse_type))
    elif mod_type == '%':
        if pulse_type == 'L':
            new_pulse_type = 'L' if mem else 'H'
            config[mod_to][-1] = not mem
            
            for d in dest:
                queue.append((d, mod_to, new_pulse_type))
    elif mod_type == '&':
        mem[mod_from] = True if pulse_type == 'H' else False
        config[mod_to][-1] = mem
        
        if all(mem.values()):
            new_pulse_type = 'L'
        else:
            new_pulse_type = 'H'
            
        for d in dest:
            queue.append((d, mod_to, new_pulse_type))
    
    return


def pressButton(config: dict) -> (dict, int, int):
    queue = [('broadcaster', '', 'L')]
    low_pulse, high_pulse = 0, 0
    
    while queue:
        mod_to, mod_from, pulse_type = queue.pop(0)
        
        if pulse_type == 'L':
            low_pulse += 1
        else:
            high_pulse += 1
        
        processPulse(mod_to, mod_from, pulse_type, queue, config)
    
    return config, low_pulse, high_pulse


def spamButton(config: dict, times: int) -> int:
    total_low, total_high = 0, 0
    
    for i in range(times):
        config, curr_low, curr_high = pressButton(config)
        total_low += curr_low
        total_high += curr_high
    
    return total_low * total_high



def main():
    here = Path(__file__).parent
    with open(here/'test01.txt') as file:
        test1_data = file.read().splitlines()
        test1_config = parseInput(test1_data)
    
    with open(here/'test02.txt') as file:
        test2_data = file.read().splitlines()
        test2_config = parseInput(test2_data)
    
    with open(here/'config.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_config = parseInput(puzzle_data)
    
    print(f'Test 1 Answer: {spamButton(test1_config, 1000)}')
    print(f'Test 2 Answer: {spamButton(test2_config, 1000)}')
    print(f'Puzzle Answer: {spamButton(puzzle_config, 1000)}')

if __name__ == '__main__':
    main()