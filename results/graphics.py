import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns


### COMBINED FREQ GRAPH OF THREE BOARD TYPES ###

def read_results(filepath):
    with open(filepath, "r") as f:
        return eval(f.read())

results_1 = read_results("results\\random_search\\6x6_1\\turns_per_game.txt")
results_2 = read_results("results\\random_search\\9x9_4\\turns_per_game.txt")
results_3 = read_results("results\\random_search\\12x12_7\\turns_per_game.txt")

# Plot histograms
plt.figure(figsize=(10, 6))
plt.hist(results_1, bins=30, alpha=0.5, color='green', label="6x6_1")
plt.hist(results_2, bins=30, alpha=0.5, color='blue', label="9x9_4")
plt.hist(results_3, bins=30, alpha=0.5, color='red', label="12x12_7")

# Format x-axis numbers with dots
def format_func(value, _):
    return f"{int(value):,}".replace(",", ".")

plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(format_func))

# Labels and legend
plt.xlabel("Moves to Solve")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Moves to Solve")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Save the plot
plt.savefig("visuals\\results_random_turns.png", dpi=300)

# Show the plot
plt.show()



### INTERPRET RESULTS DIFFERENT ALGORITHMS ###

results_4 = pd.read_csv("results\\depth_first_search\\dfs_results_6x6_1.csv")
results_5 = pd.read_csv("results\\breadth_first_search\\bfs_results_bord1.csv")
results_6 = pd.read_csv("results\\random_algorithm_heuristics\\6x6_1\\6x6_1_merged.csv")

results_4 = results_4.iloc[:100, :2]
results_5 = results_5.iloc[:100, :2]
results_6 = results_6.iloc[:, :2]

results_4['quality'] = results_4.iloc[:, 0] + results_4.iloc[:, 1]
results_5['quality'] = results_5.iloc[:, 0] + results_5.iloc[:, 1]
results_6['quality'] = results_6.iloc[:, 0] + results_6.iloc[:, 1]

results_6_list = []

for i in range(results_6.shape[0] -1):
    current_turns = results_6.iloc[i, 0]
    next_turns = results_6.iloc[i+1, 0]
    if next_turns > current_turns:
        results_6_list.append(results_6.iloc[i, :3].to_list())

# Convert filtered results_6_list to a DataFrame
results_6 = pd.DataFrame(results_6_list, columns=results_6.columns[:3])

# Calculate BFS average quality value
bfs_avg = results_5['quality'].mean()

# Filter results for each algorithm
results_4['algorithm'] = 'DFS'
results_5['algorithm'] = 'BFS'
results_6['algorithm'] = 'Random Heuristic'

# Combine the data for the boxplot (excluding BFS from the boxplot data)
combined_results = pd.concat([results_4[['quality', 'algorithm']], 
                              results_6[['quality', 'algorithm']]])

# Create the boxplot (excluding BFS data)
plt.figure(figsize=(10, 6))
sns.boxplot(x='algorithm', y='quality', data=combined_results, palette="Set2", width = 0.5)

# Add a horizontal line for the BFS average quality value
plt.axhline(y=bfs_avg, color='r', linestyle='--', label=f'BFS Avg = {bfs_avg:.2f}')

# Add title and labels
plt.title('Comparison of Quality Across Different Algorithms')
plt.xlabel('Algorithm')
plt.ylabel('Quality (Sum of Moves + Time)')

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.savefig("visuals\\results_6x6_per_alg.png", dpi=300)