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

11.Sample Output
======================================
       CIVIC REPORTING SYSTEM
======================================
1. Report a Complaint
2. View All Complaints
3. Search Complaint
4. Update Complaint Status
5. Generate Complaint Report
6. Exit

Enter your choice: 1

========== REPORT A COMPLAINT ==========
Enter your name: Nancy
Enter location: Delhi 

Select Problem Type:
1. Pothole
2. Garbage
3. Streetlight
4. Water Leakage
5. Damaged Road
6. Fallen Tree
7. Traffic Problem
Enter your choice: 4
Describe the problem: There's water leakage in my area.

Complaint submitted successfully!
Your Complaint ID is: 1008

======================================
       CIVIC REPORTING SYSTEM
======================================
1. Report a Complaint
2. View All Complaints
3. Search Complaint
4. Update Complaint Status
5. Generate Complaint Report
6. Exit

Enter your choice: 2

========== ALL COMPLAINTS ==========

Complaint ID: 1001
Name: Ananya
Location: VIT Bhopal main gate
Problem: Pothole
Description: There is a large pothole near the main gate .
Status: Resolved
--------------------------------

Complaint ID: 1002
Name: Riya
Location: Hostel Area
Problem: Garbage
Description: Garbage has not been collected.
Status: Pending
--------------------------------

Complaint ID: 1003
Name: Priya
Location: Hostel Block
Problem: Water Leakage
Description: Water is leaking near the entrance.
Status: Pending
--------------------------------

Complaint ID: 1004
Name: Aman
Location: Campus Road
Problem: Damaged Road
Description: Road surface is damaged.
Status: Pending
--------------------------------

Complaint ID: 1005
Name: Garima
Location: Bhopal
Problem: Damaged Road
Description: The road here is damaged badly.
Status: Resolved
--------------------------------

Complaint ID: 1006
Name: Mayank
Location: Ghaziabaad
Problem: Garbage
Description: Lack of dustbins .
Status: Pending
--------------------------------

Complaint ID: 1007
Name: Kavita
Location: Bhopal
Problem: Streetlight
Description: The lights are not working
Status: Pending
--------------------------------

Complaint ID: 1008
Name: Nancy
Location: Delhi
Problem: Water Leakage
Description: There's water leakage in my area.
Status: Pending
--------------------------------
======================================
       CIVIC REPORTING SYSTEM
======================================
1. Report a Complaint
2. View All Complaints
3. Search Complaint
4. Update Complaint Status
5. Generate Complaint Report
6. Exit

Enter your choice: 3

========== SEARCH COMPLAINT ==========
1. Search by Complaint ID
2. Search by Location
3. Search by Problem Type
Enter choice: 1
Enter Complaint ID: 1006

========== SEARCH RESULTS ==========

Complaint ID: 1006
Name: Mayank
Location: Ghaziabaad
Problem: Garbage
Description: Lack of dustbins .
Status: Pending
--------------------------------

======================================
       CIVIC REPORTING SYSTEM
======================================
1. Report a Complaint
2. View All Complaints
3. Search Complaint
4. Update Complaint Status
5. Generate Complaint Report
6. Exit

Enter your choice: 4
Enter Complaint ID: 1006

Current Status: Pending

Select New Status:
1. Pending
2. In Progress
3. Resolved
Enter choice: 3

Complaint status updated successfully!
======================================
       CIVIC REPORTING SYSTEM
======================================
1. Report a Complaint
2. View All Complaints
3. Search Complaint
4. Update Complaint Status
5. Generate Complaint Report
6. Exit

Enter your choice: 5

========== CIVIC REPORT ==========

Total Complaints: 8
Pending: 5
In Progress: 0
Resolved: 3

Problem-wise Statistics:
Pothole : 1
Garbage : 2
Water Leakage : 2
Damaged Road : 2
Streetlight : 1

======================================
       CIVIC REPORTING SYSTEM
======================================
1. Report a Complaint
2. View All Complaints
3. Search Complaint
4. Update Complaint Status
5. Generate Complaint Report
6. Exit

Enter your choice: 6

Thank you for using Civic Reporting System!
PS C:\Users\sarla\Downloads\Civic Reporting System> 


12. Future Enhancements

- Web-based interface
- User login and authentication
- Photo upload for complaints
- GPS-based location
- Email/SMS notifications
- Database such as MySQL
- Administrator dashboard
- Online deployment
