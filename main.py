# import statements
import events.py as Events
#inputing the primary tasks
pt = str(input("Do you have an exsisting schedule (y/n)"))


Timetable = Events.Timetable()
# primary tasks (name day start and end time)
if  pt == "y":
    print('upload your schedule')
else:
    pt2 = str(input('Do you have any primary tasks?(y/n)'))
    if pt2='y':
        condition = True
        events_list=[]
        while condition==True:
            name = str(input('What is the name of the task?'))
            day = str(input('What day is the task on?'))
            days = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
            start_time = str(input('What time does the task start?(as hhmm)'))
            end_time = str(input('What time does the task end?(as hhmm)'))
            Events.event(name, start_time, end_time, day)
            events_list.append(event)
            condition = str(input('Do you have any more primary tasks?(y/n)'))
            if condition == 'n':
                condition = False

# secondary tasks ( type ( daily or weekly or by x day))
pt3 = str(input('Do you have any secondary tasks?(y/n)'))
if pt3 == 'y':
    condition = True
    while condition == True:
        name = str(input('What is the name of the task?'))
        type = str(input('Is the task "daily", "weekly" or "by x day"?'))
        if type == 'daily':
            num = int(input('How many hours a day do you want to spend on this task?'))
            for i in range(7):
                day = i
                event = Events.event(name, day = day)
                Events.random_assigner(event, num)
        elif type == 'weekly':
            num = int(input('How many hours a day do you want to spend on this task?'))
            day = str(input('What day do you want to do this task on?'))
            day = days[day]
            event = Events.event(name, day = day)
            Events.random_assigner(event, num)
        elif type == 'by x day':
            num = int(input('How many hours a day do you want to spend on this task?'))
            day = str(input('What day do you want to do this task on?'))
            day = days[day]
            Events.random_assigner(name, num, day)
        else:
            print('invalid input')
        condition = str(input('Do you have any more secondary tasks?(y/n)'))
        if condition == 'n':
            condition = False
    
