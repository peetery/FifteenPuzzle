from puzzle import Puzzle
from utils import Utils
from solver import Solver

if __name__ == '__main__':
    size, initial_state = Utils.load_puzzle_from_file("startPuzzle.txt")
    puzzle = Puzzle(size, initial_state)
    print("Aktualny stan:")
    print(puzzle)
    print(Solver.dfs(puzzle, "LRUD"))

    Utils.save_puzzle_to_file("modifiedPuzzle.txt", puzzle.size, puzzle.current_state)
