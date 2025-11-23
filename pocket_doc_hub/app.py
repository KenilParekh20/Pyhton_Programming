from flask import Flask, render_template, request, redirect, url_for, flash
import os, sqlite3
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = "mysecret"
app.config['UPLOAD_FOLDER'] = "uploads"
DB_FILE = "app.db"
ALLOWED = {'pdf', 'png', 'jpg', 'txt', 'docx'}

def create_db():
    con = sqlite3.connect(DB_FILE)
    con.execute('''CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        savedname TEXT,
        uploaded_time TEXT
    )''')
    con.close()

@app.route('/')
def home():
    con = sqlite3.connect(DB_FILE)
    con.row_factory = sqlite3.Row
    files = con.execute("SELECT * FROM files ORDER BY id DESC").fetchall()
    con.close()
    return render_template("index.html", files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.split('.')[-1].lower() in ALLOWED:
            filename = secure_filename(file.filename)
            new_name = datetime.now().strftime("%Y%m%d%H%M%S_") + filename
            path = os.path.join(app.config['UPLOAD_FOLDER'], new_name)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file.save(path)
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            con = sqlite3.connect(DB_FILE)
            con.execute("INSERT INTO files (filename, savedname, uploaded_time) VALUES (?, ?, ?)",
                        (filename, new_name, time_now))
            con.commit()
            con.close()
            flash("File uploaded successfully!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid file type!", "danger")
    return render_template("upload.html")

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
