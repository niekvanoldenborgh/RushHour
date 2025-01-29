import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


### BOXPLOT RESULTS DIFFERENT ALGORITHMS (6x6) ###

# Load data for 6x6 and 9x9 boards
results_1 = pd.read_csv("results\\depth_first_search\\dfs_results_6x6_1.csv")
results_2 = pd.read_csv("results\\breadth_first_search\\bfs_results_bord1.csv")
results_3 = pd.read_csv("results\\random_algorithm_heuristics\\6x6_1\\6x6_1_merged.csv")

# Keep only the necessary two columns
results_1 = results_1.iloc[:100, :2]
results_2 = results_2.iloc[:100, :2]
results_3 = results_3.iloc[:, [0,2]]

# Create quality variable according to our quality function
results_1['quality'] = results_1.iloc[:, 0] + results_1.iloc[:, 1]
results_2['quality'] = results_2.iloc[:, 0] + results_2.iloc[:, 1]
results_3['quality'] = results_3.iloc[:, 0] + results_3.iloc[:, 1]

# The random heuristic algorithm has different result format, adjust accordingly
results_3_list = []

for i in range(results_3.shape[0] -1):
    current_turns = results_3.iloc[i, 0]
    next_turns = results_3.iloc[i+1, 0]
    if next_turns > current_turns:
        results_3_list.append(results_3.iloc[i, :].to_list())

# Convert filtered results_3_list and results_6_list to a DataFrame
results_3 = pd.DataFrame(results_3_list, columns=results_3.columns[:])

# Calculate BFS average quality value
bfs_avg = results_2['quality'].mean()

# Filter results for each algorithm
results_1['algorithm'] = 'DFS'
results_2['algorithm'] = 'BFS'
results_3['algorithm'] = 'RH'

# Combine the data for the boxplot (excluding BFS from the boxplot data)
combined_results = pd.concat([results_1[['quality', 'algorithm']], 
                              results_3[['quality', 'algorithm']]])

# Create the boxplot (excluding BFS data)
plt.figure(figsize=(10, 6))
sns.boxplot(x='algorithm', y='quality', data=combined_results, palette="Set2", width = 0.5)

# Add a horizontal line for the BFS average quality value
plt.axhline(y=bfs_avg, color='r', linestyle='--', label=f'BFS 6x6')

# Add title and labels
plt.title('Performance per Algorithm')
plt.xlabel('Algorithm')
plt.ylabel('Quality (Moves + Time)')

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()


