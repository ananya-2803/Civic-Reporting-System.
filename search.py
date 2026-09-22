from database import load_complaints


def search_complaint():
    complaints = load_complaints()

    print("\n========== SEARCH COMPLAINT ==========")

    print("1. Search by Complaint ID")
    print("2. Search by Location")
    print("3. Search by Problem Type")

    choice = input("Enter choice: ")

    if choice == "1":

        try:
            complaint_id = int(input("Enter Complaint ID: "))
        except ValueError:
            print("Invalid ID.")
            return

        results = [
            c for c in complaints
            if c["id"] == complaint_id
        ]

    elif choice == "2":

        location = input("Enter location: ").lower()

        results = [
            c for c in complaints
            if location in c["location"].lower()
        ]

    elif choice == "3":

        problem = input("Enter problem type: ").lower()

        results = [
            c for c in complaints
            if problem in c["problem_type"].lower()
        ]

    else:
        print("Invalid choice.")
        return

    if not results:
        print("\nNo matching complaints found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for complaint in results:

        print("\nComplaint ID:", complaint["id"])
        print("Name:", complaint["name"])
        print("Location:", complaint["location"])
        print("Problem:", complaint["problem_type"])
        print("Description:", complaint["description"])
        print("Status:", complaint["status"])
        print("--------------------------------")