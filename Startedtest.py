# all algos (Complete), Graph(Complete), Comments (working)

import tkinter as tk                        # importing the tkinter module as tk from Python library
from tkinter import filedialog              # importing the filedialog module from tkinter library
import matplotlib.pyplot as plt             # importing the matplotlib.pyplot module as plt from Python library

def fcfs(processes, n, wt, tat, contex_SWT):   #
    wt[0] = 0                                  #
    tat[0] = processes[0][1]                   #

    for i in range(1, n):                      #
        wt[i] = processes[i - 1][1] + wt[i - 1] + contex_SWT #
        tat[i] = processes[i][1] + wt[i]       #

def rr(processes, n, wt, tat, quantum):        #
    rem_bt = [0] * n                           #
    for i in range(n):                         #
        rem_bt[i] = processes[i][1]            #
    t = 0                                      #
    while True:                                #
        done = True                            #
        for i in range(n):                     #
            if rem_bt[i] > 0:                  #
                done = False                   #
                if rem_bt[i] > quantum:        #
                    t += quantum               #
                    rem_bt[i] -= quantum       #
                else:                          #
                    t += rem_bt[i]             #
                    wt[i] = t - processes[i][1]#
                    rem_bt[i] = 0              #
        if done:                               #
            break                              #

    for i in range(n):                         #
        tat[i] = processes[i][1] + wt[i]       #

def sjf(processes, n, wt, tat):                #
    rt = [0] * n                               #
    for i in range(n):                         #
        rt[i] = processes[i][1]                #
    complete = 0                               #
    t = 0                                      #
    minm = float('inf')                        #
    short = 0                                  #
    check = False                              #

    while complete != n:                       #
        for j in range(n):                     #
            if processes[j][2] <= t and rt[j] < minm and rt[j] > 0: #
                minm = rt[j]                   #
                short = j                      #
                check = True                   #

        if not check:                          #
            t += 1                             #
            continue                           #

        rt[short] -= 1                         #
        minm = rt[short]                       #
        if minm == 0:                          #
            minm = float('inf')                #

        if rt[short] == 0:                     #
            complete += 1                      #
            check = False                      #
            fint = t + 1                       #
            wt[short] = fint - processes[short][1] - processes[short][2]#

            if wt[short] < 0:                  #
                wt[short] = 0                  #

        t += 1                                 #

    for i in range(n):                         #
        tat[i] = processes[i][1] + wt[i]       #

def srt(processes, n, wt, tat):                #
    rt = [0] * n                               #
    for i in range(n):                         #
        rt[i] = processes[i][1]                #
    complete = 0                               #
    t = 0                                      #
    minm = float('inf')                        #
    short = 0                                  #
    check = False                              #

    while complete != n:                       #
        for j in range(n):                     #
            if processes[j][2]<=t and rt[j]<minm and rt[j]>0:#
                minm=rt[j]                     #
                short=j                        #
                check=True                     #

        if not check:                          #
            t+=1                               #
            continue                           #

        rt[short]-=1                           #
        minm=rt[short]                         #
        if minm==0:                            #
            minm=float('inf')                  #

        if rt[short]==0:                       #
            complete+=1                        #
            check=False                        #

            fint=t+1                           #

            wt[short]=fint-processes[short][1]-processes[short][2]#

            if wt[short]<0:                    #
                wt[short]=0                    #

        t+=1                                   #

    for i in range(n):                         #
        tat[i]=processes[i][1]+wt[i]           #

root=tk.Tk()                                   #
root.withdraw()                                #

file_path=filedialog.askopenfilename()         #
contex_SWT=int(input("Enter context switching time: "))             #
algorithm=input("Enter scheduling algorithm (FCFS,RR, SJF, SRT): ") #
 
if algorithm=="RR":                            #
    quantum=int(input("Enter time quantum: ")) #

processes=[]                                   #
with open(file_path,'r') as file:              #
    n=int(file.readline())                     #
    for line in file:                          #
        process_info=line.strip().split()      #
        processes.append([int(process_info[0]),int(process_info[2]),int(process_info[1])]) #

n=len(processes)                               #
wt=[0]*n                                       #
tat=[0]*n                                      #
total_wt=0                                     #
total_tat=0                                    #

if algorithm=="FCFS":                          #
    fcfs(processes,n,wt,tat,contex_SWT)        #
elif algorithm=="RR":                          #
    rr(processes,n,wt,tat,quantum)             #
elif algorithm=="SJF":                         #
    sjf(processes,n,wt,tat)                    #
elif algorithm=="SRT":                         #
    srt(processes,n,wt,tat)                    #

for i in range(n):                             #
    total_wt+=wt[i]                            #
    total_tat+=tat[i]                          #

avg_wt=total_wt/n                              #
avg_tat=total_tat/n                            #

print("Average waiting time: ",avg_wt)         #
print("Average turn around time: ",avg_tat)    #

x_axis=[]                                      #
y_axis=[]                                      #
current_time=0                                 #

for i in range(n):                             #
    x_axis.append(current_time)                #
    y_axis.append(processes[i][0])             #
    current_time+=wt[i]                        #
    x_axis.append(current_time)                #
    y_axis.append(processes[i][0])             #
    current_time+=processes[i][1]              #
    x_axis.append(current_time)                #
    y_axis.append(processes[i][0])             #
    current_time+=contex_SWT                   #

plt.step(x_axis,y_axis,where='post')           #
plt.xlabel('Time')                             #
plt.ylabel('Processes')                        #
plt.show()                                     #
