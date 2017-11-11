from bs4 import BeautifulSoup
from urllib.request import urlopen

html1 = urlopen("https://www.theguardian.com/books/series/100-best-nonfiction-books-of-all-time?page=1")
html2 = urlopen("https://www.theguardian.com/books/series/100-best-nonfiction-books-of-all-time?page=2")


url = "http://www.arizona.edu/colleges"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
universities = soup.findAll('span', {'class': 'field-content'})
for eachuniversity in universities:
   print(eachuniversity)

