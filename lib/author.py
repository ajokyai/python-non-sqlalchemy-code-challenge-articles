# lib/author.py

class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("name must be a non-empty string")
        self._name = name  # make name immutable
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass  # ignore changes

    def articles(self):
        from lib.classes.many_to_many import Article
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        from lib.classes.many_to_many import Article
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        areas = {mag.category for mag in self.magazines() if hasattr(mag, 'category')}
        return list(areas) if areas else None
