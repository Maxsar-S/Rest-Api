class User:
    def __init__(self, name, birthday_year):
        self.name = name
        self.birthday_year = birthday_year

    def __str__(self):
        return self.name


class Biography:
    def __init__(self, text, user):
        self.user = user
        self.text = text


class Post:
    def __init__(self, name, author):
        self.name = name
        self.authors = author


class Article:
    def __init__(self, name, authors):
        self.name = name
        self.author = authors
