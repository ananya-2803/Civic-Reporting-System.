from database import add_complaint, get_next_id
from validation import (
    validate_name,
    validate_location,
    validate_description
)


def report_complaint():
    print("\n========== REPORT A COMPLAINT ==========")

    name = input("Enter your name: ").strip()

    if not validate_name(name):
        print("Invalid name.")
        return

    location = input("Enter location: ").strip()

    if not validate_location(location):
        print("Invalid location.")
        return

    print("\nSelect Problem Type:")
    print("1. Pothole")
    print("2. Garbage")
    print("3. Streetlight")
    print("4. Water Leakage")
    print("5. Damaged Road")
    print("6. Fallen Tree")
    print("7. Traffic Problem")

    choice = input("Enter your choice: ")

    problem_types = {
        "1": "Pothole",
        "2": "Garbage",
        "3": "Streetlight",
        "4": "Water Leakage",
        "5": "Damaged Road",
        "6": "Fallen Tree",
        "7": "Traffic Problem"
    }

    if choice not in problem_types:
        print("Invalid problem type.")
        return

    problem_type = problem_types[choice]

    description = input("Describe the problem: ").strip()

    if not validate_description(description):
        print("Description cannot be empty.")
        return

    complaint_id = get_next_id()

    complaint = {
        "id": complaint_id,
        "name": name,
        "location": location,
        "problem_type": problem_type,
        "description": description,
        "status": "Pending"
    }

    add_complaint(complaint)

    print("\nComplaint submitted successfully!")
    print("Your Complaint ID is:", complaint_id)