import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Load in results
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


# Show the plot
plt.show()
