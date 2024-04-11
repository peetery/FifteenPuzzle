class Utils:
    @staticmethod
    def load_puzzle_from_file(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            size = tuple(map(int, lines[0].split()))
            initial_state = [list(map(int, line.split())) for line in lines[1:]]
            return size, initial_state

    @staticmethod
    def save_puzzle_to_file(filename, size, state):
        with open(filename, 'w') as file:
            file.write(f"{size[0]} {size[1]}\n")
            for row in state:
                file.write(" ".join(str(num) for num in row) + "\n")