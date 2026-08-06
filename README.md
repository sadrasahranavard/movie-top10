```markdown
# Movie Top 10

A personal movie ranking website with a curated list of 50 must-watch films. Built with Flask and SQLite.

---

## Features

- Rank your top 10 movies by rating
- Add movies with title, year, rating, review, and poster (URL or file upload)
- Edit ratings, reviews, and posters
- Delete movies from your collection
- Star ratings displayed visually
- Dark cinematic theme with gold accents
- Flash messages for success and error feedback
- Custom 404 error page
- Responsive design

---

## Bonus Feature: 50 Must-Watch Films

A carefully curated list of 50 essential films spanning from 1910s to 2010s. Each entry includes:

- Year and director
- A detailed description of the film
- A personal explanation of why it was chosen

Written from the perspective of someone who has watched many films

---

## Installation

```bash
git clone https://github.com/sadrasahranavard/movie-top10.git
cd movie-top10
python -m venv venv
venv\Scripts\activate
pip install flask
```

---

## Usage

```bash
python main.py
```

Open http://127.0.0.1:5000 in your browser.

### Pages

| Route | Description |
|-------|-------------|
| `/` | Homepage — top 10 movies ranked by rating |
| `/add` | Add a new movie to your collection |
| `/edit/<id>` | Edit a movie's rating, review, or poster |
| `/select` | Manage all movies (edit or delete) |
| `/must-watch` | 50 must-watch films with commentary |
| `/delete/<id>` | Delete a movie (POST only) |

---

## Project Structure

```
movie-top10/
├── main.py                 # Flask application
├── data/
│   └── must_watch.json     # 50 curated films
├── static/
│   ├── style.css           # Dark cinematic theme
│   └── posters/            # Uploaded poster images
├── templates/
│   ├── index.html          # Homepage
│   ├── add.html            # Add movie form
│   ├── edit.html           # Edit movie form
│   ├── select.html         # Manage movies
│   ├── must-watch.html     # 50 films page
│   └── 404.html            # Custom error page
├── instance/
│   └── movies.db           # SQLite database (auto-created)
├── requirements.txt
└── README.md
```

---

## Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS (dark cinematic theme)
- **Fonts:** Playfair Display, Inter (Google Fonts)

---