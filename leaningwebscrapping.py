#Following tutorial: https://www.youtube.com/watch?v=XVv6mJpFOb0 
from bs4 import BeautifulSoup 

with open('DNT.html', 'r') as html_file:
        content = html_file.read()

        soup = BeautifulSoup(content, 'lxml')
        print(soup.prettify())
        tags = soup.find('title')
        print(tags)
