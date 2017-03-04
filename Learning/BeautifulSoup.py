from bs4 import BeautifulSoup

soup = BeautifulSoup(open('a.html'))
# print(soup.prettify())
print(soup.title)
print(soup.head)
print(soup.a)
print(soup.p).