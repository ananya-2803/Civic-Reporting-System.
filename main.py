from complaint import report_complaint
from admin import view_complaints, update_status
from search import search_complaint
from report import generate_report


def main():

    while True:

        print("\n")
        print("======================================")
        print("       CIVIC REPORTING SYSTEM")
        print("======================================")

        print("1. Report a Complaint")
        print("2. View All Complaints")
        print("3. Search Complaint")
        print("4. Update Complaint Status")
        print("5. Generate Complaint Report")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            report_complaint()

        elif choice == "2":
            view_complaints()

        elif choice == "3":
            search_complaint()

        elif choice == "4":
            update_status()

        elif choice == "5":
            generate_report()

        elif choice == "6":
            print("\nThank you for using Civic Reporting System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()