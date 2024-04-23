import sys
import time

from puzzle import Puzzle
from solver import Solver
from utils import Utils

if __name__ == '__main__':
    strategy = sys.argv[1]
    additional_parameter = sys.argv[2]
    input_filename = "puzzles/" + sys.argv[3]
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()
        size = tuple(map(int, lines[0].split()))
        initial_state = [list(map(int, line.split())) for line in lines[1:]]
    original_puzzle = Puzzle(size, initial_state)
    if strategy == 'bfs':
        Solver.bfs(original_puzzle, additional_parameter)
    elif strategy == "dfs":
        Solver.dfs(original_puzzle, additional_parameter)
    elif strategy == "astr":
        if additional_parameter == "hamm":
            Solver.a_star_hamming(original_puzzle)
        elif additional_parameter == "manh":
            Solver.a_star_manhattan(original_puzzle)
        else:
            print("Error - invalid parameter.")
    else:
        print("Error - invalid strategy.")