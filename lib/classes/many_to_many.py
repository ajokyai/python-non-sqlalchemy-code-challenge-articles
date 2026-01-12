# lib/classes/many_to_many.py

class Article:
    all = []

    def __init__(self, author, magazine, title):
        from lib.author import Author
        from lib.magazine import Magazine

        # Validations
        if not isinstance(author, Author):
            raise Exception("author must be an Author")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("title must be a string between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self._title = title  # make title immutable

        Article.all.append(self)

    # Immutable title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass  # ignore changes
