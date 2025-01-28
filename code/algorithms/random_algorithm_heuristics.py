from code.classes.board_class import Board
import pandas as pd
import random
import time

"""
how to go about analysing the data?
we could take an average amount of time to get a sub [x] score?
that might be good actually

would maybe be nice to have a .csv
that also recounts all the [tunrs, time] from the session
"""

def random_algorithm_heuristics(board_file, depth, max_games, max_run_time = 600, max_game_time = 60):
    # total amount of games played
    for game in range(0, max_games):
        turn_counter_list = []
        total_time = time.time()
        max_depth = depth

        # set timeout to false to start the running
        timeout = False

        # while below allowed runtime and it hasnt timed out
        while time.time() - total_time < max_run_time and timeout == False:

            # initiate board
            board1 = Board(board_file)
            game_time = time.time()
            board1.create()
            board1.fill()
            # print("start")

            turn_counter = 0

            # while game isnt won and hasnt timed out
            while board1.is_won() == False and timeout == False:

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
                # if max depth reached, restart
                if turn_counter > max_depth:
                        turn_counter = 0
                        board1 = Board(board_file)
                        board1.create()
                        board1.fill()

                # if max time reached, time out
                if time.time() - game_time > max_game_time:
                    print("timeout")
                    df = pd.DataFrame(turn_counter_list)
                    df.to_csv(f"results_{game + 1}.csv", index = False)
                    timeout = True


            # if last game didnt time out, save log
            if timeout == False:
                print(f"{turn_counter} turns played")
                print(f"{round(time.time() - game_time, 2)} seconds played")
                turn_counter_list.append({'turns': turn_counter, 'time': round(time.time() - game_time, 2), 'total_time': round(time.time() - total_time, 2)})
                max_depth = turn_counter
                board1.save_logbook(filename = f"logbook_{game + 1}_{turn_counter}_turns.csv")

        # save the results
        df = pd.DataFrame(turn_counter_list)
        df.to_csv(f"results_{game + 1}.csv", index = False)
