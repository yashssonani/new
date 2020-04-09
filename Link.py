from BeautifulSoup4 import BeautifulSoup
import urllib2
import re

html_page = urllib2.urlopen("https://td.klprojects.tech/[Judas]%20Fairy%20Tail%20(2009-2014)%20(Seasons%201-8%20+%20OVAs)%20[BD%201080p][HEVC%20x265%2010bit][Dual-Audio][Eng-Subs]/")
soup = BeautifulSoup(html_page)
links = []

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))

print(links)
