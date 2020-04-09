from bs4 import BeautifulSoup, SoupStrainer
import requests

url = "https://td.klprojects.tech/[Judas]%20Fairy%20Tail%20(2009-2014)%20(Seasons%201-8%20+%20OVAs)%20[BD%201080p][HEVC%20x265%2010bit][Dual-Audio][Eng-Subs]/"

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
