import os
import sys

import numpy as np

class Utils:
    @staticmethod
    def save_solution_to_file(moves, visited_states_num, processed_states_num, max_reached_depth, calculation_time):
        first_index = sys.argv[4].find('_')
        second_index = sys.argv[4].find('_', first_index + 1)
        third_index = sys.argv[4].find('_', second_index + 1)
        fourth_index = sys.argv[4].find('_', third_index + 1)
        fifth_index = sys.argv[4].find('_', fourth_index + 1)
        layout = sys.argv[4][first_index + 1:second_index].lstrip('0')
        strategy = sys.argv[4][third_index + 1:fourth_index]
        parameter = sys.argv[4][fourth_index + 1:fifth_index]
        filename = os.path.join('solutions', strategy, layout, parameter, sys.argv[4])
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        stats_filename = os.path.join('stats', strategy, layout, parameter, sys.argv[5])
        os.makedirs(os.path.dirname(stats_filename), exist_ok=True)
        with open(filename, 'w') as file:
            if moves is None:
                file.write("-1")
            else:
                file.write(f"{len(moves)}\n")
                file.write("".join(moves))

        with open(stats_filename, 'w') as stats_file:
            if moves is None:
                stats_file.write("-1\n")
            else:
                stats_file.write(f"{len(moves)}\n")

            stats_file.write(f"{visited_states_num}\n")
            stats_file.write(f"{processed_states_num}\n")
            stats_file.write(f"{max_reached_depth}\n")
            stats_file.write(f"{calculation_time:.3f}")

    @staticmethod
    def hamming_distance(state, target_state):
        distance = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != target_state[i][j]:
                    distance += 1
        return distance

    @staticmethod
    def manhattan_distance(state, target_state):
        distance = 0
        size = len(state)
        for i in range(size):
            for j in range(size):
                num = state[i][j]
                if num != 0:
                    cell = np.argwhere(state == num)
                    target_cell = np.argwhere(target_state == num)
                    distance += np.sum(np.abs(cell - target_cell))
        return distance