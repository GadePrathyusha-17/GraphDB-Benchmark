import matplotlib.pyplot as plt

query_name = ["Telugu Movies"]
execution_time = [ 1.6209]  # Replace with your measured time

plt.bar(query_name, execution_time)

plt.title("Query Execution Time")
plt.xlabel("Query")
plt.ylabel("Time (seconds)")

plt.savefig("graphs/query_time.png")

plt.show()

print("Graph saved successfully.")