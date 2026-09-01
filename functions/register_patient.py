def patient_registration():
    print("\n===== Patient Registration =====")

    # Get and validate patient name
    while True:
        name = input("Enter patient name: ").strip()

        if name != "":
            break

        print("Error: Name cannot be blank. Please try again.")

    # Get and validate patient age
    while True:
        age_input = input("Enter patient age: ")

        try:
            age = int(age_input)

            if age > 0:
                break
            else:
                print("Error: Age must be a positive number.")

        except ValueError:
            print("Error: Age must be a whole number.")

    # Get and validate patient ID
    while True:
        patient_id = input("Enter patient ID: ").strip()

        if patient_id != "":
            break

        print("Error: Patient ID cannot be blank.")

    # Display confirmation
    print("\n===== Patient Information =====")
    print("Name:", name)
    print("Age:", age)
    print("Patient ID:", patient_id)

    print("\nPatient registered successfully!")
