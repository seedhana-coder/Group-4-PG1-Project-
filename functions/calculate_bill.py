BASE_CONSULTATION_FEE = 100
LAB_TEST_RATE = 10
SUBSIDISED_DISCOUNT = 0.30


def billing():
    print("\n===== Calculate Bill =====")

    # Choose patient type
    while True:
        patient_type = input(
            "Enter patient type (Subsidised/Private): "
        ).strip().lower()

        if patient_type == "subsidised":
            patient_type_name = "Subsidised"
            break

        elif patient_type == "private":
            patient_type_name = "Private"
            break

        else:
            print("Error: Please enter Subsidised or Private.")

    # Get number of lab tests
    while True:
        lab_input = input("Enter number of lab tests completed: ")

        try:
            lab_tests = int(lab_input)

            if lab_tests >= 0:
                break

            print("Error: Number of lab tests cannot be negative.")

        except ValueError:
            print("Error: Please enter a whole number.")

    # Calculate subtotal
    subtotal = BASE_CONSULTATION_FEE + (lab_tests * LAB_TEST_RATE)

    # Calculate final total
    if patient_type == "subsidised":
        total = subtotal * (1 - SUBSIDISED_DISCOUNT)
    else:
        total = subtotal

    # Display bill
    print("\n===== Bill Summary =====")
    print("Patient Type:", patient_type_name)
    print("Base Consultation Fee: $", format(BASE_CONSULTATION_FEE, ".2f"))
    print("Number of Lab Tests:", lab_tests)
    print("Lab Test Rate: $", format(LAB_TEST_RATE, ".2f"))
    print("Subtotal: $", format(subtotal, ".2f"))
    print("Total Amount to Pay: $", format(total, ".2f"))
