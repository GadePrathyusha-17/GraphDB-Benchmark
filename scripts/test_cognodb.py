import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

uri = os.getenv("COGNODB_URI")
user = os.getenv("COGNODB_USER")
password = os.getenv("COGNODB_PASSWORD")

print("URI:", uri)
print("User:", user)

connection = GraphDatabase.driver(
    uri,
    auth=(user, password)
)

try:
    connection.verify_connectivity()
    print("CognoDB connection is working.")

except Exception as error:
    print("Connection failed.")
    print(error)

finally:
    connection.close()