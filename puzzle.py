import numpy as np

class Puzzle:
    def __init__(self, size, initial_state):
        self.size = size
        self.initial_state = initial_state
        self.current_state = initial_state
        self.moves = ""

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.size = tuple(map(int, lines[0].split()))
            self.current_state = [list(map(int, line.split())) for line in lines[1:]]

    def __str__(self):
        output = ""
        for row in self.current_state:
            output += " ".join(str(num) for num in row) + "\n"
        return output

    def move(self, direction):
        empty_row, empty_col, new_row, new_col = None, None, None, None
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.current_state[i][j] == 0:
                    empty_row, empty_col = i, j
                    break
            if empty_row is not None:
                break

        new_state = np.copy(self.current_state)

        if direction == "L" and empty_col > 0:
            new_row, new_col = empty_row, empty_col - 1
        elif direction == "R" and empty_col < self.size[1] - 1:
            new_row, new_col = empty_row, empty_col + 1
        elif direction == "U" and empty_row < self.size[0] - 1:
            new_row, new_col = empty_row + 1, empty_col
        elif direction == "D" and empty_row > 0:
            new_row, new_col = empty_row - 1, empty_col

        new_state[empty_row][empty_col] = new_state[new_row][new_col]
        new_state[new_row][new_col] = new_state[empty_row][empty_col]

        # sprawdzamy czy nowy stan różni się od obecnego, jest to przydatne aby uniknąć bezcelowego kopiowania
        # gdy zadany ruch wykracza poza granice planszy i nie zostanie wykonany
        if not np.array_equal(self.current_state, new_state):
            self.current_state = new_state
            self.moves += direction