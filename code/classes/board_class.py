from numpy import var
import pandas as pd
import os
from car_class import Car

class Board:

    def __init__(self, file: str) -> None:
        """
        Load data from csv file
        """
        
        # Load csv file 
        if file[-3:] != 'csv':
            raise ValueError("File should be .csv format")

        self.file_path: str = "gameboards/" + file 
        
        if os.path.exists(self.file_path):
            self.df = pd.read_csv(self.file_path)
        else:
            raise FileNotFoundError(f"The file '{self.file_path}' does not exist")
        
        # Read car data and add to dictionary
        self.cars: dict[var] = {}
        nrows_df = self.df.shape[0]

        for r in range(nrows_df):
            car_data = list(self.df.iloc[r][:-1])
            car = Car(*car_data)
            self.cars[car.name] = car

        # define red car
        self.red_car = self.cars.get("X")

    def create(self):
        """
        Create empty board 
        """
        self.N = int(self.df['N'].iloc[0])
        self.board = list()

        for row in range(self.N + 2):
            self.board.append(['.'] * (self.N + 2))

        # Create border rows
        for i in range(self.N + 2):
            self.board[0][i] = "*"
            self.board[self.N + 1][i] = "*"

        # Create border columns
        for i in range(self.N + 2):
            self.board[i][0] = "*"
            self.board[i][self.N + 1] = "*"

        # Locate and place opening on the border
        if self.N % 2 == 0:
            opening_index = (self.N // 2, self.N + 1)
        else:
            opening_index = (self.N // 2 + 1, self.N + 1)

        self.board[opening_index[0]][opening_index[1]] = '@'


    def place(self, car: var) -> None:
        """
        Simple function to place a car in a position
        """
        for x, y in car.get_current_coördinates():
            self.board[x][y] = car.name
    
    def unplace(self, car: var):
        for x, y in car.get_current_coördinates():
            self.board[x][y] = '.'

    def fill(self):
        """
        Fill the board with cars in their inital values
        """
        for car in self.cars.values():
            self.place(car)
        

    def move(self, car: var, direction: str, blocks: int) -> bool:
        
        # Raise an error when invalid value is given
        if car.orientation == "H" and direction.upper() not in ("L", "R"):
            raise ValueError("Direction should be 'L' or 'R' for horizontal cars")
            
        elif car.orientation == "V" and direction.upper() not in ("U", "D"):
            raise ValueError("Direction should be 'U' or 'D' for vertical cars")
        
        # Check if move possible (all blocks are empty)
        for i in range(blocks):    
            if direction.upper() == "L":
                if self.board[car.row][car.current_coördinates[0][1] - range(1, blocks + 1)[i]] != ".":
                    return False
            if direction.upper() == "R":
                if self.board[car.row][car.current_coördinates[car.length - 1][1] + range(1, blocks+ 1)[i]] != ".":
                    return False 
            if direction.upper() == "U":
                if self.board[car.current_coördinates[0][0] - range(1, blocks + 1)[i]][car.col] != ".":
                    return False 
            if direction.upper() == "D":    
                if self.board[car.current_coördinates[car.length - 1][0] + range(1, blocks + 1)[i]][car.col] != ".":
                    return False
        
        # first unplace car from postition
        self.unplace(car)

        # move car 
        for i in range(car.length):
            if direction.upper() == "L":
                car.current_coördinates[i][1] = car.current_coördinates[i][1] - blocks
            if direction.upper() == "R":
                car.current_coördinates[i][1] = car.current_coördinates[i][1] + blocks
            if direction.upper() == "U":
                car.current_coördinates[i][0] = car.current_coördinates[i][0] - blocks
            if direction.upper() == "D":
                car.current_coördinates[i][0] = car.current_coördinates[i][0] + blocks

        self.place(car)
        return True

    def show(self) -> None:
        """
        Function to let user see the board
        """
        for row in self.board:
            print(row)