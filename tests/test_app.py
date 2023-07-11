from lib.album import Album

# Tests for your routes go here
"""
When I call GET /albums
Expected response (200 OK) and 
I get a list of albums back
"""
def test_get_albums(web_client, db_connection):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ""\
        "Album(1, Spirit Mission, 2022, 1)"


"""
When I call POST /albums
With parameters:
    title: Voyage
    release_year: 2022
    artist_id: 2
Expected response (200 OK):
"""
def test_post_albums(web_client, db_connection):
    db_connection.seed('seeds/record_store.sql')
    post_response = web_client.post('/albums', data={'title': 'Voyage', 'release_year':'2022', 'artist_id': '2'})
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == ""\
        "Album(1, Spirit Mission, 2022, 1)\n" \
        "Album(2, Voyage, 2022, 2)"

"""
When I call GET /albums
Expected response (200 OK):
Pixies, ABBA, Taylor Swift, Nina Simone
"""
def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/record_store.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
When I call POST /albums
with parameters name: Wild nothing and genre: Indie
Expected response (200 OK):
(no content)
subsequent call to GET /albums expected response (200 OK):
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""
def test_post_artists(web_client, db_connection):
    db_connection.seed('seeds/record_store.sql')
    post_response = web_client.post('/artists', data={'name': 'Wild nothing', 'genre': 'Indie'})
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"