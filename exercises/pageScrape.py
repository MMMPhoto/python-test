import bs4, requests

def getAboutText(pageUrl):
    res = requests.get(pageUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#searchHeader')
    return elems[0].text

text = getAboutText('https://mmmphoto.github.io/Event-Finder/')
print(f'The text of the search header is: "{text}"')