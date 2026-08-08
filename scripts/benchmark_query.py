from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import time
import csv

# Read database details from .env
load_dotenv()

database_url = os.getenv("COGNODB_URI")
username = os.getenv("COGNODB_USER")
password = os.getenv("COGNODB_PASSWORD")

# Connect to CognoDB
graph = GraphDatabase.driver(
    database_url,
    auth=(username, password)
)

query = """
MATCH (m:Movie)
WHERE m.language = 'Telugu'
RETURN m.title, m.rating
"""

# Create results directory
os.makedirs("results", exist_ok=True)

print("\nRunning Telugu Movies Benchmark...\n")

start = time.time()

session = graph.session()

records = session.run(query)

results = list(records)

end = time.time()

session.close()

total_time = end - start

# Display results
print("Telugu Movies\n")

for record in results:
    print(record["m.title"], "-", record["m.rating"])

print("\nNumber of movies:", len(results))
print("Time Taken:", round(total_time, 4), "seconds")

# Save CSV result
csv_file = "results/cognodb_benchmark_results.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Database",
        "Query",
        "Result Count",
        "Execution Time (seconds)"
    ])

    writer.writerow([
        "CognoDB",
        "Telugu Movies",
        len(results),
        round(total_time, 4)
    ])

# Save text report
txt_file = "results/benchmark_results.txt"

with open(txt_file, "w", encoding="utf-8") as file:
    file.write("CognoDB Benchmark Report\n")
    file.write("========================\n")
    file.write("Query: Telugu Movies\n")
    file.write("Result Count: " + str(len(results)) + "\n")
    file.write(
        "Execution Time: "
        + str(round(total_time, 4))
        + " seconds\n"
    )

print("\nBenchmark results saved successfully.")
print("CSV:", csv_file)
print("Report:", txt_file)

graph.close()