from puzzle import Puzzle

if __name__ == '__main__':
    puzzle = Puzzle((0, 0), [])
    puzzle.load_from_file("startPuzzle.txt")
    print(puzzle)
    print("Rozmiar tablicy: ", puzzle.size)
