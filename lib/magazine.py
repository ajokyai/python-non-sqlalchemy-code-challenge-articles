# lib/magazine.py

class Magazine:
    all = []

    def __init__(self, name, category):
        # Validate name
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("name must be a string between 2 and 16 characters")
        self._name = name

        # Validate category
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("category must be a non-empty string")
        self._category = category

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        from lib.classes.many_to_many import Article
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        contributors = {article.author for article in self.articles()}
        return list(contributors) if contributors else None

    def article_titles(self):
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    def contributing_authors(self):
        articles = self.articles()
        if not articles:
            return None
        from lib.author import Author
        author_counts = {}
        for article in articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        from lib.classes.many_to_many import Article
        max_articles = 0
        top_magazine = None
        for mag in cls.all:
            count = len([a for a in Article.all if a.magazine == mag])
            if count > max_articles:
                max_articles = count
                top_magazine = mag
        return top_magazine
