from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load values from .env
load_dotenv()

uri = os.getenv("COGNODB_URI")
user = os.getenv("COGNODB_USER")
password = os.getenv("COGNODB_PASSWORD")

db = GraphDatabase.driver(uri, auth=(user, password))

with db.session() as session:

    # Query 1
    print("\n----- Telugu Movies -----")

    result = session.run("""
        MATCH (m:Movie)
        WHERE m.language = 'Telugu'
        RETURN m.title
    """)

    for movie in result:
        print(movie["m.title"])


    # Query 2
    print("\n----- Movies with Rating Above 8 -----")

    result = session.run("""
        MATCH (m:Movie)
        WHERE m.rating > 8
        RETURN m.title, m.rating
    """)

    for movie in result:
        print(movie["m.title"], "-", movie["m.rating"])


    # Query 3
    print("\n----- Movies Released After 2020 -----")

    result = session.run("""
        MATCH (m:Movie)
        WHERE m.release_year > 2020
        RETURN m.title, m.release_year
    """)

    for movie in result:
        print(movie["m.title"], "-", movie["m.release_year"])


    # Query 4
    print("\n----- Total Movies -----")

    result = session.run("""
        MATCH (m:Movie)
        RETURN count(m) AS total
    """)

    print("Total Movies:", result.single()["total"])

db.close()