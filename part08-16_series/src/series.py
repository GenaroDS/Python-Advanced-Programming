# Write your solution here:
import string


class Series:

    def __init__(self, title: string, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
    
    def __str__(self):
        genero = ", ".join(self.genres)
        if not self.ratings:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genero}\nno ratings"
        else:
            amount = len(self.ratings)
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genero}\n{amount} ratings, average {sum(self.ratings)/(amount):.1f} points"
    def rate(self, rating: int):        
        self.ratings.append(rating)

    def average(self):
        if self.ratings:
            return f"{sum(self.ratings)/(len(self.ratings)):.1f}"
        else:
            pass
def minimum_grade(grade:float , series: list):
    goodEnough = []
    for serie in series:
        if float(serie.average()) >= float(grade):
            goodEnough.append(serie)
    return goodEnough

def includes_genre(genre: str, series: list):
    closeEnough = []
    for serie in series:
        if genre in serie.genres:
            closeEnough.append(serie)
    return closeEnough
