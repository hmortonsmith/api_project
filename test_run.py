from flask import Flask, request, json, make_response
from connection import *


app = Flask(__name__)


@app.route('/home')
def home():
    return 'home.html'


@app.route("/create_movie", methods=['POST'])
def create():
    connect = SQLTool()
    movie = request.data
    movie_dict = json.loads(movie)
    connect.query(f"INSERT INTO IMDB_Movies VALUES ('{movie_dict['VideoType']}', '{movie_dict['PrimaryTitle']}', '{movie_dict['OriginalTitle']}', {movie_dict['IsAdult']}, {movie_dict['StartYear']}, {movie_dict['EndYear']}, {movie_dict['RunTime']}, '{movie_dict['Genres']}');")
    connect.conn.commit()
    return 'Finished'


if __name__ == '__main__':
    app.run()



