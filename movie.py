class movie:
    name = 0
    year = 0
    rating = 0
    description = 0

    def __init__(self, name, year, rating, description):
        self.name = name
        self.year = year
        self.rating = rating
        self.description = description

    def print_info(self):
        print("Name: ", str(self.name), "\n", "Year: ", str(self.year), "\n", "Rating: ", str(self.rating), "\n", "Description: ", str(self.description))
