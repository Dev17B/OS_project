# all algos (Complete), Graph(Complete), Comments (working)

import tkinter as tk                        # importing the tkinter module as tk from Python library
from tkinter import filedialog              # importing the filedialog module from tkinter library
import matplotlib.pyplot as plt             # importing the matplotlib.pyplot module as plt from Python library

def fcfs(processes, n, wt, tat, contex_SWT):   # defining a function named fcfs that takes five argument processes, n, wt, tat, contex_SWT.
    wt[0] = 0                                  # it creates an empty list called WT to store the data and assigning it equals to zero for now.
    tat[0] = processes[0][1]                   # it creates an empty list called TAT to store the data and assigning it equals to processes for now.
    for i in range(1, n):                      # reating a for loop for i in range and it takes two parameter 1 and n, so loop will iterate through all of the values from 1 up until n-1
        wt[i] = processes[i - 1][1] + wt[i - 1] + contex_SWT # take one value at a time from each iteration and it assign them into wt[i] which is equal to process i - 1's value plus wt[i - 1] plus contex_SWT which is equal to 0 because there are no other variables yet defined in this program.
        tat[i] = processes[i][1] + wt[i]       # the TAT parameter equals to processes[i][1] + waiting time

def rr(processes, n, wt, tat, quantum):        # defining a function named fcfs that takes five argument processes, n, wt, tat, quantum.
    burst_time = [0] * n                       # assigning burst_time equlas to variable 0 multiply by variable n
    for i in range(n):                         # creating a for loop for i in range for variable n
        burst_time[i] = processes[i][1]        # assigning burst_time equlas to parameter processes 
    t = 0                                      # assigning t equlas to 0
    while True:                                # creating a while loop to run the process
        done = True                            # done which is equlas to Ture
        for i in range(n):                     # creating a for loop for i in range for variable n
            if burst_time[i] > 0:              # if the burst_time is more than 0 then,
                done = False                   # done which is equlas to false
                if burst_time[i] > quantum:    # if the burst_time is more than quantum then
                    t += quantum               # it will increment the t with quantum
                    burst_time[i] -= quantum   # and burst_time will decrementing with quantum
                else:                            # else 
                    t += burst_time[i]           # it will increment the t with burst_time
                    wt[i] = t - processes[i][1]  # the wt will be equals to t - processes parameter
                    burst_time[i] = 0            # assigning burst_time equlas to 0
        if done:                                 # if it done then,
            break                                # break the loop
    for i in range(n):                         # creating a for loop for i in range for variable n
        tat[i] = processes[i][1] + wt[i]       # assigning tat equlas to processes and waiting time

def sjf(processes, n, wt, tat):                # defining a function named sjf that takes four argument processes, n, wt, tat.
    rt = [0] * n                               # assigning remaining time equlas to variable 0 multiply by variable n
    for i in range(n):                         # creating a for loop for i in range for variable n
        rt[i] = processes[i][1]                # assigning remaining time equals to processes
    complete = 0                               # assigning variable complete equals to 0 for now
    t = 0                                      # assigning variable t equals to 0 for now
    minm = float('inf')                        # assigning variable minm equals to float('inf') to store the remaining burst time 
    short = 0                                  # assigning variable short equals to 0 for now
    check = False                              # assigning variable check equals to False 

    while complete != n:                       # creating a while loop so will continue executing until all processes have been completed 
        for j in range(n):                     # creating a for loop for i in range for variable n
            if processes[j][2] <= t and rt[j] < minm and rt[j] > 0: # it used to check if a process j has arrived and remaining burst time greater than zero and its remaining burst time is less than the current minimum value
                minm = rt[j]                   # assigning variable minm equals to variable remaining time with variable j
                short = j                      # assigning variable short equals to j
                check = True                   # assigning variable check equals to True 
        if not check:                          # it cheack if any process was selected to be executed during the current time quantum.
            t += 1                             # If no process has been selected, the system time is incremented by 1 and,
            continue                           # then loop continues to the next iteration
        rt[short] -= 1                         # remaining time value is decremented by 1 to simulate the execution of one time quantum
        minm = rt[short]                       # it updated the new value of remaining time of the process short 
        if minm == 0:                          # if minm is equals to 0 then,
            minm = float('inf')                # it assign variable minm equals to float('inf') to store the remaining burst time 
        if rt[short] == 0:                     # if rt[short] is equals to 0 then,
            complete += 1                      # complete value is increment by 1 to simulate the execution of one time quantum
            check = False                      # the check set to False to indicate that a new process needs to select for execution in quantum
            fint = t + 1                       # assigning finish time to t plus 1
            wt[short] = fint - processes[short][1] - processes[short][2] # it calculate the difference between the finish time of the selected process and its arrival time processes and burst time  to get waiting time of the process short 
            if wt[short] < 0:                  # if the waiting time is less than 0 then,
                wt[short] = 0                  # waiting time of the process short is 0
        t += 1                                 # t value is increment by 1 
    for i in range(n):                         # creating a for loop for i in range for variable n
        tat[i] = processes[i][1] + wt[i]       # it calculate the processes plus waiting time to get TAT

def srt(processes, n, wt, tat):                # defining a function named SRT that takes four argument processes, n, wt, tat.
    rt = [0] * n                               # assigning remaining time equlas to variable 0 multiply by variable n
    for i in range(n):                         # creating a for loop for i in range for variable n
        rt[i] = processes[i][1]                # assigning remaining time equals to processes
    complete = 0                               # assigning variable complete equals to 0 for now
    t = 0                                      # assigning variable t equals to 0 for now
    minm = float('inf')                        # assigning variable minm equals to float('inf') to store the remaining burst time 
    short = 0                                  # assigning variable short equals to 0 for now
    check = False                              # assigning variable check equals to False 
    while complete != n:                       # creating a while loop so will continue executing until all processes have been completed 
        for j in range(n):                     # creating a for loop for i in range for variable n
            if processes[j][2]<=t and rt[j]<minm and rt[j]>0: # it used to check if a process j has arrived and remaining burst time greater than zero and its remaining burst time is less than the current minimum value
                minm = rt[j]                   # assigning variable minm equals to variable remaining time with variable j
                short = j                      # assigning variable short equals to j
                check = True                   # assigning variable check equals to True 
        if not check:                          # it cheack if any process was selected to be executed during the current time quantum.
            t+=1                               # If no process has been selected, the system time is incremented by 1 and,
            continue                           # then loop continues to the next iteration
        rt[short]-=1                           # remaining time value is decremented by 1 to simulate the execution of one time quantum
        minm=rt[short]                         # it updated the new value of remaining time of the process short 
        if minm==0:                            # if minm is equals to 0 then,
            minm=float('inf')                  # it assign variable minm equals to float('inf') to store the remaining burst time
        if rt[short]==0:                       # if rt[short] is equals to 0 then,
            complete+=1                        # complete value is increment by 1 to simulate the execution of one time quantum
            check=False                        # the check set to False to indicate that a new process needs to select for execution in quantum
            fint=t+1                           # # assigning finish time to t plus 1
            wt[short]=fint-processes[short][1]-processes[short][2]# # it calculate the difference between the finish time of the selected process and its arrival time processes and burst time  to get waiting time of the process short 
            if wt[short]<0:                    # if the waiting time is less than 0 then,
                wt[short]=0                    # waiting time of the process short is 0
        t+=1                                   # t value is increment by 1 
    for i in range(n):                         # creating a for loop for i in range for variable n
        tat[i]=processes[i][1]+wt[i]           # it calculate the processes plus waiting time to get TAT

root=tk.Tk()                                   # it creates a new Tkinter window, which is the main window or container for the GUI.
root.withdraw()                                # it hides the main window, which may be useful when the program first starts and the window is not yet needed or fully initialize

file_path=filedialog.askopenfilename()         # it opens a dialog box that allows the user to navigate to a directory and select a file
contex_SWT=int(input("Enter context switching time: "))             # it ask user to enter a context switching time which is equal to contex_SWT for the program
algorithm=input("Enter scheduling algorithm (FCFS,RR, SJF, SRT): ") # it ask user to enter scheduling algorithm from FCFS,RR, SJF, SRT  which is equal to algorithm for the program
if algorithm=="RR":                            # if user select RR then,
    quantum=int(input("Enter time quantum: ")) # it also ask user to enter the time quantum which is equal to quantum for the program
processes=[]                                   # it creates an empty list called processes to store the data
with open(file_path,'r') as file:              # it opens a file, 
    n=int(file.readline())                     # then it reads in one line at a time,
    for line in file:                          # creating a for loop for the line in file,
        process_info=line.strip().split()      # And it stores each line into the process_info variable.
        processes.append([int(process_info[0]),int(process_info[2]),int(process_info[1])]) # The code then splits up the string of text stored in process_info and then appends these values onto the end of all other values in processes so that they are now stored

n=len(processes)                               # assigning n equlas to len to return the number of items in a container as processes
wt=[0]*n                                       # assigning the Wt equals to variable 0 multiplied by n
tat=[0]*n                                      # assigning the TAT equals to variable 0 multiplied by n
total_wt=0                                     # assigning total_wt equals to 0
total_tat=0                                    # assigning total_tat equals to 0

if algorithm=="FCFS":                          # if user selectes FCFS in algorithm then,
    fcfs(processes,n,wt,tat,contex_SWT)        # the program runs the fcfs algorithm 
elif algorithm=="RR":                          # if user selectes RR in algorithm then,
    rr(processes,n,wt,tat,quantum)             # the program runs the RR algorithm 
elif algorithm=="SJF":                         # if user selectes SJF in algorithm then,
    sjf(processes,n,wt,tat)                    # the program runs the sjf algorithm 
elif algorithm=="SRT":                         # if user selectes SRT in algorithm then,
    srt(processes,n,wt,tat)                    # the program runs the srt algorithm 

for i in range(n):                             # creating a for loop for i in range for variable n
    total_wt+=wt[i]                            # it will increment the total_wt with WT
    total_tat+=tat[i]                          # it will increment the total_tat with tat
avg_wt=total_wt/n                              # assigning avg_wt equals to total_wt devided by n variable
avg_tat=total_tat/n                            # assigning avg_tat equals to avg_tat devided by n variable
print("Average waiting time: ",avg_wt)         # it prints the avg_wt with print statment as Average waiting time
print("Average turn around time: ",avg_tat)    #  it prints the avg_tat with print statment as Average turn around time
 
x_axis=[]                                      # it creates an empty list called x_axis to store the data
y_axis=[]                                      # it creates an empty list called y_axis to store the data
current_time=0                                 # assigning current_time to 0 for now
for i in range(n):                             # creating a for loop for i in range for variable n
    x_axis.append(current_time)                # the current time is updated by adding the wait time of the current process and it updated time adds in x axis and,
    y_axis.append(processes[i][0])             # current process ID is appended to y axis
    current_time+=wt[i]                        # it will increment the current time with WT variable
    x_axis.append(current_time)                # current time is updated again by adding the execution time of the current process and it updated time adds in x axis and,
    y_axis.append(processes[i][0])             # process ID are again appended to y axis
    current_time+=processes[i][1]              # it will increment the current time with processes variable
    x_axis.append(current_time)                # the current time is updated by adding the context switching wait time, which is the time it takes to switch from one process to another,
    y_axis.append(processes[i][0])             # process ID are again appended to y axis
    current_time+=contex_SWT                   # it will increment the current time with contex_SWT variable

plt.step(x_axis,y_axis,where='post')           # The plt.step function takes in two arguments, x axis and y axis, which are arrays or that is used to create the plot
plt.xlabel('Time')                             # it adds the time in x label
plt.ylabel('Processes')                        # it adds the Processes in y labele
plt.show()                                     # it shows the output in graph 
