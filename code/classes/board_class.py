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
        Create empty board
        """
        self.N = int(self.df['N'].iloc[0])
        self.board = list()

        # plot
        self.board_figure, self.axes_figure = plt.subplots()
        self.axes_figure.grid(linewidth=0.1)
        plt.xlim(0, self.N + 2)
        plt.ylim(-self.N - 2, 0)

        for row in range(self.N + 2):
            self.board.append(['.'] * (self.N + 2))

        # Create border rows
        for i in range(self.N + 2):
            self.board[0][i] = "*"
            self.board[self.N + 1][i] = "*"

            # paint black squares at border rows
            self.axes_figure.add_patch(Rectangle((0, -i - 1), 1, 1, facecolor = 'black'))
            self.axes_figure.add_patch(Rectangle((self.N + 1, -i - 1), 1, 1, facecolor = 'black'))

        # Create border columns
        for i in range(self.N + 2):
            self.board[i][0] = "*"
            self.board[i][self.N + 1] = "*"

            # paint black squares at border columns
            self.axes_figure.add_patch(Rectangle((i, -1), 1, 1, facecolor = 'black'))
            self.axes_figure.add_patch(Rectangle((i, -self.N - 2), 1, 1, facecolor = 'black'))

        # Locate and place opening on the border
        if self.N % 2 == 0:
            opening_index = (self.N // 2, self.N + 1)
        else:
            opening_index = (self.N // 2 + 1, self.N + 1)

        self.board[opening_index[0]][opening_index[1]] = '@'

        # place white square at exit
        self.axes_figure.add_patch(Rectangle((opening_index[1], -opening_index[0] - 1), 1, 1, facecolor = 'white'))


    def place(self, car: var) -> None:
        """
        Simple function to place a car in a position
        """
        for x, y in car.get_current_coördinates():
            self.board[x][y] = car.name

            # random colours based on car name
            if car.name != 'X':
                self.seed_sum = 0
                for character in car.name:
                    self.seed_sum = self.seed_sum + ord(character)
                    # 56 makes pretty colours :)
                    np.random.seed(self.seed_sum + 56)
                self.axes_figure.add_patch(Rectangle((y, -x - 1), 1, 1, facecolor = (np.random.uniform(low=0, high=0.75), np.random.uniform(low=0.1, high=1), np.random.uniform(low=0.1, high=1))))

            # red car, name 'X', always red
            else:
                self.axes_figure.add_patch(Rectangle((y, -x - 1), 1, 1, facecolor = (1, 0, 0)))

    def unplace(self, car: var):
        for x, y in car.get_current_coördinates():
            self.board[x][y] = '.'
            self.axes_figure.add_patch(Rectangle((y, -x - 1), 1, 1, facecolor = 'white'))

    def fill(self):
        """
        Fill the board with cars in their inital values
        """
        for car in self.cars.values():
            self.place(car)


    def is_valid(self, car: var, blocks: int) -> bool:

        # Check if move possible (all blocks are empty)
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

        if self.is_valid(car, blocks) == True:

            # first unplace car from postition
            self.unplace(car)

            # move car
            for i in range(car.length):
                if car.orientation == "H":
                    car.current_coördinates[i][1] = car.current_coördinates[i][1] + blocks
                if car.orientation == "V":
                    car.current_coördinates[i][0] = car.current_coördinates[i][0] + blocks

            self.place(car)

            self.logbook.append({'car': car.name, 'move': blocks})
            return True
        
        return False

    def save_logbook(self, filename = "logbook.csv"):
        """
        Save logbook to csv
        """

        df = pd.DataFrame(self.logbook)
        df.to_csv(filename, index = False)
        print(f"Logbook to saved to {filename}")

    def show(self) -> None:
        """
        Function to let user see the board
        """
        # saves a figure of the current board state
        # need to think of a way to animate this
        # plt.show() could work but fails in cs50
        plt.savefig('Rush Hour Board classes')
        for row in self.board:
            print(row)

    def is_won(self) -> None:
        """
        Checks if the game is in winning configuration.
        The game is won if the red car ('X') reaches the exit.
        """
        exit = self.N + 1

        for placement in self.red_car.get_current_coördinates:
            if placement == exit:
                print("Congrats")
                return True

        return False


