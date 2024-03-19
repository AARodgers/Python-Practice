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


