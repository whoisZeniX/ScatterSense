def analyze_sessions(sessions):
    if not sessions:
        return {}

    time_counts = {}
    total_duration = 0
    energy_counts = {}
    task_counts = {}
    energy_map = {"low": 1, "medium": 2, "high": 3}
    energy_scores = []

    for session in sessions:
        time_period = session[1]
        duration = int(session[2])
        energy = session[3]
        task = session[5] if len(session) > 5 else "unknown"

        time_counts[time_period] = time_counts.get(time_period, 0) + 1
        energy_counts[energy] = energy_counts.get(energy, 0) + 1
        task_counts[task] = task_counts.get(task, 0) + 1
        total_duration += duration

        if energy in energy_map:
            energy_scores.append(energy_map[energy])

    most_productive_time = max(time_counts, key=time_counts.get)
    most_common_energy = max(energy_counts, key=energy_counts.get)
    average_duration = total_duration // len(sessions)

    total_sessions = len(sessions)
    total_focus_hours = round(total_duration / 60, 1)

    avg_energy = sum(energy_scores) / len(energy_scores) if energy_scores else 0
    duration_score = min(average_duration / 60, 1.0)
    energy_score = avg_energy / 3.0
    consistency_score = min(total_sessions / 20, 1.0)
    productivity_score = round((duration_score * 40 + energy_score * 35 + consistency_score * 25), 1)

    unique_dates = set()
    for session in sessions:
        if session[1]:
            unique_dates.add(session[1])

    sorted_dates = sorted(unique_dates)
    streak = 0
    if sorted_dates:
        streak = 1

    return {
        "most_productive_time": most_productive_time,
        "most_common_energy": most_common_energy,
        "average_duration": average_duration,
        "total_sessions": total_sessions,
        "total_focus_hours": total_focus_hours,
        "productivity_score": productivity_score,
        "streak": streak,
        "total_duration": total_duration
    }
