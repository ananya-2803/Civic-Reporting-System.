def validate_name(name):
    return name.strip() != ""


def validate_location(location):
    return location.strip() != ""


def validate_description(description):
    return description.strip() != ""


def validate_problem_type(problem_type):
    valid_types = [
        "Pothole",
        "Garbage",
        "Streetlight",
        "Water Leakage",
        "Damaged Road",
        "Fallen Tree",
        "Traffic Problem"
    ]

    return problem_type in valid_types