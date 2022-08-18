from bs4 import BeautifulSoup
import requests

movies_page = requests.get(
    url='https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/').text
soup = BeautifulSoup(movies_page, 'html.parser')

movies = soup.find_all(name='h3', class_='title')
movies_names = [movie.getText() for movie in movies]

with open('movies.txt', 'w') as fp:
    for movie in movies_names[::-1]:
        fp.write("%s\n" % movie)
