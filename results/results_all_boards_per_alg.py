import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

### BOXPLOT RESULTS DIFFERENT ALGORITHMS (6x6 and)###

# Load data for 6x6 and 9x9 boards
results_1 = pd.read_csv("results\\depth_first_search\\dfs_results_6x6_1.csv")
results_2 = pd.read_csv("results\\breadth_first_search\\bfs_results_bord1.csv")
results_3 = pd.read_csv("results\\random_algorithm_heuristics\\6x6_1\\6x6_1_merged.csv")

results_4 = pd.read_csv("results\\depth_first_search\\dfs_results-9x9_4.csv")
results_5 = pd.read_csv("results\\breadth_first_search\\bfs_results4.csv")
results_6 = pd.read_csv("results\\random_algorithm_heuristics\\9x9_4\\9x9_4_merged.csv")

results_7 = pd.read_csv("results\\random_algorithm_heuristics\\12x12_7\\12x12_7_merged.csv")

# Keep only the necessary two columns
results_1 = results_1.iloc[:100, :2]
results_2 = results_2.iloc[:100, :2]
results_3 = results_3.iloc[:, [0,2]]

results_4 = results_4.iloc[:100, :2]
results_5 = results_5.iloc[:100, :2]
results_6 = results_6.iloc[:, [0,2]]

results_7 = results_7.iloc[:, [0,2]]

# Create quality variable according to our quality function
results_1['quality'] = results_1.iloc[:, 0] + results_1.iloc[:, 1]
results_2['quality'] = results_2.iloc[:, 0] + results_2.iloc[:, 1]
results_3['quality'] = results_3.iloc[:, 0] + results_3.iloc[:, 1]

results_4['quality'] = results_4.iloc[:, 0] + results_4.iloc[:, 1]
results_5['quality'] = results_5.iloc[:, 0] + results_5.iloc[:, 1]
results_6['quality'] = results_6.iloc[:, 0] + results_6.iloc[:, 1]

results_7['quality'] = results_7.iloc[:, 0] + results_7.iloc[:, 1]

# the random heuristic algorithm has different result format, adjust
results_3_list = []
results_6_list = []
results_7_list = []

for i in range(results_3.shape[0] -1):
    current_turns = results_3.iloc[i, 0]
    next_turns = results_3.iloc[i+1, 0]
    if next_turns > current_turns:
        results_3_list.append(results_3.iloc[i, :].to_list())

for i in range(results_6.shape[0] -1):
    current_turns = results_6.iloc[i, 0]
    next_turns = results_6.iloc[i+1, 0]
    if next_turns > current_turns:
        results_6_list.append(results_6.iloc[i, :].to_list())

for i in range(results_7.shape[0] -1):
    current_turns = results_7.iloc[i, 0]
    next_turns = results_7.iloc[i+1, 0]
    if next_turns > current_turns:
        results_7_list.append(results_7.iloc[i, :].to_list())

# Convert filtered results_3_list and results_6_list to a DataFrame
results_3 = pd.DataFrame(results_3_list, columns=results_3.columns[:])
results_6 = pd.DataFrame(results_6_list, columns=results_6.columns[:])
results_7 = pd.DataFrame(results_7_list, columns=results_7.columns[:])

# Add an identifier column for grouping
results_1['Algorithm'] = 'DFS (6x6)'
results_3['Algorithm'] = 'RH (6x6)'
results_4['Algorithm'] = 'DFS (9x9)'
results_6['Algorithm'] = 'RH (9x9)'
results_7['Algorithm'] = 'RH (12x12)'

# Merge all results into one DataFrame excluding BFS results
all_results = pd.concat([results_1, results_3, results_4, results_6, results_7])

# Create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x="Algorithm", y="quality", data=all_results, width=0.4, palette="Set2")

# Calculate BFS average lines (but don't plot BFS in boxplot)
bfs_6x6_avg = results_2['quality'].mean()
bfs_9x9_avg = results_5['quality'].mean()

# Add BFS average as horizontal reference lines
plt.axhline(bfs_6x6_avg, color="red", linestyle="dashed", label="BFS 6x6")
plt.axhline(bfs_9x9_avg, color="darkred", linestyle="dashed", label="BFS 9x9")

# Labels, title and legend
plt.xlabel("Algorithm")
plt.ylabel("Quality (Moves + Time)")
plt.title('Performance per Algorithm')
plt.legend()

# Save and show
plt.savefig("visuals\\results_all_boards_per_alg.png", dpi=300)
plt.show()