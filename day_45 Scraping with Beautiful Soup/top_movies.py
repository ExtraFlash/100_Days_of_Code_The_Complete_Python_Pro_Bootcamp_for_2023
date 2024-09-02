from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
PARSER = 'html.parser'

# get html data
response = requests.get(URL)
website_html = response.text

# create soup instance
soup = BeautifulSoup(website_html, PARSER)

# get titles
movie_tags = soup.find_all(name="h3", class_="title")
titles = [movie_tag.getText() for movie_tag in movie_tags]
titles = titles[::-1]

# save titles to file
with open("titles.txt", mode='w', encoding='utf-8') as file:
    for title in titles:
        file.write(f'{title}\n')
