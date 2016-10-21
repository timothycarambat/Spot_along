#This file on execution will read current song playing on Spotify
# and attempt to find the lyrics for you automatically
# opening your default browser. Tested on windows 10 with
# Python 2.7

import spotilib as spot
from search import google_scrape
import webbrowser

#get song from info on taskbar
info = spot.song_info()

#form query for genius.com refrence
q = 'Genius ' + info + ' lyrics'
terms = ['genius.com' , 'lyrics']


#search google for song
links = google_scrape(q)

for link in links[:5]:  #get top 5 results
    link.encode('utf-8')
    if all(terms for term in link):
        print(link)
        search = link
        break # Get top result after filtering
    
if search != 'http://genius.com/':    
    webbrowser.open_new_tab(search)


