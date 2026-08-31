from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()
        patient_id = request.form.get("patient_id", "").strip()

        # Validate name
        if not name:
            return "Error: Name cannot be blank. Please try again."

        # Validate age
        try:
            age = int(age)

            if age <= 0:
                return "Error: Age must be a positive number. Please try again."

        except ValueError:
            return "Error: Age must be a valid number. Please try again."

        # Validate patient ID
        if not patient_id:
            return "Error: Patient ID cannot be blank. Please try again."

        # Successful registration
        return f"""
        <h1>Patient Registered Successfully!</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Age:</strong> {age}</p>
        <p><strong>Patient ID:</strong> {patient_id}</p>
        <p>Patient information has been recorded successfully.</p>
        """

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
