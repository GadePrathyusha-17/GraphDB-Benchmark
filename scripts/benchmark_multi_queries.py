from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import time

load_dotenv()

uri = os.getenv("COGNODB_URI")
user = os.getenv("COGNODB_USER")
password = os.getenv("COGNODB_PASSWORD")

graph = GraphDatabase.driver(uri, auth=(user, password))

queries = [
    ("All Movies", "MATCH (m:Movie) RETURN m"),
    ("Telugu Movies", "MATCH (m:Movie) WHERE m.language='Telugu' RETURN m"),
    ("Rating Above 8", "MATCH (m:Movie) WHERE m.rating > 8 RETURN m"),
    ("Released After 2020", "MATCH (m:Movie) WHERE m.release_year > 2020 RETURN m"),
    ("Count Movies", "MATCH (m:Movie) RETURN count(m)")
]

session = graph.session()

result = open("results/complete_benchmark_results.txt", "w")

result.write("Benchmark Results\n")
result.write("=========================\n\n")

for name, query in queries:

    start = time.time()

    session.run(query).consume()

    end = time.time()

    total = end - start

    print(name, ":", round(total, 4), "seconds")

    result.write(name + " : " + str(round(total, 4)) + " seconds\n")

result.close()

session.close()

graph.close()

print("\nBenchmark completed successfully.")