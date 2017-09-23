import bs4
import newspaper
import encodings.utf_16


def main():
    url ="http://civilizeddevelopment.typepad.com/civilized-development/2013/08/dragging-labels-in-2014.html"
    article = CDArticle(url)
    print("Title: " + article.title)
    print("Author: " + article.author)
    print("Categories: " + ", ".join(article.categories))
    #print("Content", article.content)
    article.content




class CDArticle(object):
    """
    """
    def __init__(self, article_url):
        self._url = article_url
        self._config = newspaper.Config()
        self._config.memoize_articles = False
        self._config.keep_article_html = True
        self._np_article = newspaper.Article(self._url, self._config)
        self._np_article.download()
        self._np_article.parse()
        self._soup = bs4.BeautifulSoup(self._np_article.html, 'html.parser')
        self._content_soup = self._soup.find('div', class_='entry-body')



    @property
    def title(self):
        return self._np_article.title


    @property
    def author(self):
        return "Isaac Rodriguez"


    @property
    def categories(self):
        footer = self._soup.find('span', class_="post-footers")
        return [category.contents[0] for category in footer.contents if category.name == 'a']


    @property
    def content(self):
        print(self._content_soup.prettify(formatter='html'))











if __name__=="__main__":
    main()