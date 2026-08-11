import os
from pathlib import Path
from dotenv import load_dotenv
from neo4j import GraphDatabase

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

print("Loading .env from:", ENV_FILE)

load_dotenv(ENV_FILE)

uri = os.getenv("COGNODB_URI")
user = os.getenv("COGNODB_USER")
password = os.getenv("COGNODB_PASSWORD")

print("URI:", uri)
print("User:", user)
print("Password loaded:", bool(password))

if not uri or not user or not password:
    raise ValueError("CognoDB credentials are missing from .env")

driver = GraphDatabase.driver(
    uri,
    auth=(user, password)
)

try:
    driver.verify_connectivity()
    print("Connection successful!")

except Exception as e:
    print("Connection failed:")
    print(e)

finally:
    driver.close()