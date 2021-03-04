

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, Response
from werkzeug.utils import secure_filename
from db import db_init, db
from models import Img
from paintings import painting_list
#create a Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///img.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

#connects default URL of server to a python function
@app.route('/')
@app.route('/home')
def home():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")

@app.route('/cubism')
def cubism():
    return render_template("cubism.html")

@app.route('/photography')
def photography():
    posts = [{'title': 'Photography', 'author': 'Francis Lim', 'summary': 'Iconic Photos in History', 'period': '5 Longhorns'}]
    return render_template("photography.html", posts=posts)

@app.route('/quotesapi')
def quotesapi():
    return render_template("quotesapi.html")

@app.route('/Movies')
def Movies():
    return render_template("Movies.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/music')
def Music():
    return render_template('Music.html', genremain="")

@app.route('/musicclassical')
def MusicClassical():
    return render_template('MusicClassical.html', genremain='')

@app.route('/musicjazz')
def MusicJazz():
    return render_template('MusicJazz.html')

@app.route("/Genresearch1", methods=["GET", "POST"])
def genresearch():
    if request.method == "POST":
        form = request.form
        Genre1 = form['MusicG1']

        if Genre1.strip() == "Classical" or Genre1.strip() == "classical" or Genre1.strip() == "Classical Music" or Genre1.strip() == "classical music":
            return render_template('/Music/MusicClassical.html', genremain='Classical Music:')
        elif Genre1.strip() == 'Jazz' or Genre1.strip() == 'jazz' or Genre1.strip() == 'Jazz Music' or Genre1.strip() == 'jazz music':
            return render_template('/Music/MusicJazz.html', genremain='Jazz Music:')
        elif Genre1.strip() == "EasterEgg" or Genre1.strip() == "easteregg" or Genre1.strip() == "Easteregg":
            return render_template('EasterEgg.html', genremain="EasterEgg!")
        elif Genre1.strip() == "Rock" or Genre1.strip() == 'rock' or Genre1.strip() == 'rock music' or Genre1.strip() == 'Rock Music':
            return render_template('/Music/MusicRock.html', genremain="Rock Music:")
        elif Genre1.strip() == 'Pop' or Genre1.strip() == 'pop' or Genre1.strip() =='Pop Music' or Genre1.strip() == 'pop music':
            return render_template('/Music/MusicPop.html', genremain='Pop Music:')
        elif Genre1.strip() == 'Hip Hop' or Genre1.strip() == 'hip hop' or Genre1.strip() == 'Hip hop' or Genre1.strip() == 'HipHop' or Genre1.strip() == 'hiphop':
            return render_template('/Music/MusicHiphop.html', genremain='Hip Hop Music:')
        elif Genre1.strip() == 'Punk' or Genre1.strip() == 'punk' or Genre1.strip() == 'Punk Rock' or Genre1.strip() == 'punk rock' or Genre1.strip() == 'Punk rock':
            return render_template('/Music/MusicPunk.html', genremain='Punk Music:')
        elif Genre1.strip() == 'Disco' or Genre1.strip() == 'disco' or Genre1.strip() == 'Disco Music' or Genre1.strip() == 'disco music':
            return render_template('/Music/MusicDisco.html', genremain='Disco Music:')
        elif Genre1.strip() == 'Folk' or Genre1.strip() == 'folk' or Genre1.strip() == 'Folk Music' or Genre1.strip() == 'folk music' or Genre1.strip() == 'Folk music' or Genre1.strip() == 'folk Music':
            return render_template('/Music/MusicFolk.html', genremain='Folk Music: ')
        elif Genre1.strip() == 'Soul' or Genre1.strip() == 'soul' or Genre1.strip() == 'Soul Music' or Genre1.strip() == 'soul music' or Genre1.strip() == 'Soul music' or Genre1.strip() == 'soul Music':
            return render_template('/Music/MusicSoul.html', genremain='Soul Music:')
        elif Genre1.strip() == 'Blues' or Genre1.strip() == 'blues' or Genre1.strip() == 'Blues Music' or Genre1.strip() == 'blues music':
            return render_template('/Music/MusicBlues.html', genremain='Blues Music: ')
        elif Genre1.strip() == 'Reggae' or Genre1.strip() == 'reggae' or Genre1.strip() == 'Reggae Music' or Genre1.strip() == 'reggae music':
            return render_template('/Music/MusicReggae.html', genremain='Reggae Music: ')
        elif Genre1.strip() == 'Funk' or Genre1.strip() == 'funk' or Genre1.strip() == 'Funk Music' or Genre1.strip() == 'funk music':
            return render_template('/Music/MusicFunk.html', genremain='Funk Music:')
        elif Genre1.strip() == 'Country' or Genre1.strip() == 'country' or Genre1.strip() == 'Country Music' or Genre1.strip() == 'country music':
            return render_template('/Music/MusicCountry.html', genremain='Country Music:')
        elif Genre1.strip() == 'Techno' or Genre1.strip() == 'techno' or Genre1.strip() == 'tech' or Genre1.strip() == 'Tech' or Genre1.strip() == 'Techno Music' or Genre1.strip() == 'techno music' or Genre1.strip() == 'tech music' or Genre1.strip() == 'Tech Music':
            return render_template('/Music/MusicTechno.html', genremain='Techno Music: ')
        else:
            return render_template('Music.html', genremain='No Such Genre in database')


        return render_template('Music.html', genremain=Genre1)


@app.route('/easteregg/')
def easteregg():
    return render_template('EasterEgg.html', genremain="EasterEgg!")

@app.route('/paintingdescriptions')
def paintingdescriptions():
    return render_template("paintingdescriptions.html")

@app.route('/paintinglist')
def paintinglist():
    return render_template("paintinglist.html", paintings=painting_list)

@app.route('/moviesummaries')
def moviesummaries():
    return render_template("moviesummaries.html")

@app.route('/actionmovies')
def actionmovies():
    return render_template("actionmovies.html")

@app.route('/Privatepage')
def Privatepage():
    return render_template("Privatepage.html")

@app.route('/img')
def hello_world():
    return render_template("index.html")

@app.route('/marc')
def marclinkedin():
    return render_template("marclinkedin.html")

@app.route('/james')
def jameslinkedin():
    return render_template("jameslikendin.html")

@app.route('/francis')
def francislinkedin():
    return render_template("francislinkedin.html")

@app.route('/upload', methods=['GET','POST'])
def upload():
    pic = request.files['pic']

    if not pic:
        return 'No pic uploaded', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype

    img = Img(img=pic.read(), mimetype=mimetype, name=filename)
    db.session.add(img)
    db.session.commit()

    return 'Img has been uploaded!', 200


@app.route('/<int:id>')
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'No img with that id', 200

    return Response(img.img, mimetype=img.mimetype)


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='127.0.0.1')


