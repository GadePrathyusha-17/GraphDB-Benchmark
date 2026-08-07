from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Read values from .env file
load_dotenv()

uri = os.getenv("COGNODB_URI")
user = os.getenv("COGNODB_USER")
password = os.getenv("COGNODB_PASSWORD")

db = GraphDatabase.driver(uri, auth=(user, password))

query = """
MATCH (m:Movie)
RETURN m.movie_id AS ID,
       m.title AS Title,
       m.genre AS Genre,
       m.release_year AS Year,
       m.rating AS Rating,
       m.director AS Director,
       m.lead_actor AS Actor,
       m.language AS Language
"""

with db.session() as s:

    result = s.run(query)

    print("\nMovie Details\n")

    for movie in result:
        print(movie)

db.close()