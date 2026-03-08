from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simple list to store notes
notes = []

@app.route("/", methods=["GET", "POST"])
def index():

    # If user submits note
    if request.method == "POST":
        note = request.form.get("note")

        if note:
            notes.append(note)

        return redirect("/")

    return render_template("index.html", notes=notes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)