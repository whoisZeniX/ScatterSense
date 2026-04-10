def analyze_sessions(sessions):
    if not sessions:
        return {}
    
    time_counts = {}
    total_duration = 0
    energy_counts = {}

    for session in sessions:
        time_period = session[1]
        duration = int(session[2])
        energy = session[3]

        time_counts[time_period] = time_counts.get(time_period, 0) + 1
        energy_counts[energy] = energy_counts.get(energy, 0) + 1
        total_duration += duration

    most_productive_time = max(time_counts, key=time_counts.get)
    most_common_energy = max(energy_counts, key=energy_counts.get)
    average_duration = total_duration // len(sessions)

    return {
        "most_productive_time": most_productive_time,
        "most_common_energy": most_common_energy,
        "average_duration": average_duration
    }    