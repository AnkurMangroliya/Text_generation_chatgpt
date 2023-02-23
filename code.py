movies = {
    'Avatar':{
        "director":"James Cameron",
        "year": 2009,
        "revenue": 2787965087
    },
    "Titanic": {
        "director": "James Cameron",
        "year": 1997,
        "revenue": 2208208395
    },
    "The Lion King": {
        "director": "Roger Allers and Rob Minkoff",
        "year": 1994,
        "revenue": 968483777
    }
}

import time
def generate_description(movie):
    director = movie['director']
    year = movie['year']
    revenue = movie['revenue']
    revenue_text = "earned over ${:,.2f} at the box office worldwide".format(revenue / 1000000)
    Description = 'The movie {} was directed by {} and released in {}. It {}. '.format(movie_name,director,year,revenue_text)
    return Description

for movie_name,movie_data in movies.items():
    description = generate_description(movie_data)
    def print_char_by_char(text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
           
    print_char_by_char(description)
