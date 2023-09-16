import datetime  
from datetime import date 
from datetime import datetime, timedelta, timezone
import icalendar
from dateutil.rrule import *

def extrat_file():
    icalfile = open('sample.ics', 'rb')
    gcal = icalendar.Calendar.from_ical(icalfile.read())
    for component in gcal.walk():
        if component.name == "VEVENT":
            summary = component.get('summary')
            startdt = component.get('dtstart').dt
            enddt = component.get('dtend').dt
        startdt = startdt.strftime("%D %H:%M UTC")
        enddt = enddt.strftime("%D %H:%M UTC")
        

        start = split(" ", startdt)
        start_date = split("/", start[0])
        start_day_name = datetime.date(int(start_date[2]), int(start_date[1]), int(start_date[0]))
        start_time = start[1]

        end = split(" ", enddt)
        end_date = split("/", end[0])
        start_day_name = datetime.date(int(end_date[2]), int(end_date[1]), int(end_date[0]))
        end_time = end[1]
