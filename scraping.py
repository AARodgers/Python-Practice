# Website to use:
#http://books.toscrape.com/

# using library beautiful soup to parse html in python

# in Jupyter lab, first cell
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
html = response.content
scraped = BeautifulSoup(html, 'html.parser')

scraped.title
#returns
# <title>
#     All products | Books to Scrape - Sandbox
# </title>

# same as above
scraped.find("title")

scraped.title.text
# '\n    All products | Books to Scrape - Sandbox\n'

scraped.title.text.strip()
#'All products | Books to Scrape - Sandbox'

# put extracted data to a variable
title_text = scraped.title.text.strip()
title_text
# Gives you same output as above"

linked_text = scraped.article.h3.a.text
linked_text
#'A Light in the ...'

# can use the attribute 'title' to get the full text
linked_text = scraped.article.h3.a["title"]
linked_text
#'A Light in the Attic'

#using find_all
# find all objects with selector article and class product_pod
items = scraped.find_all("article", class_="product_pod")

# get the contents of the title attribute to the a selector
for item in items:
    print(item.h3.a["title"])
# will give you a list of all of the book titles

#will do the same as above, it an element has a unique trait
title_links = scraped.find_all("a", title=True)

for link in title_links:
    print(link["title"])

# find all links that are descendants of h3 and article
scraped.select("article h3 a")

#find all linds, h3, and articles, 
