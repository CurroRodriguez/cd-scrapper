import newspaper

cd_url = "http://civilizeddevelopment.typepad.com"

cd_paper = newspaper.build(cd_url, memoize_articles=False)
cd_articles = [article for article in cd_paper.articles if article.url.startswith(cd_url)]
for article in sorted(cd_articles, key=lambda a: a.url):
    print(article.url)

print('Found {c} articles'.format(c=len(cd_articles)))