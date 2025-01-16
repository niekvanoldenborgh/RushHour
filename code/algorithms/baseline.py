from code.classes.board_class import Board
import random
import time

def random_algorithm(board_file, runs):
    board1 = Board(board_file)
    board1.create()
    board1.fill()
    # board1.show()
    print("start")

    turn_counter = 0
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



        # relay info on event
        turn_counter += 1
        # print(turn_counter)

        # time delay makes it visible in terminal
        # time.sleep(0.005)
    print(turn_counter)
    board1.show()
    board1.save_logbook(filename = f"logbook{runs}.csv")
    print("stop")
    return turn_counter


"""
first run: 14900~
second run: 49000~
third run: terminated at like 100.000 runs
fourth run: 1583
fifth run: 7327
sixth run: 19303

53390
297702
154696
20539
206907
26772
28789
234601
"""

