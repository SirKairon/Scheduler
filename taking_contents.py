from datetime import datetime
from events import Event, Timetable

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

if __name__ == "__main__":
    path = "test.ics"  # Assuming you have a "test.ics" file in the same folder

    with open(path) as f:
        parser = ParseICS(f.read())
        parser.parse()

    print(Timetable)
