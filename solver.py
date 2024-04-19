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
            current_puzzle = queue.get()
            processed_states += 1
            available_directions = current_puzzle.get_available_moves()
            for direction in search_order:
                if direction in available_directions:
                    new_puzzle = copy.deepcopy(current_puzzle)
                    new_puzzle.move(direction)
                    new_state_flat = tuple(map(tuple, new_puzzle.current_state))
                    if new_state_flat not in visited:
                        if len(new_puzzle.moves) > max_depth:
                            max_depth = len(new_puzzle.moves)
                        if Puzzle.is_solved(new_puzzle):
                            end = time.time()
                            duration_time = end - start
                            print(duration_time)
                            # DO DOPISANIA: tutaj nalezałoby zapisać do pliku informacje o rozwiązaniu
                            return new_puzzle
                        else:
                            queue.put(new_puzzle)
                            visited.add(new_state_flat)
                            visited_states += 1
        return False

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
            current_puzzle, current_depth = stack.pop()
            current_state = tuple(map(tuple, current_puzzle.current_state))
            processed_states += 1

            if current_state in visited and visited[current_state] <= current_depth:
                continue

            visited[current_state] = current_depth

            if Puzzle.is_solved(current_puzzle):
                end = time.time()
                duration_time = end - start
                print(duration_time)
                # DO DOPISANIA: tutaj nalezałoby zapisać do pliku informacje o rozwiązaniu
                return current_puzzle

            available_directions = current_puzzle.get_available_moves()
            if current_depth < max_allowed_depth:
                for direction in search_order:
                    if direction in available_directions:
                        new_puzzle = copy.deepcopy(current_puzzle)
                        new_puzzle.move(direction)
                        stack.append((new_puzzle, current_depth + 1))
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