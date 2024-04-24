import os
import sys

def solve(strategy, parameter):
    directory = 'puzzles'
    for filename in os.listdir(directory):
        input_filename = filename
        index = filename.find('.txt')
        output_filename = filename[:index] + '_' + strategy + '_' + parameter.lower() + "_sol.txt"
        stats_output_filename = filename[:index] + '_' + strategy + '_' + parameter.lower() + ('_stats.txt')
        sys.argv = [ 'main.py', strategy, parameter, input_filename, output_filename, stats_output_filename ]
        exec(open('main.py').read())

def bfs():
    search_orders = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
    for search_order in search_orders:
        solve('bfs', search_order)

def dfs():
    search_orders = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
    for search_order in search_orders:
        solve('dfs', search_order)

def a_star():
    heuristics = ['hamm', 'manh']
    for heuristic in heuristics:
        solve('astr', heuristic)

if __name__ == '__main__':
    bfs()
    dfs()
    a_star()