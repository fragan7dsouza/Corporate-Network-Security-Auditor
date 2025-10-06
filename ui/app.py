from flask import Flask, render_template
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.database import get_scans, init_db

app = Flask(__name__)

@app.route("/")
def dashboard():
    init_db() 
    scans = get_scans(limit=10)
    return render_template("dashboard.html", scans=scans)

if __name__ == "__main__":
    app.run(debug=True)
