from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import json
import os

app = Flask(__name__)
app.secret_key = 'movie-top10-secret-key'


def get_db():
    conn = sqlite3.connect('instance/movies.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    os.makedirs('instance', exist_ok=True)
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER,
            rating REAL NOT NULL DEFAULT 0,
            review TEXT DEFAULT '',
            poster_url TEXT DEFAULT ''
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    conn = get_db()
    movies = conn.execute('SELECT * FROM movies ORDER BY rating DESC').fetchall()
    conn.close()
    return render_template('index.html', movies=movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        year = request.form.get('year', type=int)
        rating = request.form.get('rating', type=float)
        review = request.form.get('review', '').strip()
        poster_url = request.form.get('poster_url', '').strip()

        if not title:
            flash('Title is required.', 'error')
            return render_template('add.html')

        if rating is None or not (0 <= rating <= 10):
            flash('Rating must be between 0 and 10.', 'error')
            return render_template('add.html')

        conn = get_db()
        conn.execute(
            'INSERT INTO movies (title, year, rating, review, poster_url) VALUES (?, ?, ?, ?, ?)',
            (title, year, rating, review, poster_url)
        )
        conn.commit()
        conn.close()

        flash(f'"{title}" added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db()
    movie = conn.execute('SELECT * FROM movies WHERE id = ?', (id,)).fetchone()

    if movie is None:
        conn.close()
        flash('Movie not found.', 'error')
        return redirect(url_for('select'))

    if request.method == 'POST':
        rating = request.form.get('rating', type=float)
        review = request.form.get('review', '').strip()
        poster_url = request.form.get('poster_url', '').strip()

        if rating is None or not (0 <= rating <= 10):
            flash('Rating must be between 0 and 10.', 'error')
            return render_template('edit.html', movie=movie)

        conn.execute(
            'UPDATE movies SET rating = ?, review = ?, poster_url = ? WHERE id = ?',
            (rating, review, poster_url, id)
        )
        conn.commit()
        conn.close()

        flash(f'"{movie["title"]}" updated!', 'success')
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', movie=movie)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db()
    movie = conn.execute('SELECT * FROM movies WHERE id = ?', (id,)).fetchone()

    if movie is None:
        conn.close()
        flash('Movie not found.', 'error')
        return redirect(url_for('select'))

    conn.execute('DELETE FROM movies WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    flash(f'"{movie["title"]}" deleted.', 'success')
    return redirect(url_for('select'))


@app.route('/select')
def select():
    conn = get_db()
    movies = conn.execute('SELECT * FROM movies ORDER BY title').fetchall()
    conn.close()
    return render_template('select.html', movies=movies)


@app.route('/must-watch')
def must_watch():
    with open('data/must_watch.json', 'r', encoding='utf-8') as f:
        films = json.load(f)
    return render_template('must-watch.html', films=films)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    init_db()
    app.run(debug=True)