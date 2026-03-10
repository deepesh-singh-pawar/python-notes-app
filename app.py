from flask import Flask, render_template, request, redirect, url_for
from typing import List
import os

app = Flask(__name__)

# Simple in‑memory list to store notes
notes: List[str] = []

@app.route("/", methods=["GET", "POST"])
def index():

    """Render the main page and handle new note submissions."""

    # If user submits a note, use POST‑redirect‑GET
    if request.method == "POST":
        note = request.form.get("note")

        if note:
            notes.append(note)

        return redirect(url_for("index"))

    return render_template("index.html", notes=notes)


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "1") == "1"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)