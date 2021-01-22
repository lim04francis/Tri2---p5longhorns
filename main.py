

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, Response
from werkzeug.utils import secure_filename
from db import db_init, db
from models import Img
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
    return render_template("photography.html")

@app.route('/quotesapi')
def quotesapi():
    return render_template("quotesapi.html")

@app.route('/Movies')
def Movies():
    return render_template("Movies.html")

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
            return render_template('MusicClassical.html', genremain='Classical Music:')
        elif Genre1.strip() == 'Jazz' or Genre1.strip() == 'jazz' or Genre1.strip() == 'Jazz Music' or Genre1.strip() == 'jazz music':
            return render_template('MusicJazz.html', genremain='Jazz Music:')

        return render_template('Music.html', genremain=Genre1)


@app.route('/paintingdescriptions')
def paintingdescriptions():
    return render_template("paintingdescriptions.html")

@app.route('/moviesummaries')
def moviesummaries():
    return render_template("moviesummaries.html")

@app.route('/actionmovies')
def actionmovies():
    return render_template("actionmovies.html")

@app.route('/img')
def hello_world():
    return render_template("index.html")

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
