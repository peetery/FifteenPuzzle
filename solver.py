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
                if tuple(new_state.layout.flatten()) not in visited:
                    if len(new_state.moves) > max_depth:
                        max_depth = len(new_state.moves)
                    if Puzzle.is_solved(new_state):
                        end = time.time()
                        duration_time = end - start
                        # DO DOPISANIA: tutaj nalezałoby zapisać do pliku informacje o rozwiązaniu
                        return True
                    else:
                        queue.put(new_state)
                        visited.add(tuple(new_state.layout.flatten()))
                        visited_states += 1
        return False

    # DO DOKOŃCZENIA - nie do końca mi pasuje ta implementacja, trochę inaczej to trzeba chyba zrobić
    @staticmethod
    def dfs(initial_state, search_order):
        start = time.time()
        max_depth = 0
        processed_states = 0
        visited_states = 1
        visited = set()

        stack = []
        stack.append(initial_state, 0)
        max_allowed_depth = 20

        while stack:
            current_state, depth = stack.pop()
            processed_states += 1

            if depth >= max_allowed_depth:
                continue

            if Puzzle.is_solved(current_state):
                end = time.time()
                duration_time = end - start
                # DO DOPISANIA: tutaj nalezałoby zapisać do pliku informacje o rozwiązaniu
                return True

            visited.add(tuple(current_state.layout_flatten()))

            for direction in search_order:
                new_state = copy.deepcopy(current_state)
                new_state.move(direction)
                if tuple(new_state.layout.flatten()) not in visited:
                    stack.append((new_state, depth + 1))
                    visited_states += 1
                    if depth + 1 > max_depth:
                        max_depth = depth

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