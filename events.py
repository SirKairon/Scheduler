#from ics import Calendar, Event as iCalEvent
from datetime import datetime, timedelta
import random
import json
import datetime  
from datetime import date 
from datetime import datetime, timedelta, timezone
# import icalendar
from dateutil.rrule import *

def jsonfileinput(timetable ):
    file = "timetable.json" 
    with open(file, "w") as outfile:
        for day in timetable:
            json_object = json.dump(day,outfile)
    return file



# def extrat_file():
#     icalfile = open('sample.ics', 'rb')
#     gcal = icalendar.Calendar.from_ical(icalfile.read())
#     for component in gcal.walk():
#         if component.name == "VEVENT":
#             summary = component.get('summary')
#             startdt = component.get('dtstart').dt
#             enddt = component.get('dtend').dt
#         startdt = startdt.strftime("%D %H:%M UTC")
#         enddt = enddt.strftime("%D %H:%M UTC")
        

#         start = startdt.split(" " )
#         start_date =start[0].split("/")
#         start_day_name = datetime.date(int(start_date[2]), int(start_date[1]), int(start_date[0]))
#         start_time = start[1].split(":")
#         start_time = start_time[0]
#         end = enddt.split(" ")
#         end_date = end[0].split("/")
#         start_day_name = datetime.date(int(end_date[2]), int(end_date[1]), int(end_date[0]))
#         end_time = end[1].split(":")
#         if end_time[1] != "00":
#             end_time = str(int(end_time[0])+1)        

class Event:
    def __init__(self, name, start_time=-1, end_time=-1, day=-1):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.day = day

    def set_day(self, day):
        self.day = day

    def get_day(self):
        return self.day

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name + " " + str(self.start_time) + " " + str(self.end_time)


class Timetable:
    def __init__(self):
        self.timetable = [[[] for _ in range(24)] for _ in range(7)]
    def random_assign(self, secondary_event,hours):
        day = secondary_event.get_day()
        if day==-1:
            day = random.randint(0, 6)
        start_time = random.randint(0, 24-hours)
        end_time = start_time + hours
        secondary_event.set_day(day)
        secondary_event.set_start_time(start_time)
        secondary_event.set_end_time(end_time)
        while True:
            if self.check_availability(secondary_event):
                break
            else:
                day = random.randint(0, 6)
                start_time = random.randint(0, 24-hours)
                end_time = start_time + hours
                secondary_event.set_day(day)
                secondary_event.set_start_time(start_time)
                secondary_event.set_end_time(end_time)
        self.add_event(secondary_event)

    def check_availability(self, event):
        for i in range(event.start_time, event.end_time):
            if self.timetable[event.day][i]:
                return False
        return True
    
    def add_event(self, event):
        if 0 <= event.day < 7 and 0 <= event.start_time <= event.end_time < 24:
            for i in range(event.start_time, event.end_time):
                self.timetable[event.day][i].append(event)
        else:
            print("Invalid event: ", event)
    def add_events(self, events):
        for event in events:
            self.add_event(event)

    def get_events(self, day, time):
        return self.timetable[day][time]

    def __str__(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        string = ""

        for day_index, day in enumerate(days):
            string += f"{day}:\n"
            for hour in range(24):
                events = self.timetable[day_index][hour]
                if events:
                    event_strings = [event.get_name() for event in events]
                    string += f"  {hour:02d}:00 - {hour + 1:02d}:00: {', '.join(event_strings)}\n"

        return string
    
    # def to_ics(self):
    #     cal = Calendar()

    #     for day_index, day in enumerate(range(7)):
    #         for hour in range(24):
    #             events = self.get_events(day_index, hour)
    #             for event in events:
    #                 start_time = datetime(2023, 1, day_index + 2, hour)  # Assuming January 2, 2023 is a Monday
    #                 end_time = start_time + timedelta(hours=1)

    #                 ics_event = iCalEvent()
    #                 ics_event.name = event.get_name()
    #                 ics_event.begin = start_time
    #                 ics_event.end = end_time

    #                 cal.events.add(ics_event)

    #     return cal

# Example usage:
# event1 = Event("Meeting", start_time=9, end_time=11, day=0)
# event2 = Event("Lunch", start_time=12, end_time=13, day=1)

# events = [event1, event2]

# timetable = Timetable()
# timetable.add_events(events)
# print(timetable)

# ical_data = timetable.to_ics()
# print(ical_data)
# with open("timetable.ics", "w") as ics_file:
#     ics_file.writelines(ical_data)
