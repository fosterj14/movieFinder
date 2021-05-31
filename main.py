from selenium import webdriver
from selenium.webdriver.support.select import Select

import movie

url = 'https://www.imdb.com/search/title/'
driver = webdriver.Chrome("E:\python_work\chromedriver_win32\chromedriver.exe")
driver.get(url)

# genre = input("Type a movie genre \n")
# minRating, maxRating = input("Enter a range of ratings (separated by a dash) \n").split('-')
# minYear, maxYear = input("Enter a year range (separated by a dash)  \n").split('-')
# number = input("How many movies would you like to pull? (50, 100, or 250) \n")

genre = "horror"
minRating, maxRating = 1, 4
minYear, maxYear = 1980, 1994
number = "250"

min_date_input = driver.find_element_by_name("release_date-min")
max_date_input = driver.find_element_by_name("release_date-max")
min_rating_input = driver.find_element_by_name("user_rating-min")
max_rating_input = driver.find_element_by_name("user_rating-max")
genre_table = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/form/div/div[6]/div[2]")

# input info into sections
min_date_input.send_keys(minYear)
max_date_input.send_keys(maxYear)
min_rating_input.send_keys(minRating)
max_rating_input.send_keys(maxRating)
driver.find_element_by_xpath(
    "//label[text()='" + genre.capitalize() + "']").click()  # finds the element that has the label text matching the genre

dropdown = Select(driver.find_element_by_id("search-count"))
dropdown.select_by_value(number)

search_button = driver.find_element_by_class_name("primary")
search_button.click()

# get the info of each movie on the page

movies = []
# this prints out 250 copies of the first movie, not different movies
i = 1
for film in driver.find_elements_by_class_name("lister-item-content"):
    title = driver.find_element_by_xpath(
        "//*[@id='main']/div/div[3]/div/div[%s]/div[3]/h3/a" %i).text
    date = driver.find_element_by_class_name("lister-item-year").text
    rating = driver.find_element_by_xpath(
        "//*[@id='main']/div/div[3]/div/div[%s]/div[3]/div/div[1]/strong" %i).text
    description = driver.find_element_by_xpath('.//*[@id="main"]/div/div[3]/div/div[%s]/div[3]/p[2]' % i).text #%s is used
    # to subsitute the div number for the correct movie
    temp = movie.movie(title, date, rating, description)
    movies.append(temp)
    i = i + 1

for film in movies:
    film.print_info()
print(len(movies))

# obj = movie.movie("movie name", 1990, 5.0, "This is what the movie is about")
# obj.print_info()
