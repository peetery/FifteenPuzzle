import copy
import time
import numpy as np

from queue import Queue
from queue import PriorityQueue

import utils
from puzzle import Puzzle
from utils import Utils


class Solver:
    @staticmethod
    def bfs(initial_puzzle, search_order):
        start = time.perf_counter()
        max_depth = 0
        processed_states = 0
        visited_states = 1
        visited = set()
        queue = Queue()
        queue.put(initial_puzzle)
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
                            end = time.perf_counter()
                            duration_time = end - start
                            Utils.save_solution_to_file(new_puzzle.moves, visited_states,
                                                        processed_states, max_depth, duration_time)
                            return new_puzzle
                        else:
                            queue.put(new_puzzle)
                            visited.add(new_state_flat)
                            visited_states += 1
        end = time.perf_counter()
        duration_time = end - start
        Utils.save_solution_to_file(None, visited_states, processed_states, max_depth, duration_time)
        return None

    @staticmethod
    def dfs(initial_puzzle, search_order):
        start = time.perf_counter()
        processed_states = 0
        visited_states = 1
        visited = {}

        stack = [(initial_puzzle, 0)]
        max_allowed_depth = 20
        max_depth = 0

        while stack:
            current_puzzle, current_depth = stack.pop()
            current_state_flat = tuple(map(tuple, current_puzzle.current_state))
            processed_states += 1

            if current_state_flat in visited and visited[current_state_flat] <= current_depth:
                continue

            visited[current_state_flat] = current_depth

            if Puzzle.is_solved(current_puzzle):
                end = time.perf_counter()
                duration_time = end - start
                Utils.save_solution_to_file(current_puzzle.moves, visited_states,
                                            processed_states, max_depth, duration_time)
                return current_puzzle

            available_directions = current_puzzle.get_available_moves()
            if current_depth < max_allowed_depth:
                for direction in reversed(search_order):
                    if direction in available_directions:
                        new_puzzle = copy.deepcopy(current_puzzle)
                        new_puzzle.move(direction)
                        stack.append((new_puzzle, current_depth + 1))
                        visited_states += 1
                        if current_depth + 1 > max_depth:
                            max_depth = current_depth + 1
        end = time.perf_counter()
        duration_time = end - start
        Utils.save_solution_to_file(None, visited_states, processed_states, max_depth, duration_time)
        return None

    # DO ZROBIENIA
    @staticmethod
    def a_star_hamming(initial_puzzle):
        start = time.perf_counter()
        max_depth = 0
        processed_states = 0
        visited_states = 1
        priority_queue = PriorityQueue()
        priority_queue.put(
            (len(initial_puzzle.moves)
             + Utils.hamming_distance(initial_puzzle.current_state, initial_puzzle.get_target_state()),
            initial_puzzle))
        visited = set()

        while not priority_queue.empty():
            current_puzzle = priority_queue.get()[1]
            processed_states += 1

            if Puzzle.is_solved(current_puzzle):
                end = time.perf_counter()
                duration_time = end - start
                Utils.save_solution_to_file(current_puzzle.moves, visited_states,
                                            processed_states, max_depth, duration_time)
                return current_puzzle

            available_directions = current_puzzle.get_available_moves()
            for direction in "LRUD":
                if direction in available_directions:
                    new_puzzle = copy.deepcopy(current_puzzle)
                    new_puzzle.move(direction)
                    new_state_flat = tuple(map(tuple, new_puzzle.current_state))
                    if new_state_flat not in visited:
                        priority_queue.put(
                                (len(new_puzzle.moves)
                                 + Utils.hamming_distance(new_puzzle.current_state, new_puzzle.get_target_state()),
                                new_puzzle))
                        visited_states += 1
                        visited.add(new_state_flat)
                        if len(new_puzzle.moves) > max_depth:
                            max_depth = len(new_puzzle.moves)
        end = time.perf_counter()
        duration_time = end - start
        Utils.save_solution_to_file(None, visited_states, processed_states, max_depth, duration_time)
        return None

    # DO ZROBIENIA
    @staticmethod
    def a_star_manhattan(initial_puzzle):
        start = time.perf_counter()
        max_depth = 0
        processed_states = 0
        visited_states = 1
        priority_queue = PriorityQueue()
        priority_queue.put(
            (len(initial_puzzle.moves)
             + Utils.manhattan_distance(initial_puzzle.current_state, initial_puzzle.get_target_state()),
             initial_puzzle))
        visited = set()

        while not priority_queue.empty():
            current_puzzle = priority_queue.get()[1]
            processed_states += 1

            if Puzzle.is_solved(current_puzzle):
                end = time.perf_counter()
                duration_time = end - start
                Utils.save_solution_to_file(current_puzzle.moves, visited_states,
                                            processed_states, max_depth, duration_time)
                return current_puzzle

            available_directions = current_puzzle.get_available_moves()
            for direction in "LRUD":
                if direction in available_directions:
                    new_puzzle = copy.deepcopy(current_puzzle)
                    new_puzzle.move(direction)
                    new_state_flat = tuple(map(tuple, new_puzzle.current_state))
                    if new_state_flat not in visited:
                        priority_queue.put(
                                (len(new_puzzle.moves)
                                 + Utils.manhattan_distance(new_puzzle.current_state, new_puzzle.get_target_state()),
                                new_puzzle))
                        visited_states += 1
                        visited.add(new_state_flat)
                        if len(new_puzzle.moves) > max_depth:
                            max_depth = len(new_puzzle.moves)
        end = time.perf_counter()
        duration_time = end - start
        Utils.save_solution_to_file(None, visited_states, processed_states, max_depth, duration_time)
        return None