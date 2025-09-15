
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path(__file__).resolve().parent / "todo.db"

SCHEMA = '''
CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
'''

def get_conn():
    return sqlite3.connect(DB_PATH)

@app.cli.command("init-db")
def init_db_cmd():
    with get_conn() as conn:
        conn.executescript(SCHEMA)
    print("Initialized todo.db")

@app.route("/", methods=["GET"])
def index():
    with get_conn() as conn:
        rows = conn.execute("SELECT id,title,done,created_at FROM todos ORDER BY created_at DESC").fetchall()
    return render_template("index.html", todos=rows)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title","").strip()
    if title:
        with get_conn() as conn:
            conn.execute("INSERT INTO todos (title) VALUES (?)", (title,))
            conn.commit()
    return redirect(url_for("index"))

@app.route("/toggle/<int:tid>", methods=["POST"])
def toggle(tid):
    with get_conn() as conn:
        cur = conn.execute("SELECT done FROM todos WHERE id=?", (tid,)).fetchone()
        if cur:
            newv = 0 if cur[0] else 1
            conn.execute("UPDATE todos SET done=? WHERE id=?", (newv, tid))
            conn.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:tid>", methods=["POST"])
def delete(tid):
    with get_conn() as conn:
        conn.execute("DELETE FROM todos WHERE id=?", (tid,))
        conn.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "init-db":
        with get_conn() as conn:
            conn.executescript(SCHEMA)
        print("Initialized todo.db")
    else:
        app.run(debug=True)
