from flask import Flask, render_template, request, redirect

from database import initialize_database, insert_session, fetch_sessions, delete_session
from utils.analysis import analyze_sessions

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

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        handle_submission()
        return redirect("/dashboard")

    sessions = fetch_sessions()
    insights = analyze_sessions(sessions)
    return render_template("dashboard.html", sessions=sessions, insights=insights)

@app.route("/delete/<int:session_id>", methods=["POST"])
def remove_sessions(session_id):
    delete_session(session_id)
    return redirect("/dashboard")

if __name__ == "__main__"
    app.run(debug=True)    