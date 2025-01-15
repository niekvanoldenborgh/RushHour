from code.classes.board_class import Board
import random
import time

"""
So I want to create an algorithm that randomly selects cars (tiles?).
When car is selected, check for movement options and if there are options available,
select one at random.
"""

board1 = Board("Rushhour6x6_1_simplified.csv")
board1.create()
board1.fill()
board1.show()

# print(f"{board1.car_names}")

# heres the foundation of the random algorithm
# theres a lot wrong with it still
# it doesnt check for victory and most turns try to do invalid moves
# but it can serve as a baseline for the baseline I suppose

turn_counter = 0
while board1.is_won() == False:

    # select random car based on the length of list of car names
    selected_car = board1.cars.get(board1.car_names[random.randint(0, len(board1.car_names) - 1)])
    # print(f"selected car = {selected_car.name}")
    car_moved = False
    # keep trying until a car moves
    while car_moved == False:

        # if only one direction is available, move in that direction
        if board1.is_valid(selected_car, 1) == True and board1.is_valid(selected_car, -1) == False:
            board1.move(selected_car, 1)
            car_moved = True
            # print("Moved forwards")

        elif board1.is_valid(selected_car, 1) == False and board1.is_valid(selected_car, -1) == True:
            board1.move(selected_car, -1)
            car_moved = True
            # print("Moved backwards")

        # if both directions are available, move in random direction
        elif board1.is_valid(selected_car, 1) == True and board1.is_valid(selected_car, -1) == True:
            board1.move(selected_car, random.choice([-1,1]))
            car_moved = True
            # print("Random move")

        # if neither direction is available, select a different car
        elif board1.is_valid(selected_car, 1) == False and board1.is_valid(selected_car, -1) == False:
            selected_car = board1.cars.get(board1.car_names[random.randint(0, len(board1.car_names) - 1)])
            # print("No valid moves")
            # print(f"New car is {selected_car.name}")

        print(board1.is_won())


    # relay info on event
    board1.show()
    turn_counter += 1

    # time delay makes it visible in terminal
    # for mass testing, probably best to comment/remove
    # time.sleep(0.005)

# board1.show()
print(turn_counter)



