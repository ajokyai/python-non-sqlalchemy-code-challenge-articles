from lib.classes.author import Author
from lib.classes.magazine import Magazine
from lib.classes.article import Article

def run_debug_tests():
    print("=== Creating Authors ===")
    a1 = Author("Alice")
    a2 = Author("Bob")
    print(a1.name, a2.name)

    print("\n=== Creating Magazines ===")
    m1 = Magazine("TechToday", "Tech")
    m2 = Magazine("HealthWeekly", "Health")
    print(m1.name, m1.category)
    print(m2.name, m2.category)

    print("\n=== Adding Articles ===")
    art1 = a1.add_article(m1, "Python Tips and Tricks")
    art2 = a1.add_article(m2, "Healthy Eating for Beginners")
    art3 = a2.add_article(m1, "AI in 2026")
    art4 = a2.add_article(m1, "Quantum Computing Explained")
    art5 = a2.add_article(m1, "Advanced Python Patterns")

    print("All Articles:")
    for article in Article.all:
        print(f"- {article.title} by {article.author.name} in {article.magazine.name}")

    print("\n=== Author Methods ===")
    print(f"{a1.name} Articles:", [a.title for a in a1.articles()])
    print(f"{a1.name} Magazines:", [m.name for m in a1.magazines()])
    print(f"{a1.name} Topic Areas:", a1.topic_areas())

    print(f"{a2.name} Articles:", [a.title for a in a2.articles()])
    print(f"{a2.name} Magazines:", [m.name for m in a2.magazines()])
    print(f"{a2.name} Topic Areas:", a2.topic_areas())

    print("\n=== Magazine Methods ===")
    print(f"{m1.name} Articles:", [a.title for a in m1.articles()])
    print(f"{m1.name} Contributors:", [c.name for c in m1.contributors()])
    print(f"{m1.name} Article Titles:", m1.article_titles())
    contributing = m1.contributing_authors()
    if contributing:
        print(f"{m1.name} Authors with >2 articles:", [c.name for c in contributing])
    else:
        print(f"{m1.name} Authors with >2 articles: None")

    print("\n=== Top Publisher ===")
    top = Magazine.top_publisher()
    if top:
        print("Top Publisher:", top.name)
    else:
        print("Top Publisher: None")

if __name__ == "__main__":
    run_debug_tests()
