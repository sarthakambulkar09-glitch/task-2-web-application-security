from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)

# Intentionally simple secret for LOCAL SECURITY TESTING ONLY.
app.secret_key = "securelab-test-secret"

# Intentionally predictable test credentials.
# DO NOT use this authentication design in production.
USERS = {
    "admin": {
        "password": "admin123",
        "name": "Administrator",
        "email": "admin@securelab.local",
        "role": "Administrator"
    },
    "student": {
        "password": "student123",
        "name": "Test Student",
        "email": "student@securelab.local",
        "role": "Student"
    }
}


@app.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        user = USERS.get(username)

        if user and user["password"] == password:
            session["username"] = username
            return redirect("/dashboard")

        error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    username = session.get("username")

    # Authentication check.
    if not username:
        return redirect("/")

    user = USERS.get(username)

    if not user:
        session.clear()
        return redirect("/")

    return render_template(
        "dashboard.html",
        username=username,
        user=user
    )


@app.route("/profile")
def profile():
    username = session.get("username")

    if not username:
        return redirect("/")

    user = USERS.get(username)

    if not user:
        session.clear()
        return redirect("/")

    return render_template(
        "profile.html",
        username=username,
        user=user
    )


@app.route("/search", methods=["POST"])
def search():
    username = session.get("username")

    if not username:
        return redirect("/")

    query = request.form.get("query", "")

    # INTENTIONALLY VULNERABLE:
    # User input is inserted directly into an HTML response.
    # This exists ONLY for the local security-testing exercise.
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Search Results - SecureLab</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>
        <nav>
            <div class="logo">SecureLab</div>
            <div>
                <a href="/dashboard">Dashboard</a>
                <a href="/profile">Profile</a>
                <a href="/logout">Logout</a>
            </div>
        </nav>

        <main class="container">
            <div class="card">
                <h1>Search Results</h1>

                <p>Your search query was:</p>

                <div class="result">
                    {query}
                </div>

                <a class="button" href="/dashboard">
                    Back to Dashboard
                </a>
            </div>
        </main>
    </body>
    </html>
    """


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.errorhandler(404)
def page_not_found(error):
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>404 - SecureLab</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>
        <div class="container">
            <div class="card">
                <h1>404</h1>
                <p>The requested page was not found.</p>
                <a class="button" href="/">Return to Login</a>
            </div>
        </div>
    </body>
    </html>
    """, 404


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
)
