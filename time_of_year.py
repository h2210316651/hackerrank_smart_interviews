import datetime
import calendar
def class1():
    a=[]
    b=''
    timestamp =int(input())
    value = datetime.datetime.fromtimestamp(timestamp)
    my_date = value
    day=calendar.day_name[my_date.weekday()]
    a.append(value.strftime('%d-%m-%Y')+" "+day)
    for i in a:
        lis=i.split('-')
        lis[1]=calendar.month_name[int(lis[1])]
        lis[1]=lis[1][0:3]
        lis[1]=lis[1].upper()
    for i in range(len(lis)-1):
        b=b+str(lis[i])+'-'
    b=b+lis[len(lis)-1]
    return b
t=int(input())
ap=[]
for i in range(t):
    ap.append(class1())
for i in range(t):
    print(ap[i])
