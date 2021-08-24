import requests
from bs4 import BeautifulSoup

r = requests.get('https://venmurasu.in/mutharkanal/chapter-1')

# print(r.text[0:800]) 

soup        =    BeautifulSoup(r.text , 'html.parser')

results     =    soup.find_all('p')

print(len(results))