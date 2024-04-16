import copy
import time
import numpy as np

from queue import Queue
from queue import PriorityQueue
from puzzle import Puzzle
from utils import Utils


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
            for direction in search_order:
                new_state = copy.deepcopy(current_state)
                new_state.move(direction)
                if tuple(map(tuple, new_state.current_state)) not in visited:
                    if len(new_state.moves) > max_depth:
                        max_depth = len(new_state.moves)
                    if Puzzle.is_solved(new_state):
                        end = time.time()
                        duration_time = end - start
                        # DO DOPISANIA: tutaj nalezałoby zapisać do pliku informacje o rozwiązaniu
                        return new_state
                    else:
                        queue.put(new_state)
                        visited.add(tuple(map(tuple, new_state.current_state)))
                        visited_states += 1
        return False

    # DO DOKOŃCZENIA - teraz to nie działa XD
    @staticmethod
    def dfs(initial_state, search_order):
        start = time.time()
        processed_states = 0
        visited_states = 1
        visited = {}

        stack = [(initial_state, 0)]
        max_allowed_depth = 20
        max_depth = 0

        while stack:
            current_board, current_depth = stack.pop()
            current_state = tuple(map(tuple, current_board.current_state))
            processed_states += 1

            if current_depth >= max_allowed_depth:
                continue

            if current_state in visited and visited[current_state] <= current_depth:
                continue

            visited[current_state] = current_depth

            if Puzzle.is_solved(current_board):
                end = time.time()
                duration_time = end - start
                # DO DOPISANIA: tutaj nalezałoby zapisać do pliku informacje o rozwiązaniu
                return current_board

            for direction in search_order:
                new_state = copy.deepcopy(current_board)
                new_state.move(direction)
                if tuple(map(tuple, new_state.current_state)) not in visited:
                    stack.append((new_state, current_depth + 1))
                    visited_states += 1
                    if current_depth + 1 > max_depth:
                        max_depth = current_depth + 1

            return False

    # DO ZROBIENIA
    @staticmethod
    def a_star_hamming(initial_state):
        start = time.time()
        max_depth = 0
        processed_states = 0
        visited_states = 1
        priority_queue = PriorityQueue()
        priority_queue.put(
            (len(initial_state.moves)
             + Utils.hamming_distance(initial_state, initial_state.get_traget_state)),
            initial_state)
        visited = set()

    # DO ZROBIENIA
    @staticmethod
    def a_star_manhattan(initial_state):
        start = time.time()
        max_depth = 0
        processed_states = 0
        visited_states = 1
        priority_queue = PriorityQueue()
        priority_queue.put(
            (len(initial_state.moves)
             + Utils.manhattan_distance(initial_state, initial_state.get_traget_state)),
            initial_state)
        visited = set()