import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd
import numpy as np

cars_df = pd.read_csv("Rushhour6x6_1.csv")

# add a 'colour' property per car
# painting squares allows one to just have lists of coordinates
# otherwise i suppose we could just make rectangles

# nxn = 6x6
n = 6

car_colour_list = []
car_orientation_list = []
car_col_list = []
car_row_list = []
car_length_list = []

# read this from the classes.py dict
for index in range(0, 13):

    if cars_df['car'][index] != 'X':
        car_colour_list.append([np.random.uniform(low=0, high=0.75), np.random.uniform(low=0.1, high=1), np.random.uniform(low=0.1, high=1)])
    else:
        car_colour_list.append([1,0,0])

    car_orientation_list.append(cars_df['orientation'][index])
    car_col_list.append(cars_df['col'][index])
    car_row_list.append(cars_df['row'][index])
    car_length_list.append(cars_df['length'][index])

board, axes = plt.subplots()

# WHY DONT THE RECTANGLES DRAW OVER THE GRIDLINES
# okay making the linewidth *real* small makes it barely noticable heheheheh
axes.grid(linewidth=0.1)

# probably a good idea to merge this into the classes.py internally
def place_car(car_col, car_row, car_length, car_orient, car_colour = 'red'):
    # some magic numbers to account for the graph starting bottom left, but dataframes starting from top left
    # also to account for the rectangles originating in the bottom left of the entered coordinate
    if car_orient == 'H':
        axes.add_patch(Rectangle((car_col, -car_row - 1), car_length, 1, facecolor = car_colour))
    else:
        axes.add_patch(Rectangle((car_col, -car_row - 2), 1, car_length, facecolor = car_colour))

for index in range(0, len(car_col_list)):
    place_car(car_col_list[index], car_row_list[index], car_length_list[index], car_orientation_list[index], car_colour_list[index])

plt.xlim(1, 7)
plt.ylim(-7, -1)
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('Rush Hour Board')
