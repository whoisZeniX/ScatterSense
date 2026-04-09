from flask import Flask, render_template, request, redirect

from database import initialize_database, insert_session, fetch_sessions

app = Flask(__name__)

initialize_database()

def handle_submission():
    session_date = request.form.get("session_date")
    time_period = request.form.get("time_period")
    duration = request.form.get("duration")
    energy_level = request.form.get("energy_level")
    task_type = request.form.get("task_type")

    insert_session(session_date, time_period, duration, energy_level, task_type)

 @app.route("/")
def landing():
    return render_template("index.html")   

@app.route("/")
def landing():
    if request.method == "POST":
        handle_submission()
        return redirect("/dashboard")

    sessions = fetch_sessions()
    return render_template("dashboard.html", sessions=sessions )

if __name__ == "__main__":
    app.run(debug=True)