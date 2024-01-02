import pandas as pd
import numpy as np
import re

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

def get_features(data):
    scaler = MinMaxScaler()
    music_features = data[['Danceability', 'Energy', 'Key', 
                           'Loudness', 'Mode', 'Speechiness', 'Acousticness',
                           'Instrumentalness', 'Liveness', 'Valence', 'Tempo']]
    music_features_scaled = scaler.fit_transform(music_features)
                           
    return music_features_scaled


def content_based_recommendations(data, song_name, vs_song, num_recommendations):
 
    scaled_features = get_features(data)
    
    # Get the index of the input song in the music DataFrame
    song_index = data[data['Track Name'] == song_name].index[0]

    # Calculate the similarity scores based on music features (cosine similarity)
    similarity_scores = cosine_similarity([scaled_features[song_index]], scaled_features)

    # Get the indices of the most similar songs
    similar_song_indices = similarity_scores.argsort()[0][::-1][len(vs_song):num_recommendations + len(vs_song)]
   
    # Get the names of the most similar songs based on content-based filtering
    content_based_recommendations = data.iloc[similar_song_indices]
    
    return content_based_recommendations

def result(data, input_song_name, num_recommendations):
    pattern = re.compile(fr'\b{input_song_name}\b', re.IGNORECASE)
    song = []
    
    for i in data['Track Name']:
        match = pattern.search(i)   
        if match:
            index = data[data['Track Name'] == i].index[0]
            song.append(data['Track Name'][index])  
    recommend = content_based_recommendations(data, song[0], song, num_recommendations)
    
    return recommend