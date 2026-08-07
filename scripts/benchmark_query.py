from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import time

# Read database details from .env
load_dotenv()

database_url = os.getenv("COGNODB_URI")
username = os.getenv("COGNODB_USER")
password = os.getenv("COGNODB_PASSWORD")

# Connect to the database
graph = GraphDatabase.driver(
    database_url,
    auth=(username, password)
)

query = """
MATCH (m:Movie)
WHERE m.language = 'Telugu'
RETURN m.title, m.rating
"""

start = time.time()

session = graph.session()

records = session.run(query)

print("\nTelugu Movies\n")

for record in records:
    print(record["m.title"], "-", record["m.rating"])

session.close()

end = time.time()

total_time = end - start

print("\nTime Taken:", round(total_time, 4), "seconds")

with open("results/benchmark_results.txt", "w") as file:
    file.write("Benchmark Report\n")
    file.write("----------------------\n")
    file.write("Query : Telugu Movies\n")
    file.write("Execution Time : " + str(round(total_time, 4)) + " seconds\n")

print("Benchmark report saved successfully.")

graph.close()