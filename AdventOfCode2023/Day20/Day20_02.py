#!/usr/bin/env python3

from pathlib import Path
import math

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
            if dest == 'rx':
                pen_mod = module
            if dest in config.keys() and config[dest][0] == '&':
                config[dest][2][module] = False
            
    return config, pen_mod


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


def checkLowPulse(config: dict, pen_mod: str):
    factors = {x: 0 for x in config[pen_mod][2].keys()}
    count = 0
    
    def pressButton(config: dict) -> (dict, int, int):
        queue = [('broadcaster', '', 'L')]
    
        while queue:
            mod_to, mod_from, pulse_type = queue.pop(0)        
            processPulse(mod_to, mod_from, pulse_type, queue, config)
            
            for key in config[pen_mod][2].keys():
                if (not factors[key]) and (config[pen_mod][2][key] == True):
                    factors[key] = count
    
        return config
    
    while not all(factors.values()):
        count += 1
        config = pressButton(config)
        
    return math.lcm(*factors.values())


def main():
    here = Path(__file__).parent    
    with open(here/'config.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_config, puzzle_pen_mod = parseInput(puzzle_data)
    
    print(f'Puzzle Answer: {checkLowPulse(puzzle_config, puzzle_pen_mod)}')

if __name__ == '__main__':
    main()