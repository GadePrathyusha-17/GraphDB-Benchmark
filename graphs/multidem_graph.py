import matplotlib.pyplot as plt

names = []
times = []

with open("results/complete_benchmark_results.txt", "r") as file:

    for line in file:
        if ":" in line and "Benchmark" not in line and "=" not in line:
            parts = line.strip().split(" : ")

            if len(parts) == 2:
                names.append(parts[0])
                times.append(float(parts[1].replace(" seconds", "")))


plt.bar(names, times)

plt.title("Graph Database Query Performance")
plt.xlabel("Queries")
plt.ylabel("Execution Time (seconds)")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("graphs/benchmark_graph.png")

print("Graph created successfully.")