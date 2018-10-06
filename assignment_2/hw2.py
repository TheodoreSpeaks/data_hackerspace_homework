import requests
import re
import matplotlib.pyplot as plt
import json
import numpy as np


def lyrics_word_count_easy(artist, song, phrase):
    r = requests.get('https://api.lyrics.ovh/v1/' + artist + '/' + song)
    if r.status_code == 200:
        return r.json()['lyrics'].upper().count(phrase.upper())
    return -1

def lyrics_word_count(artist, phrase):
    params = {
        'api_key': api_keys['music-graph-key'],
        'name': artist
    }
    r = requests.get('https://api.musicgraph.com/api/v2/artist/', params=params) 
    return r.json()

def visualize():
    x = np.array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9.,10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29.])
    y = np.array([ 0., 25., 27., 4., -22., -28., -8., 19., 29., 12., -16., -29., -16., 12., 29., 19., -8., -28., -22., 4., 27., 25., -0., -25., -27., -3., 22., 28., 8., -19.])
    fig = plt.figure()


    #Line graph
    ax1 = fig.add_subplot(2,1,1)
    ax1.plot(x, y) 
    ax1.set_title("LineGraph")

    #Histogram
    ax2 = fig.add_subplot(2,2,3)
    ax2.hist((x,y))
    ax2.set_title("Histogram")

    # Scatter
    ax3 = fig.add_subplot(2,2,4)
    ax3.set_title("Scatter")
    plt.scatter(x,y)

    return plt.show()
    

with open('api_keys.json') as f:
    api_keys = json.loads(f.read())
print(visualize())
#print(lyrics_word_count('Rick Astley', "never gonna give you up"))
#print(lyrics_word_count_easy('rick astley', 'never gonna give you up', 'never'))
