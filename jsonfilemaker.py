import json
file = "timetable.json" 
def jsonfileinput(timetable, file ):
    with open("timetable.json", "w") as outfile:
        for day in timetable:
            json_object = json.dump(day,outfile)
    return file