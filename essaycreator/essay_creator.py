import wikipedia
import bs4 as bs
import requests
import time
from PyDictionary import PyDictionary

#print(wikipedia.search('Gay Bishops', results=5))
def page_links(search):
    suggestions = wikipedia.search(search, results=5)

    new_urls = []

    for topic in suggestions:
        #print(str(topic))
        new_urls.append((str(topic)).replace(' ', '_'))
    return new_urls

for index, articles in enumerate(page_links('Gay Priestsw')):
    print(wikipedia.WikipediaPage(articles).summary)
    print()
    print()

#print(new_urls)



#print(page.content)
#
# dictionary = PyDictionary()
#
# resp = requests.get('https://en.wikipedia.org/wiki/Gay_bishops')
# soup = bs.BeautifulSoup(resp.text, 'lxml')
#
# info = soup.find('div', { "id" : "mw-content-text" })
# print(info.find('a'))
#print(soup.find())

# for other_thing in soup.find_all('div', {'class': 'TableHeader'}):
#     print(other_thing.text)

#print(dictionary.synonym('angry'))
#print (wikipedia.summary('Wikipedia'))