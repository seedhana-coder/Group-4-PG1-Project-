document.addEventListener("DOMContentLoaded", function () {

    // Mobile menu
    const menuButton = document.getElementById("menuButton");
    const navMenu = document.getElementById("navMenu");

    if (menuButton && navMenu) {
        menuButton.addEventListener("click", function () {
            navMenu.classList.toggle("show");
        });
    }


    // Patient registration form
    const patientForm = document.getElementById("patientForm");

    if (patientForm) {
        patientForm.addEventListener("submit", function (event) {

            const name = document.getElementById("patientName").value.trim();
            const age = document.getElementById("patientAge").value;
            const patientId = document.getElementById("patientId").value.trim();

            if (name === "") {
                alert("Please enter the patient's name.");
                event.preventDefault();
                return;
            }

            if (age === "" || Number(age) <= 0) {
                alert("Please enter a valid positive age.");
                event.preventDefault();
                return;
            }

            if (patientId === "") {
                alert("Please enter the patient ID.");
                event.preventDefault();
                return;
            }

            alert("Patient information is valid!");
        });
    }


    // Appointment form
    const appointmentForm = document.getElementById("appointmentForm");

    if (appointmentForm) {
        appointmentForm.addEventListener("submit", function (event) {

            const department =
                document.getElementById("department").value;

            const appointmentDate =
                document.getElementById("appointmentDate").value;

            if (department === "") {
                alert("Please select a department.");
                event.preventDefault();
                return;
            }

            if (appointmentDate === "") {
                alert("Please select an appointment date.");
                event.preventDefault();
                return;
            }

            alert("Appointment information is valid!");
        });
    }


    // Billing calculation
    const calculateButton =
        document.getElementById("calculateBill");

    if (calculateButton) {
        calculateButton.addEventListener("click", function () {

            const patientType =
                document.getElementById("patientType").value;

            const labTests =
                Number(document.getElementById("labTests").value);

            if (patientType === "") {
                alert("Please select the patient type.");
                return;
            }

            if (isNaN(labTests) || labTests < 0) {
                alert("Please enter a valid number of lab tests.");
                return;
            }

            const baseFee = 100;
            const labRate = 10;

            let subtotal = baseFee + (labTests * labRate);
            let total = subtotal;

            if (patientType === "Subsidised") {
                total = subtotal * 0.70;
            }

            document.getElementById("billResult").innerHTML =
                "Total Amount: $" + total.toFixed(2);
        });
    }


    // Triage room assignment
    const triageButton =
        document.getElementById("assignTriage");

    if (triageButton) {
        triageButton.addEventListener("click", function () {

            const severity =
                Number(document.getElementById("severity").value);

            if (!Number.isInteger(severity) ||
                severity < 1 ||
                severity > 10) {

                alert("Severity must be a whole number from 1 to 10.");
                return;
            }

            let room;

            if (severity >= 1 && severity <= 4) {
                room = "Waiting Room";
            }
            else if (severity >= 5 && severity <= 7) {
                room = "Room 1";
            }
            else {
                room = "Room 2";
            }

            document.getElementById("triageResult").innerHTML =
                "Severity: " + severity +
                "<br>Assigned Room: " + room;
        });
    }

});
