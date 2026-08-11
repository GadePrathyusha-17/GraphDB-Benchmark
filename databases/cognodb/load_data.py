import csv
import os
import time

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

COGNODB_URI = os.getenv("bolt+s://db-18a2d233.databases.cognodb.com:7687")
COGNODB_USER = os.getenv("cognodb")
COGNODB_PASSWORD = os.getenv("905e7381d0f91c57f41c6e085d87725a")

driver = GraphDatabase.driver(
    COGNODB_URI,
    auth=(COGNODB_USER, COGNODB_PASSWORD)
)


def load_users(session):
    users = []

    with open("data/processed/users.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print(reader.fieldnames)

        for row in reader:
            users.append({
                "user_id": row["user_id"],
                "occupation": row["occupation"],
                "age": row["age"],
                "gender": row["gender"],
                "zip_code": row["zip_code"]
            })

            if len(users) == 500:
                session.run(
                    """
                    UNWIND $users AS user
                    CREATE (:User {
                        user_id: user.user_id,
                        occupation: user.occupation,
                        age: user.age,
                        gender: user.gender,
                        zip_code: user.zip_code
                    })
                    """,
                    users=users
                )

                users = []

        if users:
            session.run(
                """
                UNWIND $users AS user
                CREATE (:User {
                    user_id: user.user_id,
                    name: user.name,
                    age: user.age,
                    gender: user.gender,
                    zip_code: user.zip_code
                })
                """,
                users=users
            )


def load_movies(session):
    movies = []

    with open("data/processed/movies.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            movies.append({
                "title": row["title"]
            })

            if len(movies) == 500:
                session.run(
                    """
                    UNWIND $movies AS movie
                    CREATE (:Movie {title: movie.title})
                    """,
                    movies=movies
                )

                movies = []

    if movies:
        session.run(
            """
            UNWIND $movies AS movie
            CREATE (:Movie {title: movie.title})
            """,
            movies=movies
        )


def load_ratings(session):
    ratings = []

    with open("data/processed/ratings.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print(reader.fieldnames)

        for row in reader:
            ratings.append({
                "user_id": row["user_id"],
                "movie_id": row["movie_id"],
                "rating": float(row["rating"]),
                "timestamp": int(row["timestamp"])
            })

            if len(ratings) == 500:
                session.run(
                    """
                    UNWIND $ratings AS r

                    MATCH (u:User {user_id: r.user_id})
                    MATCH (m:Movie {movie_id: r.movie_id})

                    CREATE (u)-[:RATED {
                        rating: r.rating,
                        timestamp: r.timestamp
                    }]->(m)
                    """,
                    ratings=ratings
                )

                ratings = []

        if ratings:
            session.run(
                """
                UNWIND $ratings AS r

                MATCH (u:User {user_id: r.user_id})
                MATCH (m:Movie {movie_id: r.movie_id})

                CREATE (u)-[:RATED {
                    rating: r.rating,
                    timestamp: r.timestamp
                }]->(m)
                """,
                ratings=ratings
            )

start = time.perf_counter()

try:
    with driver.session() as session:
        print("Loading users...")
        load_users(session)

        print("Loading movies...")
        load_movies(session)

        print("Loading ratings...")
        load_ratings(session)

    total_time = time.perf_counter() - start

    print("\nData loading completed.")
    print("Total loading time:", round(total_time, 4), "seconds")

finally:
    driver.close()