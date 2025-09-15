# Flask To-Do (CRUD + SQLite)

A minimal full-stack Flask app: add tasks, toggle done/undo, and delete. Data persists in a local **SQLite** DB. Good starter project to show **routing**, **templates (Jinja)**, and **CRUD**.

## Demo (local)
```bash
git clone git@github.com:diasflx/flask-todo.git
cd flask-todo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# initialize the database
python app.py init-db

# run the server
python app.py run
# open http://127.0.0.1:5000

Features

* Add a task (HTML form → POST /add)

* Toggle done/undo (POST /toggle/<id>)

* Delete (POST /delete/<id>)

* Server-side rendered UI (Jinja templates)

* Tiny CSS, no JS required

Tech Stack

* Python 3, Flask

* SQLite via sqlite3

* HTML/CSS templates (Jinja)

Project Structure

flask-todo/
├─ app.py
├─ templates/
│  ├─ base.html
│  └─ index.html
├─ requirements.txt
└─ README.md

