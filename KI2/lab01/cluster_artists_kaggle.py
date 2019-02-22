"""
Cluster artists based on the words in their lyrics
Data from kaggle
Format data with create_data_kaggle.py
"""

__author__ = 'don.tuggener@zhaw.ch'

import numpy
import json
import pdb
import re
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import pyplot as plt

def plot_dendrogram(clustered, artists):
    """ Plot a dendrogram from the hierarchical clustering of the artist lyrics """
    #plt.figure(figsize=(25, 10))   # for orientation = 'bottom'|'top'
    plt.figure(figsize=(10, 25))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Distance')  # this' but the label of the whole axis!
    plt.ylabel('Artists')
    plt.tight_layout()
    dendrogram(clustered,
        #leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
        labels = artists,
        orientation = 'left',
    )
    #plt.show() # Instead pf saving
    plt.savefig('example_dendrogram.svg', bbox_inches='tight')  

def words_per_artist(artist_lyrics, lyrics_tfidf_matrix, ix2word, n=10):
    """ 
    For each artist, print the most highly weighted words acc. to TF IDF 
    Print n words that are above the mean weight 
    """
    # TODO implement it

if __name__ == '__main__':
    
    print('Loading data')
    artist2genre = json.load(open('data/artist2genre_kaggle.json', 'r', encoding='utf-8'))
    artist_lyrics = json.load(open('data/artist_lyrics_kaggle.json', 'r', encoding='utf-8'))
    # Custom tokenization to remove numbers etc.
    lyrics = [' '.join(re.findall('[A-Za-z]+', l)) for l in artist_lyrics.values()]
    
    print('Vectorizing with TF IDF')
    # Vectorize the song lyrics
    # TODO implement; create lyrics_tfidf_matrix (artist/word matrix) and ix2word (dict that maps word IDs to words)
    
    print('Distinct words per artist')
    words_per_artist(artist_lyrics, lyrics_tfidf_matrix, ix2word)

    print('Clustering')
    # TODO call SciPy's hierarchical clustering 

    print('Plotting')
    artist_names = [a+': '+artist2genre[a].upper() for a in list(artist_lyrics.keys())]
    plot_dendrogram(clustered, artist_names)
