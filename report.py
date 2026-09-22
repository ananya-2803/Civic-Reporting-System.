from database import load_complaints


def generate_report():
    complaints = load_complaints()

    print("\n========== CIVIC REPORT ==========")

    total = len(complaints)

    pending = 0
    in_progress = 0
    resolved = 0

    problem_count = {}

    for complaint in complaints:

        status = complaint["status"]

        if status == "Pending":
            pending += 1

        elif status == "In Progress":
            in_progress += 1

        elif status == "Resolved":
            resolved += 1

        problem = complaint["problem_type"]

        if problem in problem_count:
            problem_count[problem] += 1
        else:
            problem_count[problem] = 1

    print("\nTotal Complaints:", total)
    print("Pending:", pending)
    print("In Progress:", in_progress)
    print("Resolved:", resolved)

    print("\nProblem-wise Statistics:")

    if not problem_count:
        print("No complaints available.")

    else:
        for problem, count in problem_count.items():
            print(problem, ":", count)