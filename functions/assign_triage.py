def assign_triage():
    print("\n===== Assign Triage Room =====")

    # Get and validate severity
    while True:
        severity_input = input(
            "Enter severity of condition (1-10): "
        )

        try:
            severity = int(severity_input)

            if 1 <= severity <= 10:
                break

            print("Error: Severity must be between 1 and 10.")

        except ValueError:
            print("Error: Severity must be a whole number.")

    # Assign room
    if 1 <= severity <= 4:
        room = "Waiting Room"

    elif 5 <= severity <= 7:
        room = "Room 1"

    else:
        room = "Room 2"

    # Display summary
    print("\n===== Triage Summary =====")
    print("Severity Level:", severity)
    print("Assigned Room:", room)

    print("\nTriage assignment completed successfully!")
