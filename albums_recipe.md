# Single Table Design Recipe Template

_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organise my records,
I want to keep a list of albums' release years.
```

```
Nouns:

album, title, release year
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| album                 | title, release year |

Name of the table (always plural): `albums`

Column names: `title`, `release_year`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
title: text
release_year: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
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

# Submit message route
POST /albums
  title: string 
  release_year: int
  artist_id: int
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# POST /albums
#  Parameters:
#    title: Voyage
#    release_year: 2022
#    artist_id: 2
#  Expected response (200 OK):

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

"""
POST /albums
  Parameters:
    title: Voyage
    release_year: 2022
    artist_id: 2
  Expected response (200 OK):
"""
def test_post_albums(web_client, db_connection):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': 2022, 'artist_id': 2})
    assert response.status_code == 200
    response = web_client.get('/albums', methods=['GET'])
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ""\
        "Album(1, 'Spirit Mission', 2022, 1)\n" \
        "Album(2, 'Voyage', 2022, 2)"
    
```

