from puzzle import Puzzle

if __name__ == '__main__':
    puzzle = Puzzle((0, 0), [])
    puzzle.load_from_file("startPuzzle.txt")
    print("Aktualny stan:")
    print(puzzle)
    print("Docelowy stan:")
    print(puzzle.get_target_state())
    print("\nis solved: ", puzzle.is_solved())

    for neighbor, direction in puzzle.get_neighbors():
        print(neighbor, "Ruch:", direction)
