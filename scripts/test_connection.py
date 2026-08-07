from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# Load the values from the .env file
load_dotenv()

# Read database details
db_uri = os.getenv("COGNODB_URI")
db_user = os.getenv("COGNODB_USER")
db_password = os.getenv("COGNODB_PASSWORD")

# Create a connection to the database
db_connection = GraphDatabase.driver(
    db_uri,
    auth=(db_user, db_password)
)

# Open a session and execute a query
with db_connection.session() as session:
    query = "RETURN 'Connected Successfully!' AS message"
    result = session.run(query)

    for record in result:
        print(record["message"])

# Close the connection
db_connection.close()