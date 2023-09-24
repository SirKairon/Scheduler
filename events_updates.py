#from ics import Calendar, Event as iCalEvent
from datetime import datetime, timedelta
import random
import json
import datetime  
from datetime import date 
from datetime import datetime, timedelta, timezone
from ics import Calendar, Event as iCalEvent
import icalendar
from dateutil.rrule import *

def jsonfileinput(timetable ):
    file = "timetable.json" 
    with open(file, "w") as outfile:
        for day in timetable:
            json_object = json.dump(day,outfile)
    return file

# # Set the path to your credentials JSON file
# credentials_file = 'path/to/your/credentials.json'

# # Define the calendar ID (usually your email address)
# calendar_id = 'your.email@gmail.com'

# # Authenticate using the credentials file
# credentials = service_account.Credentials.from_service_account_file(
#     credentials_file, scopes=['https://www.googleapis.com/auth/calendar']
# )

# # Build the Calendar API service
# service = build('calendar', 'v3', credentials=credentials)

# # Create a new event
# event = {
#     'summary': 'Your Event Summary',
#     'description': 'Event Description',
#     'start': {'dateTime': '2023-12-31T10:00:00'},
#     'end': {'dateTime': '2023-12-31T12:00:00'},
# }

# Add the event to the calendar
# event = service.events().insert(calendarId=calendar_id, body=event).execute()

# Print the event details
# print(f'Event created: {event.get("htmlLink")}')

# To convert json to 
class ParseICS:
    def __init__(self, icsFile: str) -> None:
        assert icsFile is not None
        self.__file = icsFile.splitlines()
        assert len(self.__file) > 23
        self.__file = self.__file[23:]

    def __str_to_date(self, date_str: str) -> datetime:
        print(datetime.strptime(date_str, "%Y%m%dT%H%M%S"))
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
                location = ""
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
                t = Timetable()
                print(dtStart, dtEnd, summary, days)
                if not days:
                    days = ["SU", "MO", "TU", "WE", "TH", "FR", "SA"]
                for day in days:
                    event = Event(summary, dtStart, dtEnd, days.index(day))
                    t.add_event(event)

        return t

# if __name__ == "__main__":
#     path = "test.ics"  # Assuming you have a "test.ics" file in the same folder

#     with open(path) as f:
#         parser = ParseICS(f.read())
#         parser.parse()
class Event:
    def __init__(self, name, start_time=-1, end_time=-1, day=-1, hours=0):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.day = day
        self.hours = hours

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
    def random_assign(self, se):
        day = se.get_day()
        if day==-1:
            day = random.randint(0, 6)
        start_time = random.randint(0, 24-se.hours)
        end_time = start_time + se.hours
        se.set_day(day)
        se.set_start_time(start_time)
        se.set_end_time(end_time)
        while True:
            if self.check_availability(se):
                break
            else:
                day = random.randint(0, 6)
                start_time = random.randint(0, 24-se.hours)
                end_time = start_time + se.hours
                se.set_day(day)
                se.set_start_time(start_time)
                se.set_end_time(end_time)
        self.add_event(se)

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
    
    def to_ics(self):
        cal = Calendar()

        for day_index, day in enumerate(range(7)):
            for hour in range(24):
                events = self.get_events(day_index, hour)
                for event in events:
                    start_time = datetime(2023, 1, day_index + 2, hour)  # Assuming January 2, 2023 is a Monday
                    end_time = start_time + timedelta(hours=1)

                    ics_event = iCalEvent()
                    ics_event.name = event.get_name()
                    ics_event.begin = start_time
                    ics_event.end = end_time

                    cal.events.add(ics_event)

        return cal

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
