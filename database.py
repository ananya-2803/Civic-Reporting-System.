import json

FILE_NAME = "complaints.json"


def load_complaints():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_complaints(complaints):
    with open(FILE_NAME, "w") as file:
        json.dump(complaints, file, indent=4)


def add_complaint(complaint):
    complaints = load_complaints()
    complaints.append(complaint)
    save_complaints(complaints)


def get_next_id():
    complaints = load_complaints()

    if not complaints:
        return 1001

    return max(complaint["id"] for complaint in complaints) + 1