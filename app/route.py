from app import app
from app.model import *
from flask import Flask, render_template, request

data = pd.read_csv('./app/data_girl_group.csv')


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html')     

@app.route('/recommend', methods=['POST'])
def recommend():
    input_song_name = request.form['song_name']
    numb_of_rec = int(request.form['number-of-recs'])
    song_recommendations =  result(data, input_song_name, numb_of_rec)

    song = []
    for i in range(numb_of_rec):
        song.append([str(song_recommendations['Artists'].iloc[i]) + ' - '+ '"'+str(song_recommendations['Track Name'].iloc[i])+'"', "https://open.spotify.com/track/"+ str(song_recommendations['Track ID'].iloc[i])])

    return render_template('result.html', songs=song)