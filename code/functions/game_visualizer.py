import pandas as pd
from code.classes.board_class import Board
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

def replay_game(board_file: str, log_file: str) -> None:
    """
    Takes a board file and a corresponding log file
    and replays a game, saving each turn as an image.

    Args:
        board_file (str): The name of the board played on.
        log_file (str): The name of the logbook of a game on said board.

    Returns:
        None
    """

    # read the log
    df_log = pd.read_csv(log_file, sep=',')

    # separate cars from moves
    df_cars = df_log["car"]
    df_moves = df_log["move"]
    
    # initialize board
    board = Board(board_file)
    board.create()
    board.fill()
    board.show()
    print("")

    # initialize grid
    board_figure, axes_figure = plt.subplots()
    axes_figure.grid(linewidth=0.1)
    plt.xlim(0, len(board.board))
    plt.ylim(-len(board.board), 0)
    axes_figure.set_yticklabels([])
    axes_figure.set_xticklabels([])
    
    # for every line in log file
    for turn in range(0, len(df_cars)):

        # select the car on current line and move it
        selected_car = board.cars.get(df_cars[turn])
        board.move(selected_car, df_moves[turn])
        board.show()

        # paint the grid
        for y in range(0, len(board.board)):
            for x in range(0, len(board.board)):

                # '*' means wall, black rectangle
                if board.board[y][x] == '*':
                    axes_figure.add_patch(Rectangle((x, -y - 1), 1, 1, facecolor = 'black'))

                # if not empty spot or exit
                elif board.board[y][x] != '.' and board.board[y][x] != '@':
                    
                    # if not red car
                    if board.board[y][x] != 'X':
                        
                        # character means car, random colour rectangle
                        seed_sum = 0
                        for character in board.board[y][x]:
                            seed_sum = seed_sum + ord(character)
                            # 56 makes pretty colours :)
                            np.random.seed(seed_sum + 56)
                        axes_figure.add_patch(Rectangle((x, -y - 1), 1, 1, facecolor = (np.random.uniform(low=0, high=0.75), np.random.uniform(low=0.1, high=1), np.random.uniform(low=0.1, high=1))))

                    # 'X' means red car, red rectangle
                    else:
                        axes_figure.add_patch(Rectangle((x, -y - 1), 1, 1, facecolor = (1, 0, 0)))

                # else is empty space, white rectangle
                else:
                    axes_figure.add_patch(Rectangle((x, -y - 1), 1, 1, facecolor = 'white'))
                    

        print("")
        plt.savefig(f"game_frame_turn_{turn}.png")