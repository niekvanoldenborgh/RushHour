from numpy import var
from code.classes.board_class import Board
import copy
import random
import time
import pandas as pd

class DepthFirst:
    def __init__(self, board_name: str):
        """
        Initialize game
        """
        # define board and cars
        self.board: var = Board(board_name)
        self.board_name: str = board_name

        # initialize board 
        self.board.create()
        self.board.fill()

        # initial state
        self.states_stack = []
        self.visited = set()
        self.visited.add(tuple(sum(self.board.board, [])))
        self.start_time = time.time()
        self.path = []
        self.path_stack = []
        
    
    def get_neighbours(self):
        """
        Function that generates all possible 1-block moves
        """
        moves = [1, -1]
        neighbours = []

        for car in list(self.board.cars.values()):
            for move in moves:
                if self.board.is_valid(car, move):
                    neighbours.append({'car': car.name, 'move': move})
        
        # shuffle neighbours so algorithm does not always take same
        random.shuffle(neighbours)

        return neighbours
    
    def get_neighbour_states(self):
        
        """
         Function that generates all neighbour states based on possible moves and adds them to the stack
        """
        
        neighbours = self.get_neighbours()

        # move to neighbour, copy move, save the board, go back to initial state
        for neighbour in neighbours:
            car = self.board.cars.get(neighbour['car'])
            move = neighbour['move']
            
            self.board.move(car, move)
            board_tmp = copy.deepcopy(self.board.board)

            # add to stack if not visited
            if tuple(sum(board_tmp, [])) not in self.visited:
                current_coördinates = copy.deepcopy(self.board.get_car_coördinates())
                self.states_stack.append(current_coördinates)
                self.path_stack.append(self.path + [(car.name, move)]) 
                self.visited.add(tuple(sum(board_tmp, [])))

            self.board.move(car, -1*move)           
    
    def next_state(self):
        if self.board.is_won():
            self.elapsed_time = time.time() - self.start_time
            print("Exit found!")
            return True
        
        if self.states_stack:
            new_coördinates = self.states_stack.pop()
            self.path = self.path_stack.pop()
            self.board.set_board(new_coördinates)
            
            
        
        return False
    
    def get_path_as_csv(self, filename = "output.csv"):
         """
         Return moves needed to solve puzzle as csv
         """
        # Make list of dictionaries that can be transormed to csv
         logbook = []
         for car, move in self.path:
             logbook.append({"car": car, 'move': move})
        
        # Create csv file
         df = pd.DataFrame(logbook)
         df.to_csv(filename, index = False)
         print(f"Logbook to saved to {filename}")


    def get_elapsed_time(self):
        return self.elapsed_time

