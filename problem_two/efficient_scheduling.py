def greedy_schedule(sessions):
    """
    Schedule the maximum number of non-overlapping sessions using a greedy algorithm.

    :param sessions: List of tuples [(start_time, end_time, name), ...]
    :return: List of selected sessions
    """
    # Sort sessions by their end time
    sessions.sort(key=lambda x: x[1])

    selected_sessions = []
    last_end_time = 9  # Start scheduling from 9 AM

    for start, end, name in sessions:
        if start >= last_end_time:
            selected_sessions.append((start, end, name))
            last_end_time = end

    return selected_sessions

def test_greedy_schedule():
    # Static schedule for courses (Start Time, End Time, Course Name)
    test_cases = [
        # Monday
        [
            (9, 10, "Introduction to Programming"),
            (9, 11, "Data Structures"),
            (10, 12, "Algorithms"),
            (13, 14, "Database Management Systems"),
            (13, 15, "Operating Systems"),
            (14, 16, "Software Engineering"),
            (15, 17, "Computer Networks"),
        ],
        # Tuesday
        [
            (9, 10, "Artificial Intelligence"),
            (9, 12, "Machine Learning"),
            (10, 11, "Web Development"),
            (13, 14, "Mobile App Development"),
            (14, 15, "Cybersecurity"),
            (14, 16, "Cloud Computing"),
            (15, 17, "Human-Computer Interaction"),
        ],
        # Wednesday
        [
            (9, 10, "Ethics in Computing"),
            (9, 11, "Compiler Design"),
            (10, 12, "Introduction to Programming"),
            (13, 14, "Data Structures"),
            (13, 15, "Algorithms"),
            (14, 16, "Database Management Systems"),
            (15, 17, "Operating Systems"),
        ],
        # Thursday
        [
            (9, 10, "Software Engineering"),
            (9, 11, "Computer Networks"),
            (10, 12, "Artificial Intelligence"),
            (13, 14, "Machine Learning"),
            (14, 15, "Web Development"),
            (14, 16, "Mobile App Development"),
            (15, 17, "Cybersecurity"),
        ],
        # Friday
        [
            (9, 10, "Cloud Computing"),
            (9, 12, "Human-Computer Interaction"),
            (10, 11, "Ethics in Computing"),
            (13, 14, "Compiler Design"),
            (14, 15, "Introduction to Programming"),
            (14, 16, "Data Structures"),
            (15, 17, "Algorithms"),
        ],
    ]

    # Display results for each day
    for i, sessions in enumerate(test_cases):
        result = greedy_schedule(sessions)
        total_hours = sum(end - start for start, end, _ in result)
        print(f"Day {i + 1}:")
        print(f"Original Sessions:")
        for session in sessions:
            print(f"  {session[0]}:00-{session[1]}:00 -> {session[2]}")
        print(f"Selected Sessions:")
        for start, end, name in result:
            print(f"  {start}:00-{end}:00 -> {name}")
        print(f"Total Hours Taken: {total_hours}")
        print("-" * 40)

if __name__ == "__main__":
    test_greedy_schedule()
