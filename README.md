Civic Reporting System

1. Project Overview

The Civic Reporting System is a Python-based application designed to allow citizens to report common civic problems such as potholes, garbage, damaged roads, broken streetlights, water leakage, fallen trees, and traffic problems.

The system stores complaint information and provides features for viewing, searching, updating, and generating reports about civic complaints.

2. Objectives

- To provide a simple way to report civic problems.
- To store complaint information systematically.
- To allow complaints to be searched easily.
- To allow administrators to update complaint status.
- To generate a summary of reported civic problems.

3. Features

- Report a civic complaint
- Generate a unique complaint ID
- View all complaints
- Search complaints
- Update complaint status
- Generate complaint statistics
- Store data using JSON
- Input validation and error handling

4. Technologies Used

- Python
- JSON
- Git
- GitHub
- Visual Studio Code

5. Project Modules

main.py

Provides the main menu and connects all modules.

complaint.py

Handles submission of new civic complaints.

database.py

Handles storing and loading complaint data from the JSON file.

admin.py

Allows complaints to be viewed and their status to be updated.

search.py

Provides search functionality for complaints.

report.py

Generates complaint statistics and summaries.

validation.py

Validates user input.

complaints.json

Stores complaint data.

6. Complaint Status

A complaint can have one of the following statuses:

- Pending
- In Progress
- Resolved

7. How to Run

1. Download or clone the project repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

python main.py

5. Select an option from the displayed menu.

8. Main Menu

The system provides the following options:

1. Report a Complaint
2. View All Complaints
3. Search Complaint
4. Update Complaint Status
5. Generate Complaint Report
6. Exit

9. Data Storage

Complaint information is stored in the "complaints.json" file.

Each complaint contains:

- Complaint ID
- Citizen name
- Location
- Problem type
- Description
- Status

10. Testing

The system was tested by:

- Adding multiple complaints
- Viewing stored complaints
- Searching complaints
- Updating complaint status
- Generating complaint statistics
- Testing invalid inputs

11. Future Enhancements

- Web-based interface
- User login and authentication
- Photo upload for complaints
- GPS-based location
- Email/SMS notifications
- Database such as MySQL
- Administrator dashboard
- Online deployment