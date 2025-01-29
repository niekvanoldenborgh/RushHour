import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from numpy import var
import pandas as pd
import os
from code.classes.car_class import Car

class Board:

    def __init__(self, file: str) -> None:
        """
        Load game configurartion from csv file
        """

        # load csv file
        if file[-3:] != 'csv':
            raise ValueError("File should be .csv format")

        self.file_path: str = "gameboards/" + file

        if os.path.exists(self.file_path):
            self.df = pd.read_csv(self.file_path)
        else:
            raise FileNotFoundError(f"The file '{self.file_path}' does not exist")

        # read car data and add to dictionary
        self.cars: dict[var] = {}
        self.car_names: list[var] = []
        nrows_df = self.df.shape[0]

        for r in range(nrows_df):
            car_data = list(self.df.iloc[r][:-1])
            car = Car(*car_data)
            self.car_names.append(car.name)
            self.cars[car.name] = car

        # define red car
        self.red_car = self.cars.get("X")

        # create logbook
        self.logbook: list = []

    def create(self):
        """
        Create board representation.

        - Empty spots: '.'
        - Border: '*'
        - Opening: '@'
        """

        # initialize variables
        self.N = int(self.df['N'].iloc[0])
        self.board = list()

        # initialize grid
        for row in range(self.N + 2):
            self.board.append(['.'] * (self.N + 2))

        # fill grid with border rows
        for i in range(self.N + 2):
            self.board[0][i] = "*"
            self.board[self.N + 1][i] = "*"

        # fill grid with border columns 
        for i in range(self.N + 2):
            self.board[i][0] = "*"
            self.board[i][self.N + 1] = "*"

        # locate and place opening on the border
        if self.N % 2 == 0:
            self.opening_index = (self.N // 2, self.N + 1)
        else:
            self.opening_index = (self.N // 2 + 1, self.N + 1)

        self.board[self.opening_index[0]][self.opening_index[1]] = '@'


    def place(self, car: var) -> None:
        """
        Simple method to place a car in a position on the board.
        """
        for x, y in car.get_current_coördinates():
            self.board[x][y] = car.name

    def unplace(self, car: var):
        """
        Simple method to unplace a car from the board.
        """
        for x, y in car.get_current_coördinates():
            self.board[x][y] = '.'

    def fill(self):
        """
        Fill the board with cars in their inital state.
        """
        for car in self.cars.values():
            self.place(car)

    def is_valid(self, car: var, blocks: int) -> bool:
        """
        Method that verifies if move is possible.
        """

        # Check if move possible (all blocks in range are empty)
        if blocks > 0:
            for i in range(blocks):
                if car.orientation == "H":
                     if self.board[car.row][car.current_coördinates[car.length - 1][1] + range(1, blocks+ 1)[i]] != ".":
                        return False
                elif car.orientation == "V":
                    if self.board[car.current_coördinates[car.length - 1][0] + range(1, blocks + 1)[i]][car.col] != ".":
                        return False
        elif blocks < 0:
            for i in range(-blocks):
                if car.orientation == "H":
                    if self.board[car.row][car.current_coördinates[0][1] - range(1, -blocks + 1)[i]] != ".":
                        return False
                elif car.orientation == "V":
                    if self.board[car.current_coördinates[0][0] - range(1, -blocks + 1)[i]][car.col] != ".":
                        return False

        return True

    def move(self, car: var, blocks: int) -> bool:
        """
        Method that moves a car if the move is valid.
        """

        # verify if move is valid
        if self.is_valid(car, blocks) == True:

            # unplace car from current postition
            self.unplace(car)

            # change car coördinates
            for i in range(car.length):
                if car.orientation == "H":
                    car.current_coördinates[i][1] = car.current_coördinates[i][1] + blocks
                if car.orientation == "V":
                    car.current_coördinates[i][0] = car.current_coördinates[i][0] + blocks

            # place car in new postition
            self.place(car)
            self.logbook.append({'car': car.name, 'move': blocks})

            return True

        return False

    def save_logbook(self, filename = "logbook.csv"):
        """
        Method that creates a logbook of all moves made (format is compatible with check50).
        """

        df = pd.DataFrame(self.logbook)
        df.to_csv(filename, index = False)
        print(f"Logbook to saved to {filename}")

    def show(self) -> None:
        """
        Simple method to print board in the console.
        """
        for row in self.board:
            print(row)

    def is_won(self) -> None:
        """
        Checks if the game is in winning configuration.
        The game is won if the red car ('X') reaches the exit.
        """
        exit = [self.opening_index[0], self.opening_index[1] - 1]

        for placement in self.red_car.get_current_coördinates():
            if placement == exit:
                print("Congrats")
                return True

        return False

    def get_car_coördinates(self):
        """
        Function returning all current coördinates of the cars.
        """
        car_coördinates = dict()
        
        # add all coördinates to a dict, then return
        for car in self.cars.values():
            car_coördinates[car.name] = car.get_current_coördinates()

        return car_coördinates

    def set_board(self, car_coördinates: dict):
        """
        Function that sets board to new car coördinates.
        """
        
        # Unplace cars and change coördinates
        for car in self.cars.values():
            self.unplace(car)
            car.current_coördinates = car_coördinates[car.name]
        
        # Place car in new position
        for car in self.cars.values():
            self.place(car)


