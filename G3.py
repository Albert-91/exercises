"""
CREATE TABLE Show(
    id serial,
    movie_id int not null,
    cinema_id int not null,
    PRIMARY KEY (id),
    FOREIGN KEY (movie_id)
    REFERENCES movies(id),
    FOREIGN KEY(cinema_id)
    REFERENCES cinemas(id)
);
"""
from flask import Flask

#pg_dump -U postgres -h localhost -W -d cinemas_db > backup.sql

from flask import Flask, request
from psycopg2 import connect, OperationalError

app = Flask("Płatnik")


def create_connection(db_name="cinema_db"):
    username = "postgres"
    password = "coderslab"
    host = "localhost"

    try:
        connection = connect(user=username, password=password, host=host, dbname=db_name)
        return connection
    except OperationalError:
        return None


@app.route('/', methods=['POST', 'GET'])
def movies():
    forms = """
    <form class="payment_form" method="post" action="#">
        <label>Film</label><br>
        <select name="movie_id">
            {}
        </select><br>
        <label>Kino</label><br>
        <select name="cinema_id">
            {}
        </select><br>
        <button type="submit" name="submit" value="payment">Wyślij</button>
    </form>
    """
    if request.method == 'GET':
        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT id, name FROM movies")
        option_movie = ""
        for movie in cursor:
            option_movie += "<option value='{}'>{}</option>".format(movie[0], movie[1])
        option_cinema = ""
        cursor.execute("SELECT id, name FROM cinemas")
        for cinema in cursor:
            option_cinema += "<option value='{}'>{}</option>".format(cinema[0], cinema[1])
        return forms.format(option_movie, option_cinema)
    else:
        cnx = create_connection()
        cursor = cnx.cursor()
        cinema_id = request.form['cinema_id']
        movie_id = request.form['movie_id']
        cursor.execute("""
            insert INTO show (cinema_id, movie_id)
            VALUES ({},{})
        """.format(cinema_id, movie_id))
        cnx.commit()
        cursor.close()
        cnx.close()
        return "Udało się"

"""
SELECT * FROM cinemas
JOIN show ON cinemas.id = show.cinema_id
WHERE show.movie_id = 1;
"""


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    cnx = create_connection()
    cursor = cnx.cursor()
    statement = """
        SELECT * FROM cinemas
        JOIN show ON cinemas.id = show.cinema_id
        WHERE show.movie_id = %s;    
    """
    cursor.execute(statement, (movie_id,))
    cinema_string = ''
    for cinema in cursor:
        cinema_string += '{} {}<br>'.format(cinema[0], cinema[1])
    return cinema_string


if __name__ == '__main__':
    app.run(debug=True)