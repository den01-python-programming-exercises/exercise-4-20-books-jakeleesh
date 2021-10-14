class Book:
    def __init__(self, title, pages, year):
        self.title = title
        self.pages = pages
        self.year = year

    def get_title(self):
        return self.title

    def __str__(self):
        return str(self.title) + ", " + str(self.pages) + " pages, " + str(self.year)