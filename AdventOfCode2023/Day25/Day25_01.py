#!/usr/bin/env python3

from pathlib import Path
import networkx as nx

def parseInput(file: list):
    graph = nx.Graph()
    
    for line in file:
        main_com, con_com = line.split(': ')
        con_com = con_com.split(' ')
        
        for com in con_com:
            graph.add_edge(main_com, com)
            
    return graph


def cutGraph(graph):
    cuts = nx.minimum_edge_cut(graph)
    
    for u, v in cuts:
        graph.remove_edge(u, v)
    
    ans = 1
    for g in list(nx.connected_components(graph)):
        ans *= len(g)
    
    return ans


def main():
    here = Path(__file__).parent
    with open(here/'test.txt') as file:
        test_data = file.read().splitlines()
        test_diagram = parseInput(test_data)
    
    with open(here/'diagram.txt') as file:
        puzzle_data = file.read().splitlines()
        puzzle_diagram = parseInput(puzzle_data)
    
    print(f'Test Answer: {cutGraph(test_diagram)}')
    print(f'Puzzle Answer: {cutGraph(puzzle_diagram)}')


if __name__ == '__main__':
    main()