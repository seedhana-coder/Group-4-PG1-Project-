from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

# ==========================
# Home Page
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Patient Registration
# ==========================
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        patient_name = request.form["patient_name"].strip()
        patient_age = request.form["patient_age"].strip()
        patient_id = request.form["patient_id"].strip()

        if patient_name == "":
            return render_template(
                "register.html",
                error="Patient name cannot be blank."
            )

        try:
            patient_age = int(patient_age)

            if patient_age <= 0:
                return render_template(
                    "register.html",
                    error="Age must be a positive number."
                )

        except ValueError:
            return render_template(
                "register.html",
                error="Please enter a valid age."
            )

        if patient_id == "":
            return render_template(
                "register.html",
                error="Patient ID cannot be blank."
            )

        return render_template(
            "success.html",
            title="Registration Successful",
            message="Patient registered successfully!"
        )

    return render_template("register.html")


# ==========================
# Appointment Booking
# ==========================
@app.route("/appointment", methods=["GET", "POST"])
def appointment():

    if request.method == "POST":

        patient_name = request.form["patient_name"].strip()
        appointment_date = request.form["appointment_date"]
        appointment_type = request.form["appointment_type"]

        booking_date = datetime.strptime(
            appointment_date,
            "%Y-%m-%d"
        ).date()

        today = datetime.today().date()

        # Must be at least 5 days in advance
        if booking_date < today + timedelta(days=5):
            return render_template(
                "appointment.html",
                error="Appointments must be booked at least 5 days in advance."
            )

        return render_template(
            "success.html",
            title="Appointment Booked",
            message=f"{appointment_type} appointment booked successfully for {patient_name} on {booking_date}."
        )

    return render_template("appointment.html")


# ==========================
# Billing
# ==========================
@app.route("/billing", methods=["GET", "POST"])
def billing():

    if request.method == "POST":

        patient_type = request.form["patient_type"]
        lab_test = request.form["lab_test"]

        total = 100

        if lab_test == "Yes":

            try:
                num_tests = int(request.form["num_tests"])

                if num_tests <= 0:
                    return render_template(
                        "billing.html",
                        error="Enter a valid number of lab tests."
                    )

                total += num_tests * 10

            except ValueError:
                return render_template(
                    "billing.html",
                    error="Please enter a whole number."
                )

        if patient_type == "Subsidised":
            total *= 0.7

        return render_template(
            "success.html",
            title="Billing Complete",
            message=f"Total Amount: ${total:.2f}"
        )

    return render_template("billing.html")


# ==========================
# Triage
# ==========================
@app.route("/triage", methods=["GET", "POST"])
def triage():

    if request.method == "POST":

        try:
            severity = int(request.form["severity"])

            if severity < 1 or severity > 10:
                return render_template(
                    "triage.html",
                    error="Severity must be between 1 and 10."
                )

        except ValueError:
            return render_template(
                "triage.html",
                error="Please enter a valid number."
            )

        if severity <= 4:
            room = "Waiting Room"

        elif severity <= 7:
            room = "Room 1"

        else:
            room = "Room 2"

        return render_template(
            "success.html",
            title="Triage Complete",
            message=f"Assigned Room: {room}"
        )

    return render_template("triage.html")


# ==========================
# Run Flask
# ==========================
if __name__ == "__main__":
    app.run(debug=True)