# import statements
import events.py as Events
#inputing the primary tasks
pt = str(input("Do you have an exsisting schedule (y/n)"))
# primary tasks (name day start and end time)
# secondary tasks ( type ( daily or weekly or by x day))
Timetable = Events.Timetable()
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


pt3 = str(input('Do you have any secondary tasks?(y/n)'))
if pt3 == 'y':
    condition = True
    while condition == True:
        name = str(input('What is the name of the task?'))
        type = str(input('Is the task daily, weekly or by x day?'))
        if type == 'daily':
            Events.event(name, start_time, end_time, day)
        elif type == 'weekly':
            Events.event(name, start_time, end_time, day)
        elif type == 'by x day':
            Events.event(name, start_time, end_time, day)
        else:
            print('invalid input')
        condition = str(input('Do you have any more secondary tasks?(y/n)'))
        if condition == 'n':
            condition = False
    
