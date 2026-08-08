import csv
import os

raw_folder = "data/raw"
output_folder = "data/processed"

os.makedirs(output_folder, exist_ok=True)

# Create users.csv
with open(os.path.join(raw_folder, "u.user"), "r", encoding="latin-1") as file:
    users = []

    for line in file:
        parts = line.strip().split("|")

        if len(parts) >= 5:
            users.append([
                parts[0],
                parts[1],
                parts[2],
                parts[3],
                parts[4]
            ])

with open(os.path.join(output_folder, "users.csv"), "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["user_id", "age", "gender", "occupation", "zip_code"])
    writer.writerows(users)


# Create movies.csv
with open(os.path.join(raw_folder, "u.item"), "r", encoding="latin-1") as file:
    movies = []

    for line in file:
        parts = line.strip().split("|")

        if len(parts) >= 2:
            movies.append([
                parts[0],
                parts[1]
            ])

with open(os.path.join(output_folder, "movies.csv"), "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["movie_id", "title"])
    writer.writerows(movies)


# Create ratings.csv
with open(os.path.join(raw_folder, "u.data"), "r", encoding="latin-1") as file:
    ratings = []

    for line in file:
        parts = line.strip().split("\t")

        if len(parts) == 4:
            ratings.append(parts)

with open(os.path.join(output_folder, "ratings.csv"), "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["user_id", "movie_id", "rating", "timestamp"])
    writer.writerows(ratings)


print("Dataset preparation completed.")
print("Users:", len(users))
print("Movies:", len(movies))
print("Ratings:", len(ratings))