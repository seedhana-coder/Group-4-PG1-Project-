def main():
    while True:
        print("\n===== Hospital Management System =====")
        print("1. Patient Registration")
        print("2. Book Appointment")
        print("3. Billing")
        print("4. Assign Triage Room")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            patient_registration()
        elif choice == "2":
            book_appointment()
        elif choice == "3":
            billing()
        elif choice == "4":
            assign_triage()
        elif choice == "5":
            print("Thank you for using the Hospital Management System.")
            break
        else:
            print("Invalid choice.")

        input("\nPress Enter to return to the Main Menu...")


main()
