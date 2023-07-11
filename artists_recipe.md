# Single Table Design Recipe Template

_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
1. Test-drive a route GET /artists, which returns the list of artists:
# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone


2. Test-drive a route POST /artists, which creates a new artist in the database. Your test should verify the new artist is returned in the response of GET /artists.
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
```

```
Nouns: artist, name, genre


```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| artist                | name, genre        |

Name of the table (always plural): `artists`

Column names: `name`, `genre`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
name: text
genre: text
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```

# {{ albums }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Get artists route
GET /artists

# Create artists route
POST /artists
  name: string 
  genre: string

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# GET /artists
  #Expected response (200 OK):
  #Pixies, ABBA, Taylor Swift, Nina Simone

# POST /artists
#  Parameters:
#    name: Wild nothing
#    genre: Indie

#  Expected response (200 OK):
#   (no content)
#  subsequent GET /artists expected response (200 OK):
#   Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

"""
# GET /artists
  #Expected response (200 OK):
  #Pixies, ABBA, Taylor Swift, Nina Simone
"""
def test_get_artists(web_client, db_connection):
  db_connection.seed('seeds/record_store.sql)
  response = web_client.get('/artists')
  assert response.status_code == 200
  assert response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
POST /artists
#  Parameters:
#    name: Wild nothing
#    genre: Indie

#  Expected response (200 OK):
#   (no content)
#  subsequent GET /artists expected response (200 OK):
#   Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""
def test_post_artists(web_client, db_connection):
    db_connection.seed('seeds/record_store.sql')
    post_response = web_client.post('/artists', data={'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ""

    get_response = web_client.get('/artists', methods=['GET'])
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"
    
```

