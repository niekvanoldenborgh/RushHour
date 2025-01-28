from code.classes.board_class import Board
import pandas as pd
import random
import time

def random_algorithm_heuristics(board_file: str, depth: int, max_runs: int, max_run_time: int = 600, max_game_time: int = 60) -> None:

    # amount of times the algorithm runs
    for run in range(0, max_runs):
        turn_counter_list: list = []
        total_time: float = time.time()

        # maximum turns
        max_depth = depth

        # make sure timeout is false to clear next loops
        timeout: bool = False

        # stop when max_run_time is reached or has timed out
        while time.time() - total_time < max_run_time and timeout == False:

            # initiate board
            board: Board = Board(board_file)
            game_time = time.time()
            board.create()
            board.fill()
            turn_counter: int = 0

            # stop when game is won or has timed out
            while board.is_won() == False and timeout == False:

                # select random car based on the length of list of car names
                selected_car = board.cars.get(board.car_names[random.randint(0, len(board.car_names) - 1)])
                car_moved = False

                # keep trying until a car moves
                while car_moved == False:

                    # if only one direction is available, move in that direction
                    if board.is_valid(selected_car, 1) == True and board.is_valid(selected_car, -1) == False:
                        board.move(selected_car, 1)
                        car_moved = True

                    elif board.is_valid(selected_car, 1) == False and board.is_valid(selected_car, -1) == True:
                        board.move(selected_car, -1)
                        car_moved = True

                    # if both directions are available, move in random direction
                    elif board.is_valid(selected_car, 1) == True and board.is_valid(selected_car, -1) == True:
                        board.move(selected_car, random.choice([-1,1]))
                        car_moved = True

                    # if neither direction is available, select a different car
                    elif board.is_valid(selected_car, 1) == False and board.is_valid(selected_car, -1) == False:
                        selected_car = board.cars.get(board.car_names[random.randint(0, len(board.car_names) - 1)])

                turn_counter += 1

                # if max depth reached, restart game
                if turn_counter > max_depth:
                        turn_counter = 0
                        board = Board(board_file)
                        board.create()
                        board.fill()

                # if max time reached, save data and time out
                if time.time() - game_time > max_game_time:
                    print("timeout")
                    df = pd.DataFrame(turn_counter_list)
                    df.to_csv(f"results_{run + 1}.csv", index = False)
                    timeout = True


            # if last game didnt time out, save log
            if timeout == False:
                print(f"{turn_counter} turns played")
                print(f"{round(time.time() - game_time, 2)} seconds played")
                turn_counter_list.append({'turns': turn_counter, 'time': round(time.time() - game_time, 2), 'total_time': round(time.time() - total_time, 2)})
                max_depth = turn_counter
                board.save_logbook(filename = f"logbook_{run + 1}_{turn_counter}_turns.csv")

        # save the results
        df = pd.DataFrame(turn_counter_list)
        df.to_csv(f"results_{run + 1}.csv", index = False)
