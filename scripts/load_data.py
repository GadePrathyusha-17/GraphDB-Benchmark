from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import csv

load_dotenv()

uri = os.getenv("COGNODB_URI")
user = os.getenv("COGNODB_USER")
password = os.getenv("COGNODB_PASSWORD")

db = GraphDatabase.driver(uri, auth=(user, password))

with db.session() as session:

    file = open("data/movies.csv", "r", encoding="utf-8")

    reader = csv.DictReader(file)

    for row in reader:

        session.run(
            """
            CREATE (m:Movie {
                movie_id:$movie_id,
                title:$title,
                genre:$genre,
                release_year:$release_year,
                rating:$rating,
                director:$director,
                lead_actor:$lead_actor,
                language:$language
            })
            """,
            movie_id=int(row["movie_id"]),
            title=row["title"],
            genre=row["genre"],
            release_year=int(row["release_year"]),
            rating=float(row["rating"]),
            director=row["director"],
            lead_actor=row["lead_actor"],
            language=row["language"]
        )

file.close()

print("Movie data loaded successfully.")

db.close()