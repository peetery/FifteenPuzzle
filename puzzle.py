class Puzzle:
    def __init__(self, size, initial_state):
        self.size = size
        self.initial_state = initial_state
        self.current_state = initial_state

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
        empty_row, empty_col = None, None
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.current_state[i][j] == 0:
                    empty_row, empty_col = i, j
                    break
            if empty_row is not None:
                break

        # ! niedokończone, patrz niżej
        if direction == "L":
            new_row, new_col = empty_row, empty_col - 1
        elif direction == "R":
            new_row, new_col = empty_row, empty_col + 1
        elif direction == "U":
            new_row, new_col = empty_row + 1, empty_col
        elif direction == "D":
            new_row, new_col = empty_row - 1, empty_col
        # teraz trzeba jeszcze pomyśleć nad zabezpieczeń aby nie wyjść poza granice planszy