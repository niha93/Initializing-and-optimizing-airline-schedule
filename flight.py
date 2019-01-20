# Declaring different data structures
tails=["T1","T2","T3","T4","T5","T6"]
gates=["AUS1","DAL1","DAL2","HOU1","HOU2","HOU3"]
airports=["AUS","DAL","HOU"]
flight_times={"AUSDAL":50,"DALAUS":50,"AUSHOU":45,"HOUAUS":45,
              "DALHOU":65,"HOUDAL":65}
ground_time={"AUS":25,"DAL":30,"HOU":35}
schedule_flight=[]

#Defining header for csv file
header=["tail_number","origin","destination","departure_time","arrival_time"]
schedule_flight.append(header)    

#Converting arrival time from minutes since midnight to military time
def arr_time_m():
    m_arr_time=(arrival_time // 60,arrival_time%60) 
    if (m_arr_time[1] in range (0,10)):
        y="0"+str(m_arr_time[1])
        m_arr_time=(arrival_time//60,y)
        new_m_time=int(''.join(str(x) for x in (m_arr_time)))
        k=str(new_m_time).zfill(4)
        return k
    else:
        new_m_time=int(''.join(str(x) for x in (m_arr_time)))
        k=str(new_m_time).zfill(4)
        return k 
    
#Converting depature time from minutes since midnight to military time
def dept_time_m():
    m_dept_time=(dept_time // 60,dept_time%60)
    if (m_dept_time[1] in range (0,10)):
        y="0"+str(m_dept_time[1])
        m_dept_time=(dept_time//60,y)
        new_m_time=int(''.join(str(x) for x in (m_dept_time)))
        k=str(new_m_time).zfill(4)
        return k
    else:
        new_m_time=int(''.join(str(x) for x in (m_dept_time)))
        k=str(new_m_time).zfill(4)
        return k

#Schedule for Flight T1 between Austin and Houston   

#First flight departs at 6:00am
dept_time=6*60
x=600
initial=str(x).zfill(4)
arrival_time=dept_time + flight_times["AUSHOU"]
j=arr_time_m()
list1=[]
list1.append("T1")
list1.append("AUS")
list1.append("HOU")
list1.append(initial)
list1.append(j)
schedule_flight.append(list1)

print("T1, AUS, HOU, " + initial + ", " + j)

#Flight should be grounded before 10:00pm
while True:
    loop1 = []    
    dept_time=arrival_time + ground_time["HOU"]
    if (dept_time > 1320):
        break
    m=dept_time_m() 
    
    arrival_time=dept_time+flight_times["HOUAUS"]
    k=arr_time_m()
    loop1.append("T1")
    loop1.append("HOU")
    loop1.append("AUS")
    loop1.append(m)
    loop1.append(k)
    schedule_flight.append(loop1)  # Appending values to the empty list
    
    print("T1, HOU, AUS, " + m + ", " + k )
    
    loop2=[]
    dept_time=arrival_time + ground_time["AUS"]
    m=dept_time_m() 
    arrival_time = dept_time+flight_times["AUSHOU"]
    if(arrival_time > 1320):
        break
    k=arr_time_m()
    loop2.append("T1")
    loop2.append("AUS")
    loop2.append("HOU")
    loop2.append(m)
    loop2.append(k)
    print("T1, AUS, HOU, " + m + ", " + k )
    schedule_flight.append(loop2)
    
#Schedule for Flight T2 between Dallas and Houston

#First flight departs at 6:00am
dept_time=6*60
x=600
initial=str(x).zfill(4)
arrival_time=dept_time + flight_times["DALHOU"]
j=arr_time_m()
list2=[]
list2.append("T2")
list2.append("DAL")
list2.append("HOU")
list2.append(initial)
list2.append(j)
schedule_flight.append(list2)
print("T2, DAL, HOU, " + initial + ", " + j)

#Flight should be grounded before 10:00pm
while True:    
    loop3=[]
    dept_time=arrival_time + ground_time["HOU"]
    if(dept_time > 1320):
        break
    m=dept_time_m() 
    arrival_time=dept_time+flight_times["HOUDAL"]
    k=arr_time_m()
    loop3.append("T2")
    loop3.append("HOU")
    loop3.append("DAL")
    loop3.append(m)
    loop3.append(k)
    schedule_flight.append(loop3)
    print("T2, HOU, DAL, " + m + ", " + k )
    
    loop4=[]
    dept_time=arrival_time + ground_time["DAL"]
    m=dept_time_m() 
    arrival_time= dept_time+flight_times["DALHOU"]
    if (arrival_time >1320):
        break
    k=arr_time_m()
    loop4.append("T2")
    loop4.append("DAL")
    loop4.append("HOU")
    loop4.append(m)
    loop4.append(k)
    schedule_flight.append(loop4)
    print("T2, DAL, HOU, " + m + ", " + k )
  
#Schedule for Flight T3 between Dallas and Houston    

#First flight departs at 6:00am
dept_time=6*60
x=600
initial=str(x).zfill(4)
arrival_time=dept_time + flight_times["DALHOU"]
j=arr_time_m()
list3=[]
list3.append("T3")
list3.append("DAL")
list3.append("HOU")
list3.append(initial)
list3.append(j)
schedule_flight.append(list3)
print("T3, DAL, HOU, " + initial + ", " + j)

#Flight should be grounded before 10:00pm
while True:    
    loop5=[]
    dept_time=arrival_time + ground_time["HOU"]
    if (dept_time > 1320):
        break
    m=dept_time_m() 
    arrival_time=dept_time+flight_times["HOUDAL"]
    k=arr_time_m()
    loop5.append("T3")
    loop5.append("HOU")
    loop5.append("DAL")
    loop5.append(m)
    loop5.append(k)
    schedule_flight.append(loop5)
    print("T3, HOU, DAL, " + m + ", " + k )
    
    loop6=[]
    dept_time=arrival_time + ground_time["DAL"]
    m=dept_time_m() 
    arrival_time= dept_time+flight_times["DALHOU"]
    if (arrival_time > 1320):
        break
    k=arr_time_m()
    k=arr_time_m()
    loop6.append("T3")
    loop6.append("DAL")
    loop6.append("HOU")
    loop6.append(m)
    loop6.append(k)
    schedule_flight.append(loop6)
    print("T3, DAL, HOU, " + m + ", " + k )
   
#Schedule for Flight T4 between Houston and Austin

#First flight departs at 6:00am
dept_time=6*60
x=600
initial=str(x).zfill(4)
arrival_time=dept_time + flight_times["HOUAUS"]
j=arr_time_m()
list4=[]
list4.append("T4")
list4.append("HOU")
list4.append("AUS")
list4.append(initial)
list4.append(j)
schedule_flight.append(list4)
print("T4, HOU, AUS, " + initial + ", " + j)

#Flight should be grounded before 10:00pm
while True:  
    loop7=[]
    dept_time=arrival_time + ground_time["AUS"]
    if (dept_time > 1320):
        break
    m=dept_time_m() 
    arrival_time=dept_time+flight_times["AUSHOU"]
    k=arr_time_m()
    loop7.append("T4")
    loop7.append("AUS")
    loop7.append("HOU")
    loop7.append(m)
    loop7.append(k)
    schedule_flight.append(loop7)
    print("T4, AUS, HOU, " + m + ", " + k )
    
    loop8=[]
    dept_time=arrival_time + ground_time["HOU"]
    m=dept_time_m() 
    arrival_time= dept_time+flight_times["HOUAUS"]
    if (arrival_time > 1320):
        break
    loop8.append("T4")
    loop8.append("HOU")
    loop8.append("AUS")
    loop8.append(m)
    loop8.append(k)
    schedule_flight.append(loop8)
    k=arr_time_m()
    print("T4, HOU, AUS, " + m + ", " + k )
    

#Schedule for Flight T5 between Houston and Dallas

#First flight departs at 6:00am
dept_time=6*60
x=600
initial=str(x).zfill(4)
arrival_time=dept_time + flight_times["HOUDAL"]
j=arr_time_m()
list5=[]
list5.append("T5")
list5.append("HOU")
list5.append("DAL")
list5.append(initial)
list5.append(j)
schedule_flight.append(list5)
print("T5, HOU, DAL, " + initial + ", " + j)

#Flight should be grounded before 10:00pm
while True:   
    loop9=[]
    dept_time=arrival_time + ground_time["DAL"]
    if (dept_time > 1320):
        break
    m=dept_time_m()     
    arrival_time=dept_time+flight_times["HOUDAL"]
    if(arrival_time>=1300):
        break
    k=arr_time_m()
    loop9.append("T5")
    loop9.append("HOU")
    loop9.append("DAL")
    loop9.append(m)
    loop9.append(k)
    schedule_flight.append(loop9)
    print("T5, HOU, DAL, " + m + ", " + k )
    
    loop10=[]
    dept_time=arrival_time + ground_time["HOU"]
    m=dept_time_m() 
    arrival_time= dept_time+flight_times["DALHOU"]
    if (arrival_time > 1320):
        break
    k=arr_time_m()
    loop10.append("T5")
    loop10.append("DAL")
    loop10.append("HOU")
    loop10.append(m)
    loop10.append(k)
    schedule_flight.append(loop10)
    print("T5, DAL, HOU, " + m + ", " + k )
    
    
#Schedule for Flight T6 between Dallas and Houston

#First flight departs at 6:00am
dept_time=6*60
x=600
initial=str(x).zfill(4)
arrival_time=dept_time + flight_times["HOUDAL"]
j=arr_time_m()
list6=[]
list6.append("T6")
list6.append("HOU")
list6.append("DAL")
list6.append(initial)
list6.append(j)
schedule_flight.append(list6)
print("T6, HOU, DAL, " + initial + ", " + j)

#Flight should be grounded before 10:00pm 
while True:  
    loop11=[]
    dept_time=arrival_time + ground_time["DAL"]
    if (dept_time > 1320):
        break
    m=dept_time_m() 
    arrival_time=dept_time+flight_times["HOUDAL"]
    if(arrival_time>=1300):
        break
    k=arr_time_m()
    loop11.append("T6")
    loop11.append("HOU")
    loop11.append("DAL")
    loop11.append(m)
    loop11.append(k)
    schedule_flight.append(loop11)
    print("T6, HOU, DAL, " + m + ", " + k )
    
    loop12=[]
    dept_time=arrival_time + ground_time["HOU"]
    z=ground_time["HOU"]
    m=dept_time_m()     
    arrival_time= dept_time+flight_times["DALHOU"]
    if (arrival_time > 1320):
        break
    k=arr_time_m()
    loop12.append("T6")
    loop12.append("DAL")
    loop12.append("HOU")
    loop12.append(m)
    loop12.append(k)
    schedule_flight.append(loop12)
    print("T6, DAL, HOU, " + m + ", " + k )
    
# Importing CSV module to write into CSV format
import csv

#Writing the List of List to Excel CSV
with open("flight_schedule.csv","w") as f:
    wr=csv.writer(f,delimiter="\n",quoting=csv.QUOTE_NONE)
    wr.writerow(schedule_flight)