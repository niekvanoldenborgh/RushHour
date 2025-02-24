from code.classes.board_class import Board
import random

def random_algorithm(board_file: str, games: int) -> None:
    """
    Takes a board file, and a desired amount of games played,
    and plays that many games of Rush Hour on that board.
    This algorithm selects random vehicles
    and moves them in random directions until victory is achieved.

    Args:
        board_file (str): The name of a board in the gameboards directory.
        games (int): The desired amount of games.

    Returns:
        None
    """
    board1 = Board(board_file)
    turn_counter_list: list = []

    # initiate board
    for game in range(0, games):
        board1.create()
        board1.fill()

        turn_counter: int = 0

        # play until game won
        while board1.is_won() == False:

            # select random car based on the length of list of car names
            selected_car = board1.cars.get(board1.car_names[random.randint(0, len(board1.car_names) - 1)])
            car_moved = False

            # keep trying until a car moves
            while car_moved == False:

                # if only one direction is available, move in that direction
                if board1.is_valid(selected_car, 1) == True and board1.is_valid(selected_car, -1) == False:
                    board1.move(selected_car, 1)
                    car_moved = True

                elif board1.is_valid(selected_car, 1) == False and board1.is_valid(selected_car, -1) == True:
                    board1.move(selected_car, -1)
                    car_moved = True

                # if both directions are available, move in random direction
                elif board1.is_valid(selected_car, 1) == True and board1.is_valid(selected_car, -1) == True:
                    board1.move(selected_car, random.choice([-1,1]))
                    car_moved = True

                # if neither direction is available, select a different car
                elif board1.is_valid(selected_car, 1) == False and board1.is_valid(selected_car, -1) == False:
                    selected_car = board1.cars.get(board1.car_names[random.randint(0, len(board1.car_names) - 1)])

            turn_counter += 1

        # save data
        print(turn_counter)
        turn_counter_list.append(turn_counter)
        board1.save_logbook(filename = f"logbook{game}.csv")
