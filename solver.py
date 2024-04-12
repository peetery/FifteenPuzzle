import copy
import time
import numpy as np

from queue import Queue
from puzzle import Puzzle


class Solver:
    @staticmethod
    def bfs(initial_state, search_order):
        start = time.time()
        max_depth = 0
        processed_states = 0
        visited_states = 1
        visited = set()
        queue = Queue()
        queue.put(initial_state)
        while not queue.empty():
            current_state = queue.get()
            processed_states += 1
            if Puzzle.is_solved(current_state):
                return 1
            for direction in search_order:
                new_state = copy.deepcopy(current_state)
                new_state.move(direction)
                if tuple(new_state.layout.flatten()) not in visited_states:
                    if len(new_state.moves) > max_depth:
                        max_depth = len(new_state.moves)
                    if np.array_equal(new_state, new_state.get_target_state):
                        end = time.time()
                        duration_time = end - start
                        # DO DOPISANIA: tutaj nalezałoby zapisać do pliku informacje o rozwiązaniu
                        return True
                    else:
                        queue.put(new_state)
                        visited.add(tuple(new_state.layout.flatten()))
                        visited_states += 1
        return False