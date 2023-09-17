from distutils.log import debug
from fileinput import filename
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

sample_data = [
    ["6:00 AM - 6:50 AM", "", "", "", "", "", "", ""],
    ["7:00 AM - 7:50 AM", "", "", "", "Krupal", "", "", ""],
    ["8:00 AM - 8:50 AM", "", "", "", "", "", "", ""],
    ["9:00 AM - 9:50 AM", "", "", "", "", "", "", ""],
    ["10:00 AM - 10:50 AM", "", "", "", "", "", "", ""],
    ["11:00 AM - 11:50 AM", "", "", "", "", "", "", ""],
    ["12:00 PM - 12:50 PM", "", "", "", "", "", "", ""],
    ["1:00 PM - 1:50 PM", "", "", "", "", "", "", ""],
    ["2:00 PM - 2:50 PM", "", "", "", "HELLO", "", "", ""],
    ["3:00 PM - 3:50 PM", "", "", "", "", "", "", ""],
    ["4:00 PM - 4:50 PM", "", "", "", "", "", "", ""],
    ["5:00 PM - 5:50 PM", "", "", "", "", "", "", ""],
    ["6:00 PM - 6:50 PM", "", "", "", "", "", "", ""],
    ["7:00 PM - 7:50 PM", "", "", "", "", "", "", ""],
    ["8:00 PM - 8:50 PM", "", "", "", "", "", "", ""],
    ["9:00 PM - 9:50 PM", "", "", "", "", "", "", ""],
    ["10:00 PM - 10:50 PM", "", "", "", "", "", "", ""],
    ["11:00 PM - 11:50 PM", "", "", "", "", "", "", ""]
]

@app.route("/")
@app.route("/index.html", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/schedule.html", methods=["GET"])
def handle_start():
    return render_template("schedule.html")

@app.route("/success", methods=["POST"])
def handle_success():
    if request.method == "POST":
        f = request.files["file"]
        f.save(f.filename)
        return redirect(url_for("handle_schedule"))
    
@app.route("/result.html", methods=["GET"])
def handle_schedule():
    flaskName = request.values.get("name")
    return render_template("result.html", flaskName=flaskName, data = sample_data)

if __name__ == "__main__":
    app.run(debug=True)
