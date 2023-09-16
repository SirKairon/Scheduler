class Event:
    def __init__(self,name, start_time=-1, endtime = -1) -> None:
        self.name = name
        self.start_time = start_time;
        self.end_time = endtime
    def set_start_time(self,start_time):
        self.start_time = start_time

    def set_end_time(self,end_time):
        self.end_time = end_time
    
    def get_start_time(self):
        return self.start_time
    def get_end_time(self):
        return self.get_end_time
    def get_name(self):
        return self.name
    def __str__(self) -> str:   
        return self.name + " " + str(self.start_time) + " " + str(self.end_time)

# making a time table object with start and end time of each event and name of the event
class TimeTable:
    def __init__(self,events) -> None:
        self.days= {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
        self.timetable = []# list of lists
        self.events = events
    def make_time_table(self):

        return time_table
    def get_time_table(self):
        return self.time_table
    def __str__(self) -> str:
        return str(self.time_table)


    
