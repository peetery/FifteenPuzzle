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

    @staticmethod
    def hamming_distance(state, target_state):
        distance = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != target_state[i][j]:
                    distance += 1
        return distance

    # ta implementacja manhattan distance jeszcze do przemyślenia / ewentualnej zmiany
    @staticmethod
    def manhattan_distance(state, target_state):
        distance = 0
        size = len(state)
        for i in range(size):
            for j in range(size):
                num = state[i][j]
                if num != 0:
                    target_row, target_col = divmod(num - 1, size)
                    distance += abs(i - target_row) + abs(j - target_col)
        return distance