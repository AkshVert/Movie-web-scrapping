#Importing libraries and modules
import requests
from bs4 import BeautifulSoup
import datetime
import pytz

# Set the timezone to Indian Standard Time (IST)
IST = pytz.timezone('Asia/Kolkata')

# Get the current date and time in IST
now = datetime.datetime.now(IST)
date_time = now.strftime("%d-%m-%Y %H:%M:%S")

url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

top_movies_table = soup.find('tbody', class_='lister-list')

movie_titles = []
movie_ratings = []
movie_years = []

for movie_row in top_movies_table.find_all('tr')[:10]:
    title_column = movie_row.find('td', class_='titleColumn')
    rating_column = movie_row.find('td', class_='ratingColumn')
    movie_title = title_column.a.text.strip()
    movie_rating = rating_column.strong.text.strip()
    movie_year = title_column.span.text.strip('()')
    movie_titles.append(movie_title)
    movie_ratings.append(movie_rating)
    movie_years.append(movie_year)

with open('top_10_indian_movies.txt', 'w') as f:
    f.write(f'IMDb Top 10 Indian Movies ({date_time} IST):\n\n')
    for i in range(10):
        f.write(f'{i+1}. {movie_titles[i]} ({movie_years[i]}) - {movie_ratings[i]}\n')
