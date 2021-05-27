import movie
from requests import get
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/'

# just get the top 50 for now (it appears on the page that opens up first)

# html class tags:
#     title: <a href="/title/stuff"> title of movie
#     year: <span class="lister-item-year text-muted unbold">(2021)</span>
#     rating: <div class="inline-block ratings-imdb-rating" name="ir" data-value="5.9">
#         <span class="global-sprite rating-star imdb-rating"></span>
#         <strong>5.9</strong>
#         </div>
#     description: <p class="text-muted">description here</p>

# genre = input("Type a movie genre \n")
# minRating, maxRating = input("Enter a range of ratings (separated by a dash) \n").split('-')
# minYear, maxYear = input("Enter a year range (separated by a dash)  \n").split('-')

response = get(url)

# obj = movie.movie("movie name", 1990, 5.0, "This is what the movie is about")
# obj.print_info()
