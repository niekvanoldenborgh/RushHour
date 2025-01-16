from code.classes.board_class import Board
from code.algorithms.baseline import random_algorithm

if __name__ == "__main__":
    result_list = []
    for x in range(0, 20):
        result = random_algorithm("Rushhour6x6_3.csv", x)
        result_list.append(result)
        result = 0
    print(result_list)

