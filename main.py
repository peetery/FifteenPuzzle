from puzzle import Puzzle
from utils import Utils

if __name__ == '__main__':
    size, initial_state = Utils.load_puzzle_from_file("startPuzzle.txt")
    puzzle = Puzzle(size, initial_state)
    print("Aktualny stan:")
    print(puzzle)
    print("Docelowy stan:")
    print(puzzle.get_target_state())
    print("\nis solved: ", puzzle.is_solved())
    print("\nStany wszystkich sąsiadów:")
    for neighbor, direction in puzzle.get_neighbors():
        print(neighbor, "Ruch:", direction)

    print("\nWykonujemy ruch L:")
    puzzle.move("L")
    print("Stan układanki po wykonaniu ruchu:")
    print(puzzle)
    Utils.save_puzzle_to_file("modifiedPuzzle.txt", puzzle.size, puzzle.current_state)
