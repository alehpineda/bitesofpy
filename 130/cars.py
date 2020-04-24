from collections import Counter

import requests

CAR_DATA = "https://bit.ly/2Ov65SJ"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    count = Counter(
        [car.get("automaker") for car in data if car.get("year") == year]
    )
    return count.most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return {
        car.get("model")
        for car in data
        if car.get("automaker") == automaker and car.get("year") == year
    }


# Pybites solution:
def most_prolific_automaker1(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    cnt = Counter(
        row["automaker"] for row in data if row["year"] == year
    ).most_common()
    return cnt[0][0]


def get_models1(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return set(
        [
            row["model"]
            for row in data
            if row["automaker"] == automaker and row["year"] == year
        ]
    )
