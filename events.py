from ics import Calendar, Event as iCalEvent
from datetime import datetime, timedelta




class event:
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
event1 = Event("Meeting", start_time=9, end_time=11, day=0)
event2 = Event("Lunch", start_time=12, end_time=13, day=1)

events = [event1, event2]

timetable = Timetable(events)
ical_data = timetable.to_ics()
print(ical_data)
with open("timetable.ics", "w") as ics_file:
    ics_file.writelines(ical_data)





