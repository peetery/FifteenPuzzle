import numpy as np

class Puzzle:
    def __init__(self, size, initial_state):
        self.size = size
        self.initial_state = initial_state
        self.current_state = initial_state
        self.moves = ""

    def __str__(self):
        output = ""
        for row in self.current_state:
            output += " ".join(str(num) for num in row) + "\n"
        return output

    def find_empty_cell(self):
        empty_row, empty_col = None, None
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.current_state[i][j] == 0:
                    empty_row, empty_col = i, j
                    break
            if empty_row is not None:
                break
        return empty_row, empty_col

    def move(self, direction):
        empty_row, empty_col = self.find_empty_cell()

        new_state = np.copy(self.current_state)
        new_row, new_col = empty_row, empty_col

        if direction == "L" and empty_col > 0:
            new_col -= 1
        elif direction == "R" and empty_col < self.size[1] - 1:
            new_col += 1
        elif direction == "U" and empty_row > 0:
            new_row -= 1
        elif direction == "D" and empty_row < self.size[0] - 1:
            new_row += 1

        new_state[empty_row][empty_col] = new_state[new_row][new_col]
        new_state[new_row][new_col] = self.current_state[empty_row][empty_col]

        # sprawdzamy czy nowy stan różni się od obecnego, jest to przydatne aby uniknąć bezcelowego kopiowania
        # gdy zadany ruch wykracza poza granice planszy i nie zostanie wykonany
        if not np.array_equal(self.current_state, new_state):
            self.current_state = new_state
            self.moves += direction

    def get_target_state(self):
        target_state = []
        for i in range(self.size[0]):
            row = []
            for j in range(self.size[1]):
                row.append(i * self.size[1] + j + 1)
            target_state.append(row)
        target_state[-1][-1] = 0
        return target_state

    def is_solved(self):
        return np.array_equal(self.current_state, self.get_target_state())

    def get_neighbors(self):
        neighbors = []
        empty_row, empty_col = self.find_empty_cell()
        for direction in ["L", "R", "U", "D"]:
            new_row, new_col = empty_row, empty_col
            if direction == "L" and empty_col > 0:
                new_col -= 1
            elif direction == "R" and empty_col < self.size[1] - 1:
                new_col += 1
            elif direction == "U" and empty_row > 0:
                new_row -= 1
            elif direction == "D" and empty_row < self.size[0] - 1:
                new_row += 1

            if new_row != empty_row or new_col != empty_col:
                neighbor = np.copy(self.current_state)
                neighbor[empty_row][empty_col] = neighbor[new_row][new_col]
                neighbor[new_row][new_col] = self.current_state[empty_row][empty_col]
                neighbors.append((neighbor, direction))

        return neighbors

