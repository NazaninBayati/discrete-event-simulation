import random
import numpy
from colorama import Fore


def SetClock(a , b):
     res = 0.0
     if a<b : res = a
     elif a == b : res = b
     else: res = b
     return res


def SetClock_zero(a, b):
    res = 0.0
    if a < b:
        res = b
    elif a == b:
        res = b
    else:
        res = a
    return res


import random




random.seed(10)
def random_generation_A():
    r = random.random()
    r = numpy.log(r)

    return round((-r / 1.0),2)

def random_generation_B():

    r1 = random.random()
    r1 = numpy.log(r1)

    return round((-r1 / 1.2), 2)

def bprint(sentence,val):
    p = [None,None]
    p[0]=sentence
    p[1]=val
    return print(Fore.BLUE+p[0], p[1])

def pprint(sentence,val):
    p = [None,None]
    p[0]=sentence
    p[1]=val
    return print(Fore.LIGHTMAGENTA_EX+p[0], p[1])

def gprint(sentence,val):
    p = [None,None]
    p[0]=sentence
    p[1]=val
    return print(Fore.LIGHTCYAN_EX+p[0], p[1])

def yprint(sentence,val):
    p = [None,None]
    p[0]=sentence
    p[1]=val
    return print(Fore.YELLOW+p[0], p[1])


deadline = 1
Ea=0.0
Es=0.0

   # A = random_generation(Landa)
    #S = random_generation(M)
A = random_generation_A()
Ea = Ea+A




deadline = int(input("please enter number of iteration: "))
if deadline < 1:
        print(Fore.RED + "WRONG NUMBER!!!!!!!!!!")
        deadline = 1



#use random function
Queue=0
NumberService=0
NumberProcess=0
busy=0
clock=0.0
Area_under_B=0.0
Area_under_Q=0.0
last_clock=0.0
last_clock1=0.0
pprint("clock: ", clock)
bprint("numberservice: ", NumberService)
yprint("Queue: ", Queue)
print(Fore.LIGHTCYAN_EX,"eventlist: [",A,", ~]")
eventList=[0.0,10000.1]
i=0
j=0
timestamp=""
out_timestamp=""
totdelay=0.0
eventList[0] = eventList[0] + A
lastQ = 0
last_clock = A
while NumberService != deadline:

    if(eventList[0] < eventList[1]):
        if (Queue == 0 and busy == 0):
            clock = SetClock((eventList[0]), (eventList[1]))
            pprint("clock: ",clock)
            NumberService = NumberService + 1
            bprint("numberservice: ",NumberService)
            NumberProcess = NumberProcess + 1
            yprint("Queue: ",Queue)
            S = random_generation_B()
            Es = Es + S
            eventList[1] = last_clock + S
            j = j + 1
            i = i + 1


            #Area_under_B = Area_under_B + busy * (clock - last_clock)
            last_clock = clock
            busy = 1
            A = random_generation_A()
            Ea = Ea + A
            eventList[0] = eventList[0] + A
            NumberProcess = NumberProcess + 1
            gprint("eventlist: ", eventList)
            clock = SetClock((eventList[0]), (eventList[1]))

        if (Queue==0 and busy == 1):
            clock = SetClock((eventList[0]), (eventList[1]))
            Area_under_B = Area_under_B + busy * (clock - last_clock)
            last_clock = clock
            lastQ = 0




        if (busy == 1):
            i = i + 1
            pprint("clock: ", clock)
            Queue = Queue + 1
            timestamp = timestamp + str(clock) +','
            A = random_generation_A()
            Ea = Ea + A
            eventList[0] = eventList[0] + A
            NumberProcess = NumberProcess + 1




            Area_under_Q = Area_under_Q + Queue*(clock - last_clock)
            last_clock=clock
            clock = SetClock((eventList[0]), (eventList[1]))
            Area_under_B = Area_under_B + busy * (clock - last_clock)

            lastQ = Queue

            bprint("numberservice: " , NumberService)
            yprint("Queue: " , Queue)
            gprint("eventlist: " , eventList)

    if (eventList[0] >= eventList[1]):

        if Queue == 0:

            clock = SetClock((eventList[0]), (eventList[1]))
            Area_under_B = Area_under_B + busy * (clock - last_clock)
            last_clock = clock
            pprint("clock: ", clock)
            bprint("numberservice: ", NumberService)
            yprint("Queue: ", Queue)
            print(Fore.LIGHTCYAN_EX,"eventlist: [", str(eventList[0]),", ~]")




            clock = SetClock_zero((eventList[0]),(eventList[1]))
            busy = 0
            i = i+1

            NumberService= NumberService+1
            A = random_generation_A()
            Ea = Ea + A
            eventList[0] = eventList[0] + A
            NumberProcess = NumberProcess + 1
            S = random_generation_B()
            Es = Es + S
            eventList[1] = clock + S
            j = j+1

            Area_under_Q = Area_under_Q + lastQ * (clock - last_clock)

            lastQ = Queue
            pprint("clock: " , clock)
            bprint("numberservice: " , NumberService)
            yprint("Queue: " , Queue)
            gprint("eventlist: " , eventList)

        if Queue > 0:
            lastQ = Queue
            Queue = Queue - 1
            S = random_generation_B()
            NumberService = NumberService + 1
            last_clock1=clock
            clock = SetClock((eventList[0]), (eventList[1]))
            busy = 1
            out_timestamp = out_timestamp + str(clock) +','
           # totdelay = totdelay + ( clock - timestamp)
            #timestamp=0.0



            eventList[1] = clock + S
            Es = Es + S
            j = j + 1
            pprint("clock: " , clock)
            bprint("numberservice: " , NumberService)
            yprint("Queue: " , Queue)
            gprint("eventlist: " , eventList)
            Area_under_Q = Area_under_Q + lastQ * (clock - last_clock)
            last_clock = clock
            clock = SetClock((eventList[0]),(eventList[1]))




        Area_under_B = Area_under_B + busy * (clock - last_clock)


        lastQ = Queue
        last_clock = clock

        busy = 1

print(Fore.WHITE,"")




m=0
ts=0.0
ots=0.0
timestamp = timestamp.split(',')
out_timestamp = out_timestamp.split(',')
for m in range(out_timestamp.__len__() - 1):
    ts = float(timestamp[m])
    ots = (float(out_timestamp[m]))
    totdelay = totdelay + (ots - ts)



print(Fore.YELLOW,"*****************FINAL RESULTS******************")
bprint("ServiceNumber  :  ",NumberService)
bprint("system clock   :  ",round(clock,2))
bprint("Area under B(t):  ",round(Area_under_B,2))
bprint("Area under Q(t):  ",round(Area_under_Q,2))
bprint("Total Delay    :  ",round(totdelay,2))


Wq = totdelay / NumberService
Lq = Area_under_Q / clock
p  = Area_under_B / clock
L  = Lq + p

gprint("Wq :  ",round(Wq,3))
gprint("Lq :  ",round(Lq,3))
gprint("p  :  ",round(p,3))
gprint("L  :  ",round(L,3))
W = 0.0



n=0
value_of_Es=0.0
value_of_Ea = 0.0
M=0.0
Landa=0.0
throughput=0.0

value_of_Es = Es/NumberService

value_of_Ea = eventList[0] / NumberProcess
W = Wq + value_of_Es
if value_of_Es == 0:
    print("something is going wrong!!!")
else: M = 1/value_of_Es
if value_of_Es == 0:
    print("something is going wrong!!!")
else: Landa = 1/value_of_Ea
#pprint("ES    :",round(value_of_Es,3))
pprint("W     :",round(W,3))


#pprint("Landa :",round(Landa,3))

#pprint("Mou   :",round(M,3))
print("")
if Landa < M:
    throughput = 1.0
    print(Fore.LIGHTBLUE_EX+"***********PAYDAR***********")
else:
    throughput = p*1.2
    print(Fore.RED + "!!!! NAPAYDAR !!!!")






import time
import sys

print(Fore.YELLOW+"")
animation = "|"
i=0
for i in range(15):
    time.sleep(0.1)
    sys.stdout.write(animation)
    sys.stdout.flush()

yprint("syetem THROUGHPUT :",round(throughput,1))
print("")






#@NAZANIN BAYATI