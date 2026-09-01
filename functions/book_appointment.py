from datetime import datetime, date, timedelta


def book_appointment():
    print("\n===== Book Appointment =====")

    # Choose department
    while True:
        department = input("Enter department (GP/Specialist): ").strip().lower()

        if department == "gp":
            department_name = "GP"
            break

        elif department == "specialist":
            department_name = "Specialist"
            break

        else:
            print("Error: Please enter GP or Specialist.")

    # Enter appointment date
    while True:
        date_input = input("Enter appointment date (DD/MM/YYYY): ").strip()

        try:
            appointment_date = datetime.strptime(
                date_input, "%d/%m/%Y"
            ).date()

            today = date.today()
            maximum_date = today + timedelta(days=7)

            if today <= appointment_date <= maximum_date:
                break

            print("Error: Appointment date must be within the next 7 days.")

        except ValueError:
            print("Error: Please enter the date in DD/MM/YYYY format.")

    # Confirmation
    print("\n===== Appointment Confirmation =====")
    print("Department:", department_name)
    print("Appointment Date:", appointment_date.strftime("%d/%m/%Y"))

    print("\nAppointment booked successfully!")
