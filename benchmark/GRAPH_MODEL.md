# Graph Model

## Nodes

### User

Properties:
- user_id
- age
- gender
- occupation
- zip_code

### Movie

Properties:
- movie_id
- title

## Relationship

### RATED

Direction:

User -> Movie

Properties:
- rating
- timestamp

## Graph Structure

(User)-[:RATED]->(Movie)