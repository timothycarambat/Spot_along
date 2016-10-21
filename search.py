import urllib2, urllib
from bs4 import BeautifulSoup

def google_scrape(query):
    address = "http://www.google.com/search?q=%s&num=100&hl=en&start=0" % (urllib.quote_plus(query))
    request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urllib2.urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page, "html.parser")

    links = []

    for li in soup.findAll('h3', attrs={'class':'r'})[:10]: #get first 10 results
        sLink = li.find('a')
        links.append(sLink['href'])
        
    return links

