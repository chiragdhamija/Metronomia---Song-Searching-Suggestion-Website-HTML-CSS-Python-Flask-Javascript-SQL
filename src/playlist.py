import sqlite3
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

conn = sqlite3.connect('playlist.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS songs
    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)
''')

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/indextopalbum')
def indextopalbum():
    home()
    return redirect('/#topalbum')

@app.route('/artists')
def artists():
    return render_template('artists.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/spotlight')
def spotlight():
    return render_template('spotlight.html')

@app.route('/playlist')
def playlist():
    conn=sqlite3.connect('playlist.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM songs')
    data=cursor.fetchall()
    return render_template('playlist.html', data=data)

@app.route('/Sidhu_Moosewala')
def Sidhu_Moosewala():
    return render_template('artist01-albums.html')

@app.route('/Sidhu_Moosewala/Moosetape')
def Moosetape():
    return render_template('album11-songs.html')

@app.route('/Sidhu_Moosewala/Pbx1')
def Pbx1():
    return render_template('album12-songs.html')

@app.route('/Sidhu_Moosewala/Snitches_Get_Stitches')
def Snitches_Get_Stitches():
    return render_template('album13-songs.html')

@app.route('/Sidhu_Moosewala/Yes_I_Am_Student')
def Yes_I_Am_Student():
    return render_template('album14-songs.html')

@app.route('/Sidhu_Moosewala/No_Name')
def No_Name():
    return render_template('album15-songs.html')

@app.route('/Nucleya')
def Nucleya():
    return render_template('artist02-albums.html')

@app.route('/Nucleya/Bass_Rani')
def Bass_Rani():
    return render_template('album21-songs.html')

@app.route('/Nucleya/Tota_Myna')
def Tota_Myna():
    return render_template('album22-songs.html')

@app.route('/Nucleya/Koocha_Monster')
def Koocha_Monster():
    return render_template('album23-songs.html')

@app.route('/Nucleya/Horn_Ok_Please')
def Horn_Ok_Please():
    return render_template('album24-songs.html')

@app.route('/Nucleya/In_My_Heart_Remixes')
def In_My_Heart_Remixes():
    return render_template('album25-songs.html')

@app.route('/Imagine_Dragons')
def Imagine_Dragons():
    return render_template('artist03-albums.html')

@app.route('/Imagine_Dragons/Night_Visions')
def Night_Visions():
    return render_template('album31-songs.html')

@app.route('/Imagine_Dragons/Evolve')
def Evolve():
    return render_template('album32-songs.html')

@app.route('/Imagine_Dragons/Origins_Deluxe')
def Origins_Deluxe():
    return render_template('album33-songs.html')

@app.route('/Imagine_Dragons/Mercury_Acts')
def Mercury_Acts():
    return render_template('album34-songs.html')

@app.route('/Imagine_Dragons/Smoke_Mirrors_Deluxe')
def Smoke_Mirrors_Deluxe():
    return render_template('album35-songs.html')

@app.route('/Alan_Walker')
def Alan_Walker():
    return render_template('artist04-albums.html')

@app.route('/Alan_Walker/Different_World')
def Different_World():
    return render_template('album41-songs.html')

@app.route('/Alan_Walker/World_of_Walker')
def World_of_Walker():
    return render_template('album42-songs.html')

@app.route('/Alan_Walker/Walkerverse')
def Walkerverse():
    return render_template('album43-songs.html')

@app.route('/Alan_Walker/Walker_Racing_League')
def Walker_Racing_League():
    return render_template('album44-songs.html')

@app.route('/Alan_Walker/The_Club_Iguana_Years')
def The_Club_Iguana_Years():
    return render_template('album45-songs.html')

@app.route('/Diljit_Dosanjh')
def Diljit_Dosanjh():
    return render_template('artist05-albums.html')

@app.route('/Diljit_Dosanjh/GOAT')
def GOAT():
    return render_template('album51-songs.html')

@app.route('/Diljit_Dosanjh/Drive_Thru')
def Drive_Thru():
    return render_template('album52-songs.html')

@app.route('/Diljit_Dosanjh/MoonChildEra')
def MoonChildEra():
    return render_template('album53-songs.html')

@app.route('/Diljit_Dosanjh/ConFiDenTial')
def ConFiDenTial():
    return render_template('album54-songs.html')

@app.route('/Diljit_Dosanjh/Back_To_Basics')
def Back_To_Basics():
    return render_template('album55-songs.html')

@app.route('/Raghu_Dixit')
def Raghu_Dixit():
    return render_template('artist06-albums.html')

@app.route('/Raghu_Dixit/Antaragni')
def Antaragni():
    return render_template('album61-songs.html')

@app.route('/Raghu_Dixit/Jag_Changa')
def Jag_Changa():
    return render_template('album62-songs.html')

@app.route('/Raghu_Dixit/Raghu_Dixit_Unplugged')
def Raghu_Dixit_Unplugged():
    return render_template('album63-songs.html')

@app.route('/Raghu_Dixit/Courtyard_Jam_Sessions')
def Courtyard_Jam_Sessions():
    return render_template('album64-songs.html')

@app.route('/Starboy')
def Starboy():
    return render_template('album71-songs.html')

@app.route('/The_Carnival')
def The_Carnival():
    return render_template('album81-songs.html')

@app.route('/Rockstar')
def Rockstar():
    return render_template('album91-songs.html')

@app.route('/add_song', methods=['POST'])
def add_song():
    conn = sqlite3.connect('playlist.db')
    cursor = conn.cursor()
    song_name = request.json['song_name']

    cursor.execute('SELECT * FROM songs WHERE name=?', (song_name,))
    result = cursor.fetchone()

    if result is None:
        cursor.execute('INSERT INTO songs (name) VALUES (?)', (song_name,))
        conn.commit()
        return 'Song added successfully!', 200
    else:
        return 'Song already exists.', 409

@app.route('/remove_song', methods=['POST'])
def remove_song():
    conn=sqlite3.connect('playlist.db')
    cursor=conn.cursor()
    song_id=request.form['song_id']
    cursor.execute('DELETE FROM songs WHERE id = ?', (song_id,))
    conn.commit()
    return redirect(url_for('playlist'))

if __name__ == '__main__':
    app.run(debug=True)