"""
In this Bite we are going to parse a csv movie dataset to identify the
 directors with the highest rated movies.

Write get_movies_by_director: use csv.DictReader to convert 
movie_metadata.csv into a (default)dict of lists of Movie namedtuples. 

Convert/filter the data: 

Only extract director_name, movie_title, title_year and imdb_score.

Type conversions: title_year -> int / imdb_score -> float

Discard any movies older than 1960.

Here is an extract:

....
{ 'Woody Allen': [
    Movie(title='Midnight in Paris', year=2011, score=7.7),
    Movie(title='The Curse of the Jade Scorpion', year=2001, score=6.8),
    Movie(title='To Rome with Love', year=2012, score=6.3),  ....
    ], ...
}

Write the calc_mean_score helper that takes a list of Movie namedtuples 
and calculates the mean IMDb score, returning the score rounded to 1 
decimal place.

Complete get_average_scores which takes the directors data structure 
returned by get_movies_by_director (see 1.) and returns a list of tuples 
(director, average_score) ordered by highest score in descending order. 
Only take directors into account with >= MIN_MOVIES

See the tests for more info. This could be tough one, but we really hope 
you learn a thing or two. Good luck and keep calm and code in Python!
"""

import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from statistics import mean
from tempfile import gettempdir

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = gettempdir()

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = defaultdict(list)
    with open(MOVIE_DATA) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            
            except ValueError:
                continue
            if year and year < MIN_YEAR:
                continue

            m = Movie(title = movie, year = year, score = score)
            directors[director].append(m)

    return directors


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return float("{:.1f}".format(mean([movie.score for movie in movies])))


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    director_avg = [(director, calc_mean_score(movies)) 
                    for director, movies in directors.items() 
                    if len(movies) >= MIN_MOVIES]
    return sorted(director_avg, key= lambda tup: tup[1], reverse=True)
