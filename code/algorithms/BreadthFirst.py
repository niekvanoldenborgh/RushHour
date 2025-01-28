from code.classes.board_class import Board
from collections import deque
import copy
import time
import random
import pandas as pd

def initialize_board(board_file):
    """
    Initializes the board from a file.
    """
    board = Board(board_file)
    board.create()
    board.fill()
    return board

def get_neighbors(board):
    """
    Generates all possible moves or neighbors from the current board state
    """
    moves = [1, -1]
    neighbors = []

    for car in list(board.cars.values()):
        for move in moves:
            if board.is_valid(car, move):
                neighbors.append({'car': car.name, 'move': move})

    # random.shuffle(neighbors)
    # prune = len(neighbors) // 2
    # neighbors = neighbors [:prune]
    return neighbors

def get_neighbor_states(board, visited):
    """
    Generates all neighboring states based on possible moves and adds them to the queue.
    """
    neighbors = get_neighbors(board)
    if not neighbors:
        print('No neighbours')
    neighbor_states = []

    for neighbor in neighbors:
        car = board.cars.get(neighbor['car'])
        move = neighbor['move']
        
        # Apply the move
        board.move(car, move)
        board_tmp = copy.deepcopy(board.board)

        if tuple(sum(board_tmp, [])) not in visited:
            neighbor_states.append((copy.deepcopy(board.get_car_coördinates()), (car.name, move)))

            # TODO: Explain
            visited.add(tuple(sum(board_tmp, [])))

        # Undo the move
        board.move(car, -1 * move)
    
    return neighbor_states

def breadth_first_search(board_file, game, results):
    """
    Implements breadth-first search to solve the board puzzle.
    """
    # Initialize the board
    board = initialize_board(board_file)
    start_time = time.time()

    # Initialize queue and visited set
    queue = deque()
    visited = set()

    # Add the initial board state to the queue
    initial_state = tuple(sum(board.board, []))  
    visited.add(initial_state)
    queue.append((board.get_car_coördinates(), 0, []))

    while queue:
        # Get the next state from the queue
        current_state, moves, path = queue.popleft()
        board.set_board(current_state)
        
        if board.is_won():
            print(f"Moves: {moves}, Time: {time.time() - start_time:.2f} seconds")
            results.append({'moves': moves, 'time_taken': time.time() - start_time})
            get_path_as_csv(path)
            return results

        # Get all valid neighbor states
        neighbors = get_neighbor_states(board, visited)
        for neighbor_state, details in neighbors:
            queue.append((neighbor_state, moves + 1, path + [details]))

        # if moves == 60:
        #     return print(f"Reached depth of 60, {board.show()}")
    
    # If no solution is found
    return results

def get_path_as_csv(path, filename = "output.csv"):
    """
    Return moves needed to solve puzzle as csv
    """
    # Make list of dictionaries that can be transormed to csv
    logbook = []
    for car, move in path:
        logbook.append({"car": car, 'move': move})
        
    # Create csv file
    df = pd.DataFrame(logbook)
    df.to_csv(filename, index = False)
    return print(f"Logbook to saved to {filename}")




