from database import load_complaints, save_complaints


def view_complaints():
    complaints = load_complaints()

    print("\n========== ALL COMPLAINTS ==========")

    if not complaints:
        print("No complaints found.")
        return

    for complaint in complaints:
        print("\nComplaint ID:", complaint["id"])
        print("Name:", complaint["name"])
        print("Location:", complaint["location"])
        print("Problem:", complaint["problem_type"])
        print("Description:", complaint["description"])
        print("Status:", complaint["status"])
        print("--------------------------------")


def update_status():
    complaints = load_complaints()

    if not complaints:
        print("\nNo complaints available.")
        return

    try:
        complaint_id = int(input("Enter Complaint ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for complaint in complaints:

        if complaint["id"] == complaint_id:

            print("\nCurrent Status:", complaint["status"])

            print("\nSelect New Status:")
            print("1. Pending")
            print("2. In Progress")
            print("3. Resolved")

            choice = input("Enter choice: ")

            status = {
                "1": "Pending",
                "2": "In Progress",
                "3": "Resolved"
            }

            if choice not in status:
                print("Invalid choice.")
                return

            complaint["status"] = status[choice]

            save_complaints(complaints)

            print("\nComplaint status updated successfully!")
            return

    print("Complaint ID not found.")