from flask import Flask, render_template, request, flash, redirect, url_for
import os
import events_updates as e
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

sample_data = [
    ["6:00 AM - 6:50 AM", "", "", "", "", "", "", ""],
    ["7:00 AM - 7:50 AM", "", "", "", "", "", "", ""],
    ["8:00 AM - 8:50 AM", "", "", "", "", "", "", ""],
    ["9:00 AM - 9:50 AM", "", "", "", "", "", "", ""],
    ["10:00 AM - 10:50 AM", "", "", "", "", "", "", ""],
    ["11:00 AM - 11:50 AM", "", "", "", "", "", "", ""],
    ["12:00 PM - 12:50 PM", "", "", "", "", "", "", ""],
    ["1:00 PM - 1:50 PM", "", "", "", "", "", "", ""],
    ["2:00 PM - 2:50 PM", "", "", "", "", "", "", ""],  
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

@app.route("/#change", methods=['GET'])
def changeButton():
    return render_template("schedule.html")
    
@app.route("/upload", methods=["POST"])
def handle_success():
    path = os.getcwd()
    UPLOAD_FOLDER = os.path.join(path, 'uploads')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == "POST":
        f = request.files["file"]
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return render_template("tasks.html")

@app.route("/generate", methods=["GET"])
def handle_process():

        object_cookie = request.cookies.get('task')
        data = json.loads(object_cookie)
        generateData(data)
        return render_template("result.html", flaskName=data['userName'], data = sample_data)

@app.route("/about.html", methods=["GET"])
def handle_about():
    return render_template("about.html")

@app.route("/tasks.html", methods=["GET"])
def handle_task():
    return render_template("tasks.html")

def generateData(data):
    # creating timeTable object
    tTable = e.Timetable()

    if (data["hasIcs"] == "yes"):
        # Parsing and storing data from ics in timetable
        with open(f'uploads\{os.listdir(f"uploads")[0]}') as f:
            e.ParseICS(f.read()).parse(tTable)

    # Adding primary tasks and secondary Tasks to timetable
    for i in range(0, len(data['primaryTasks'])):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        title = list(data['primaryTasks'].keys())[i]
        s_time = int(data['primaryTasks'][title]["start_time"])
        e_time = int(data['primaryTasks'][title]["end_time"])
        day = days.index(data['primaryTasks'][title]["day"])

        pT = e.Event(title, s_time, e_time, day)
        tTable.add_event(pT)
    
    for i in range(0, len(data['secondaryTasks'])):
        title = list(data['secondaryTasks'].keys())[i]
        s_time = int(data['secondaryTasks'][title]["time"])
        S_day = days.index(data['secondaryTasks'][title]["day"])
        S_hours = int(data['secondaryTasks'][title]["hours"])

        sT = e.Event(name=title, start_time=s_time, day=S_day, hours=S_hours)
        tTable.random_assign(sT)
    
    for i in range(7):
        print(tTable.get_events(i))
        for j in range(18):
            if (tTable.timetable[i][j] != []):
                sample_data[j][i+1] = tTable.timetable[i][j]
    tTable.delete()
    
    return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)


