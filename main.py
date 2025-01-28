from code.classes.board_class import Board
from code.algorithms.baseline import random_algorithm
from code.functions.game_visualizer import replay_game
from code.algorithms.BreadthFirst import breadth_first_search
from code.algorithms.DepthFirst import DepthFirst, depth_first_search
from code.algorithms.random_algorithm_heuristics import random_algorithm_heuristics

import pandas as pd
import subprocess
import time

# comes with lists 'all_turns_game_[1-7]' of baseline results
from code.functions.data_analysis import *

if __name__ == "__main__":
    
    # Give small welcome and ask what board to play
    print("Welcome to Rush Hour!\nWhat game would you like to play?\n 1. board 1 (6x6)\n 2. board 2 (6x6)\n 3. board 3 (6x6)\n 4. board 4 (9x9)\n 5. board 5 (9x9)\n 6. board 6 (9x9)\n 7. board 7 (12x12)\n")
    board_input = input("Please choose a number: \n")
    
    while board_input not in "1234567":
        print("Invalid board choice.")
        board_input = input("Please choose a number: \n")
        
    if board_input == "1":
        board_file = "Rushhour6x6_1.csv"
    elif board_input == "2":
        board_file = "Rushhour6x6_2.csv"
    elif board_input == "3":
        board_file = "Rushhour6x6_3.csv"
    elif board_input == "4":
        board_file = "Rushhour9x9_4.csv"
    elif board_input == "5":
        board_file = "Rushhour9x9_5.csv"
    elif board_input == "6":
        board_file = "Rushhour9x9_6.csv"
    elif board_input == "7":
        board_file = "Rushhour12x12_7.csv"

    # Ask user how many times to simulate the game    
    n_times_input = input("How many times would you like to play? \n")
    
    while not n_times_input.isdigit():
        print("Invalid choice. Please choose a number.")
        n_times_input = input("How many times would you like to play? \n")
    
    n_times_input = int(n_times_input)
    
    # As user for a time limit
    print("Would you like to add a time limit?\n 1. No time limit\n 2. Only time limit per game\n 3. Only overall time limit\n 4. Both overall time limit and time limit per game\n")
    time_limit_input = input("Please choose a number:\n")
    game_time_limit_ind = False
    overall_time_limit_ind = False
    
    while time_limit_input not in "1234":
        print("Invalid choice.")
        time_limit_input = input("Please choose a number:\n")
    
    if time_limit_input == '1':
        pass
    elif time_limit_input == '2':
        game_time_limit = input("Time limit in seconds:\n")
        while not game_time_limit.isdigit():
            print("Please choose a valid int.")
            game_time_limit = input("Time limit in seconds:\n")
        
        game_time_limit = float(game_time_limit)
        game_time_limit_ind = True       
    elif time_limit_input == '3':
        overall_time_limit = input("Time limit in seconds: \n")
        while not overall_time_limit.isdigit():
            print("Please choose a valid int.")
            overall_time_limit = input("Time limit in seconds:\n")
        
        overall_time_limit = float(overall_time_limit)
        overall_time_limit_ind = True
    elif time_limit_input == '4':
        game_time_limit = input("Time limit per game in seconds:\n")
        while not game_time_limit.isdigit():
            print("Please choose a valid int.")
            game_time_limit = input("Time limit per game in seconds:\n")
            
        overall_time_limit = input("Overall time limit in seconds: \n")
        while not overall_time_limit.isdigit():
            print("Please choose a valid int.")
            overall_time_limit = input("Overall time limit in seconds:\n")
        
        game_time_limit = int(game_time_limit)
        overall_time_limit = int(overall_time_limit)
        game_time_limit_ind = True
        overall_time_limit_ind = True
    
    # Ask user which algorthm to use
    print("Choose an algorithm to solve the board:\n 1. Random search\n 2. Breadth first search\n 3. Depth first search\n 4. Random Algorithm with Heuristics (Note: Has a default time limit)")
    algorithm_input = input("Please choose a number:\n")

    if algorithm_input == "1":
        random_algorithm(board_file, 1)
    elif algorithm_input == "2":

        if game_time_limit_ind and overall_time_limit_ind:
            result = breadth_first_search(board_file, n_times_input, game_time_limit, overall_time_limit)
        elif game_time_limit_ind and not overall_time_limit_ind:
            result = breadth_first_search(board_file, n_times_input, max_time_game = game_time_limit)
        elif not game_time_limit_ind and overall_time_limit_ind:
            result = breadth_first_search(board_file, n_times_input, max_time_overall = overall_time_limit)
        else:
            result = breadth_first_search(board_file, n_times_input)

        # Save results to CSV after all runs
        df = pd.DataFrame(result)
        df.to_csv('bfs_results.csv', index=False)
        print("Results saved to bfs_results.csv")
    
    elif algorithm_input == "3":
        
        if game_time_limit_ind and overall_time_limit_ind:
            result = depth_first_search(board_file, n_times_input, game_time_limit, overall_time_limit)
        elif game_time_limit_ind and not overall_time_limit_ind:
            result = depth_first_search(board_file, n_times_input, max_time_game = game_time_limit)
        elif not game_time_limit_ind and overall_time_limit_ind:
            result = depth_first_search(board_file, n_times_input, max_time_overall = overall_time_limit)
        else:
            result = depth_first_search(board_file, n_times_input)

        # Save results to CSV after all runs
        df = pd.DataFrame(result)
        df.to_csv('dfs_results.csv', index=False)
        print("Results saved to dfs_results.csv")

    elif algorithm_input == "4":

        if game_time_limit_ind and overall_time_limit_ind:
            result = random_algorithm_heuristics(board_file, 50000, n_times_input, overall_time_limit, game_time_limit)
        elif game_time_limit_ind and not overall_time_limit_ind:
            result = random_algorithm_heuristics(board_file, 50000, n_times_input, max_game_time = game_time_limit)
        elif not game_time_limit_ind and overall_time_limit_ind:
            result = random_algorithm_heuristics(board_file, 50000, n_times_input, max_run_time = overall_time_limit)
        else:
            result = random_algorithm_heuristics(board_file, 50000, n_times_input)
        
    else: 
        print("Invalid choice. Please choose a number.")


