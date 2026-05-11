from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        previous_marks = float(request.form["previous_marks"])

        features = np.array([[study_hours, attendance, previous_marks]])

        result = model.predict(features)[0]

        if result == 1:
            prediction = "Student is likely to PASS"
        else:
            prediction = "Student is likely to FAIL"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)