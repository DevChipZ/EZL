from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage
users = {}
concept_history = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            return "User already exists!"

        users[username] = password
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username not in users:
            return "User not found!"

        if users[username] != password:
            return "Incorrect password!"

        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/create-concept", methods=["GET", "POST"])
def create_concept():

    if request.method == "POST":

        concept = request.form["concept"]

        concept_history.setdefault("demo_user", []).append(concept)

        return render_template(
            "concept_created.html",
            concept=concept
        )

    return render_template("create_concept.html")


@app.route("/history")
def history():

    history = concept_history.get("demo_user", [])

    return render_template(
        "history.html",
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)
