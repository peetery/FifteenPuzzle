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