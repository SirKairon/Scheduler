# import statements
from events import Event, Timetable
from jsonfilemaker import jsonfileinput
from datetime import datetime
#inputing the primary tasks
pt = str(input("Do you have an exsisting schedule (y/n)"))


timetable = Timetable()
# primary tasks (name day start and end time)
class ParseICS:
    def __init__(self, icsFile: str) -> None:
        assert icsFile is not None
        self.__file = icsFile.splitlines()

    def __str_to_date(self, date_str: str) :
        return datetime.strptime(date_str, "%Y%m%dT%H%M%S")

    def parse(self):
        dtStart = None
        summary = ""
        dtEnd = None
        day = ""

        for line in self.__file:
            line = line.strip()

            if line == "BEGIN:VEVENT":
                dtStart = None
                summary = ""
                dtEnd = None
                day = ''
            elif "DTSTART" in line:
                # Format -> Canada/Mountain:20220902T140000
                starting = line.index("=") + 1
                dtStart = int(line[starting + 25:starting + 27])
                
            elif "SUMMARY" in line:
                starting = line.index(":") + 1
                summary = line[starting:]
            elif "DTEND" in line:
                starting = line.index("=") + 1
                dtEnd = int(line[starting + 25:starting + 27])
            elif "RRULE" in line:
                # format FREQ=WEEKLY;INTERVAL=1;UNTIL=20231208T235959Z;BYDAY=MO,WE,FR;WKST=SU
                days = line.split(";")[3]
                days = days.split(",")
                days = [day[6:] for day in days]  # Extract the day abbreviations

            elif line == "END:VEVENT":
                # Create the event and add it to the timetable
                if not days:
                    days = ["SU", "MO", "TU", "WE", "TH", "FR", "SA"]
                for day in days:
                    event = Event(summary, dtStart, dtEnd, days.index(day))
                    timetable.add_event(event)

        return timetable
    
if  True:
    print('upload your schedule')
    path = str(input('What is the name of your schedule?'))
    path = "demo.ics"
    with open(path) as f:
        parser = ParseICS(f.read())
        Timetable = parser.parse()
    
pt2 = str(input('Do you have any primary tasks?(y/n)'))
if pt2=='y':
    condition = 'y'
    events_list=[]
    while (condition=='y'):
        name = str(input('What is the name of the task?'))
        day = str(input('What day is the task on?'))
        days = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5,"Sunday": 6}
        start_time = int(input('What time does the task start?(as hh)'))
        end_time = int(input('What time does the task end?(as hh)'))
        day = days[day]
        event = Event(name, start_time, end_time, day)
        events_list.append(event)
        condition = str(input('Do you have any more primary tasks?(y/n)'))
    Timetable.add_events(events_list)
# secondary tasks ( type ( daily or weekly or by x day))
events_list=[]
pt3 = str(input('Do you have any secondary tasks?(y/n)'))
if pt3 == 'y':
    condition = 'y'
    while condition == 'y':
        name = str(input('What is the name of the task?'))
        type = str(input('Is the task "daily" or "weekly" ?'))
        if type == 'daily':
            num = int(input('How many hours a day do you want to spend on this task?'))
            for i in range(7):
                day = i
                event = Event(name, day = day)
                Timetable.random_assign(event, num)
        elif type == 'weekly':
            num = int(input('How many hours a day do you want to spend on this task?'))
            day = str(input('What day do you want to do this task on?'))
            day = days[day]
            event = Event(name, day = day)
            Timetable.random_assign(event, num)
        else:
            print('invalid input')
        condition = str(input('Do you have any more secondary tasks?(y/n)'))
    
Timetable.add_events(events_list)
print (Timetable)

# converting the timetable to json
#jsonfileinput(Timetable.timetable, "timetable.json")
