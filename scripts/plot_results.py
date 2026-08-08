import pandas as pd
import matplotlib.pyplot as plt

# Read benchmark results
file = "results/cognodb_complete_results.csv"
df = pd.read_csv(file)

# Create performance graph
plt.figure(figsize=(10, 6))

plt.bar(df["Query"], df["Execution Time (seconds)"])

plt.xlabel("Query")
plt.ylabel("Execution Time (seconds)")
plt.title("CognoDB Query Performance")

plt.xticks(rotation=30, ha="right")
plt.tight_layout()

# Save graph
plt.savefig("results/cognodb_performance.png", dpi=300)

print("Performance graph created successfully.")
print("Saved to: results/cognodb_performance.png")