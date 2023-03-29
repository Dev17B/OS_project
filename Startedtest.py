import tkinter as tk                        # importing the tkinter module as tk from Python library
from tkinter import filedialog              # importing the filedialog module from tkinter library
import matplotlib.pyplot as plt             # importing the matplotlib.pyplot module as plt from Python library

# read input from the selected file and return
def select_file(filename):                             # defining a function named select_file that takes one argument filename.
    with open(filename, 'r') as f:                     # it opens the file with open('filename', 'r') as f.
        num_processes = int(f.readline().strip())      # it reads in each line of the file into an array called num_processes
        Task = []                                      # it creates an empty list called processes to store all of the data from each line of inpu
        for i in range(num_processes):                 # adding for loop to iterates through each number in num_processes
            line = f.readline().strip().split(' ')     # assigning line variable equals to f which will read the text
            process = {'number': int(line[0]), 'arrival_time': int(line[1]), 'burst_time': int(line[2]), 'priority': int(line[3])}   # stores them into a dictionary keyed by number with arrival time, burst time, priority values stored under those keys respectively.
            Task.append(process)                       # the append will add selected number in the list
    return Task                                        # it returns this list of dictionaries

# First Come First Serve scheduling algorithm
def fcfs(Task, switchT):                        # defining a function named fcfs that takes two argument Task, switchT.
    currentT = 0                                # assining current time equals to zero for now.
    schedule = []                               # it creates an empty list called schedule to store the data
    for process in Task:                        # creating a for loop to connect process in Task 
        if currentT < process['arrival_time']:  # in readings, if current time is smaller than process then its arrival time
            currentT = process['arrival_time']  # or in readings, if current time is equals to process then its also arrival time
        schedule.append(process['number'])      # The append will add the process arrival time at the end of the list as number
        currentT += process['burst_time'] + switchT # it will add the value to an currentT variable and assign the new value back to the same process as burst_time. there is no context switch time after the last process.
    return schedule                             # return statement for output

# Round Robin scheduling algorithm

# Shortest Job First scheduling algorithm

# Shortest Remaining Time scheduling algorithm
def srt(Task, switchT):                         # defining a function named srt that takes two argument Task, switchT. 
    currentT = 0                                # assining current time equals to zero for now.
    schedule = []                               # it creates an empty list called schedule to store the data
    remaining_pro = Task[:]                     # creating a remaining_pro list and assining equals to task
    while True:                                 # while true for keep the process in runing 
        ready_queue = [process for process in remaining_pro if process['arrival_time'] <= currentT]  #
        if not ready_queue:                     # if above condition is not applicable then break the loop
            break                               # break statment
        next_process = min(ready_queue, key=lambda process: process['burst_time'])  # 
        next_process['burst_time'] -= 1         # It subtracts the next process operator burst_time from the left operand and assign the result to 1 operand
        if next_process['burst_time'] == 0:     # if next process operator burst time is equals to 0,
            remaining_pro.remove(next_process)  # then the remaining_pro will prmove the next process vlaue
        schedule.append(next_process['number']) # the aooend will add the next process value to end of the list of schedule
        currentT += 1 + switchT                 # it will add the value to a current variable and assign the new value back to the same process and it add 1 & the switch time.
    return schedule                             # the return statment for schedule 

# generating the graph using the scheduled order  ---------------------------------------------
def generate_graph(schedule):                       # it iterates through the list of processes and plots them on a graph.
    plt.step(range(len(schedule)), schedule, where='post') # starts with the first process, then iterates to the last process in the list.
    plt.xlabel('Time')                              # The x-axis is time
    plt.ylabel('Process Number')                    # The y-axis is number of processes that are currently running
    plt.ylim(0, max(schedule)+1)                    # it generates a graph of the schedule
    plt.show()                                      # it will show the result 

# The Main function of all algorithoms  ----------------------------------------------------------------------------------------------------------
def schedule_processes(algorithm, Task, context_switching_time=0, time_quantum=0): # Define function to schedule processes based on selected algorithm
    currentT = 0                                    # Initialize variables, assining current time equals to zero for now.
    completed_processes = []                        # it creates an empty list called completed_processes to store the data
    remaining_pro = Task.copy()                     # assinign a remaining_pro equals to task and it copy the task that isin process
    n_processes = len(Task)                         # assinign a n_processes equals to len in task where len returns a number of items in a container.

    # Sort processes based on selected algorithm
    if algorithm == 'FCFS':                         # if user select FCFS then it run this process
        saved_process = sorted(remaining_pro, key=lambda x: x['arrival_time'])  #
    elif algorithm == 'SJF':                        # if user select SJF then it run this process
        saved_process = sorted(remaining_pro, key=lambda x: (x['arrival_time'], x['burst_time']))  #
    elif algorithm == 'SRT':                        # if user select SRT then it run this process
        sorted_processes = []                       # it creates an empty list called sorted_processes to store the data
        while len(remaining_pro) > 0:               # Creating a while loop, to return a number of items in a container the remaining process is more than 0.
            arrived_processes = [p for p in remaining_pro if p.arrival_time <= currentT]  # Geting all processes that have arrived at the current time
            if len(arrived_processes) == 0:         # If there are no arrived processes then,
                currentT += 1                       # it will increment the current time
                continue                            # and the process will continue
            sorted_arrived_pro = sorted(arrived_processes, key=lambda x: x.burst_time) # Sort arrived processes by remaining burst time
            next_process = sorted_arrived_pro[0]   # Geting the process with the shortest remaining burst time
            sorted_processes.append(next_process)   # Add the process to the sorted list of processes and,
            remaining_pro.remove(next_process)      # it will remove it from the remaining processes

    elif algorithm == 'RR':                         # if user select RR then it run this process
        saved_process = rr(remaining_pro, context_switching_time, time_quantum)
    # the main function continues

    # Calculating WT,TAT,RT for each process
    for i, p in enumerate(saved_process):          # Creating a for loop for i and p in enumerate to obtain an saved_process list
        if i == 0:                                 # if i is equals to 0 then,
            p.waiting_time = 0                     # waiting_time for p is 0
            p.turnaround_time = p.burst_time       # turnaround_time and burst_time for p is equals as well,
            p.response_time = 0                    # response_time for p is 0 also.
        else:                                      # else,
            prev_p = saved_process[i-1]            # prev_p (stores the previous state of this particular process before it was interrupted) and saved_process (after interruption)
            p.waiting_time = prev_p.turnaround_time + context_switching_time - p.arrival  # if will make waiting_time equals to turnaround_time + context_switching_time - arrival for p.

# Initializing (Part of interface )  ----------------------------------------------------------------------------------------------------------
def main():                                          # Initialize GUI, defining a function named main
    root = tk()                                      # using Tkinter for creating the GUI
    root.title("Process Scheduler")                  # the title 
    root.geometry("500x500")                         # the size
    algorithm_label = tk.Label(root, text="Select Algorithm:")    # Create widgets
    algorithm_label.pack()                           # 
 
    algorithm_var = tk.StringVar(root)               #
    algorithm_var.set("FCFS")                        #

    algorithm_menu = tk.OptionMenu(root, algorithm_var, "FCFS", "RR", "SJF", "SRT")    #
    algorithm_menu.pack()                            #

    file_label = tk.Label(root, text="Input File:")  #
    file_label.pack()                                #

    file_entry = tk.Entry(root)                      #
    file_entry.pack()                                #

    context_switch_label = tk.Label(root, text="Context Switching Time:")   #
    context_switch_label.pack()                      #

    context_switch_entry = tk.Entry(root)            #
    context_switch_entry.pack()                      #

    quantum_label = tk.Label(root, text="Time Quantum (RR Only):")     #
    quantum_label.pack()                             #

    quantum_entry = tk.Entry(root)                   #
    quantum_entry.pack()                             #

    output_label = tk.Label(root, text="Output:")    #
    output_label.pack()                              #
 
    output_text = tk.Text(root, height=20)           #
    output_text.pack()                               #

    def run_scheduler():                             # defining a function named run_scheduler that takes no argument.
        input_file = file_entry.get()                # getting  a improt file as a file entry
        algorithm = algorithm_var.get()              # getting  a algorithm as a algorithm_var
        switchT = int(context_switch_entry.get())    # getting  a switchT as intager for context_switch_entry
        time_quantum = int(quantum_entry.get()) if algorithm == "RR" else None  # if the selected algorithm is RR then get time_quantum as a intager for quantum_entry
        Task = Task(input_file)                      # Loading processes from file

        if algorithm == "FCFS":                         # if the selected algorithm is FCFS then,
            schedule = fcfs(Task, switchT)              # run schedule as fcfs with its two argument Task, switchT
        # elif algorithm == "RR":                       # if the selected algorithm is RR then,
        #     schedule = rr(Task, switchT, time_quantum)# run schedule as RR with its three argument Task, switchT and time_quantum
        # elif algorithm == "SJF":                      # if the selected algorithm is SJF then,
        #     schedule = sjf(Task, switchT)             # run schedule as SJF with its two argument Task, switchT
        elif algorithm == "SRT":                        # if the selected algorithm is SRT then,
            schedule = srt(Task, switchT)               # run schedule as SRT with its two argument Task, switchT
        
        output_text.delete("1.0", 'END')                   # Display output
        for process in schedule:                           # for loop with the variable process in order to iterate through all of the processes in schedule.
            output_text.insert('END', str(process) + "\n") # it inserts "END" at the end of each line in output_text, where it will display the process's output.

    run_button = run_button(root, text="Run", command=run_scheduler) # Adding run button
    run_button.pack()                                     # it organizes widgets in horizontal and vertical boxes
    root.mainloop()                                       # create commands that are run on each process using root's mainloop() function.

# The interface -------------------------------------------------------------------------------------------------------------
class Application(tk.Frame):                        # adding Application class for tkinter
    def __init__(self, master=None):                # initializing the application object with a master widget.
        super().__init__(master)                    # using super() function to call the parent class's __init__ method, it sets up the frame and creates widgets.
        self.master = master                        # assigning self.master equals to master
        self.pack()                                 # it organizes widgets in horizontal and vertical boxes
        self.create_widgets()                       # assigning create_widgets to self parameter

    def create_widgets(self):                                 # defining a function named create_widgets that takes one argument self.
        self.input_label = tk.Label(self, text="Input File:") # Label for input file
        self.input_label.grid(row=0, column=0)                # giving size 0 for the row and column both

        self.input_path = tk.Entry(self)                      # Entry field for input file path
        self.input_path.grid(row=0, column=1)                 # giving size 0 and 1 for the row and column 

        self.input_button = tk.Button(self, text="Browse", command=self.browse_input_file)   # Button to select input file
        self.input_button.grid(row=0, column=2)               # giving size 0 and 2 for the row and column 

        self.algorithm_label = tk.Label(self, text="Scheduling Algorithm:")   # Label for scheduling algorithm 
        self.algorithm_label.grid(row=1, column=0)            # giving size 1 and 0 for the row and column 

        self.algorithm_var = tk.StringVar()                   # Dropdown menu for scheduling algorithm
        self.algorithm_options = ["First Come First Serve", "Round Robin", "Shortest Job First", "Shortest Remaining Time"] # Label for selecting scheduling algorithm 
        self.algorithm_dropdown = tk.OptionMenu(self, self.algorithm_var, *self.algorithm_options)
        self.algorithm_dropdown.grid(row=1, column=1)         # giving size 1 for the row and column 

        self.context_label = tk.Label(self, text="Context Switching Time:")   # Label for context switching time
        self.context_label.grid(row=2, column=0)              # giving size 2 and 0 for the row and column 

        self.context_time = tk.Entry(self)                    # Entry field for context switching time
        self.context_time.grid(row=2, column=1)               # giving size 2 and 1 for the row and column 

        self.quantum_label = tk.Label(self, text="Time Quantum:")   # Label for time quantum
        self.quantum_label.grid(row=3, column=0)              # giving size 3 and 0 for the row and column 

        self.quantum_time = tk.Entry(self)                    # Entry field for time quantum
        self.quantum_time.grid(row=3, column=1)               # giving size 3 and 1 for the row and column 

        self.schedule_button = tk.Button(self, text="Schedule", command=self.schedule_processes)   # Button to start scheduling
        self.schedule_button.grid(row=4, column=1)            # giving size 4 and 1 for the row and column 
  
    def browse_input_file(self):                              # defining a function named browse_input_file that takes no argument.
        file_path = filedialog.askopenfilename()              # Open file dialog to select input file
        self.input_path.delete(0, tk.END)                     # it delets the text from the input file and,
        self.input_path.insert(0, file_path)                  # It inserts the text into the file_path variable.
#Retrieve user input values and start scheduling
    def schedule_processes(self):                           #  defining a function named schedule_processes that takes one argument self.
        file_path = self.input_path.get()                   # retrieving the input path from the user.
        algorithm = self.algorithm_var.get()                # retrieving the input path from selected algorithms
        context_time = float(self.context_time.get())       # gets a value for algorithm and context time.
        quantum_time = float(self.quantum_time.get())       # it calculates quantum time by multiplying the context time with the quantum_time variable.
        # Call scheduling functions here with the provided inputs

root = tk.Tk()                                              # assigning root equals to tk.TK with no argument
app = Application(master=root)                              # Creating an application object and given to the master window (root) as its parent.
app.mainloop()                                              # main loop of the program is then started inside the method mainloop() which will be executed repeatedly until the user closes it.

