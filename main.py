# import statements
from events import Event, Timetable
from jsonfilemaker import jsonfileinput
#inputing the primary tasks
pt = str(input("Do you have an exsisting schedule (y/n)"))


Timetable = Timetable()
# primary tasks (name day start and end time)
if  pt == "y":
    print('upload your schedule')
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
