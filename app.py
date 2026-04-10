import csv
import io
from flask import Flask, render_template, request, redirect, jsonify, Response

from database import initialize_database, insert_session, fetch_sessions, fetch_filtered_sessions, delete_session
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

    date_from = request.args.get("date_from")
    date_to = request.args.get("date_to")
    task_search = request.args.get("task_search")
    energy_filter = request.args.get("energy_filter")

    has_filters = any([date_from, date_to, task_search, energy_filter])

    if has_filters:
        sessions = fetch_filtered_sessions(date_from, date_to, task_search, energy_filter)
    else:
        sessions = fetch_sessions()

    insights = analyze_sessions(sessions)
    return render_template("dashboard.html", sessions=sessions, insights=insights,
                           date_from=date_from or "", date_to=date_to or "",
                           task_search=task_search or "", energy_filter=energy_filter or "")

@app.route("/delete/<int:session_id>", methods=["POST"])
def remove_session(session_id):
    delete_session(session_id)
    return redirect("/dashboard")

@app.route("/chart-data")
def chart_data():
    sessions = fetch_sessions()
    insights = analyze_sessions(sessions)
    return jsonify(insights)

@app.route("/export")
def export_data():
    sessions = fetch_sessions()
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(["ID", "Date", "Time Period", "Duration (min)", "Energy Level", "Task Type"])
    for session in sessions:
        cw.writerow(session)

    response = Response(si.getvalue(), mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=scattersense_sessions.csv"
    return response

if __name__ == "__main__":
    app.run(debug=True)
