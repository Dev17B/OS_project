import tkinter as tk                        # importing the tkinter module as tk from Python library
from tkinter import filedialog              # importing the filedialog module from tkinter library
import matplotlib.pyplot as plt             # importing the matplotlib.pyplot module as plt from Python library

# read input from the selected file and return
def select_file(filename):                             # defining a function named select_file that takes one argument filename.
    with open(filename, 'r') as f:                     # it opens the file with open('filename', 'r') as f.
        num_processes = int(f.readline().strip())      # it reads in each line of the file into an array called num_processes
        Task = []                                 # it creates an empty list called processes to store all of the data from each line of inpu
        for i in range(num_processes):                 # adding for loop to iterates through each number in num_processes
            line = f.readline().strip().split(' ')        # assigning line variable equals to f which will read the text
            process = {'number': int(line[0]), 'arrival_time': int(line[1]), 'burst_time': int(line[2]), 'priority': int(line[3])}   # stores them into a dictionary keyed by number with arrival time, burst time, priority values stored under those keys respectively.
            Task.append(process)                  # the append will add selected number in the list
    return Task                                   # it returns this list of dictionaries

# First Come First Serve scheduling algorithm
def fcfs(Task, switchT):                        # defining a function named fcfs that takes two argument Task, switchT.
    currentT = 0                                # assining current time equals to zero for now.
    schedule = []                               # it creates an empty list called schedule to store the data
    for process in Task:                        # creating a for loop to connect process in Task 
        if currentT < process['arrival_time']:  # in readings, if current time is smaller than process then its arrival time
            currentT = process['arrival_time']  # or in readings, if current time is equals to process then its also arrival time
        schedule.append(process['number'])      # The append will add the process arrival time at the end of the list as number
        currentT += process['burst_time']       # it will add the value to an currentT variable and assign the new value back to the same process as burst_time. there is no context switch time after the last process.
    return schedule                             # return statement for output


# Round Robin scheduling algorithm

# Shortest Job First scheduling algorithm

# Shortest Remaining Time scheduling algorithm


# generating the graph using the scheduled order  ---------------------------------------------
def generate_graph(schedule):                       #
    plt.step(range(len(schedule)), schedule, where='post')
    plt.xlabel('Time')                              #
    plt.ylabel('Process Number')                    #
    plt.ylim(0, max(schedule)+1)                    #
    plt.show()                                      #

# The Main function of all algorithoms  ----------------------------------------------------------------------------------------------------------

def schedule_processes(algorithm, Task, context_switching_time=0, time_quantum=0): # Define function to schedule processes based on selected algorithm
    current_time = 0                                          # Initialize variables
    completed_processes = []                                  #
    remaining_processes = Task.copy()                    #
    n_processes = len(Task)                              #

    # Sort processes based on selected algorithm
    if algorithm == 'FCFS':
        saved_process = sorted(remaining_processes, key=lambda x: x['arrival_time'])
    elif algorithm == 'SJF':
        saved_process = sorted(remaining_processes, key=lambda x: (x['arrival_time'], x['burst_time']))
    elif algorithm == 'SRT':
        saved_process = []
    # the main function continues
    elif algorithm == 'RR':
        saved_process = rr(remaining_processes, context_switching_time, time_quantum)
    # the main function continues

    # Calculating WT,TAT,RT for each process
    for i, p in enumerate(saved_process):
        if i == 0:
            p.waiting_time = 0
            p.turnaround_time = p.burst_time
            p.response_time = 0
        else:
            prev_p = saved_process[i-1]
            p.waiting_time = prev_p.turnaround_time + context_switching_time - p.arrival

# Initializing (Part of interface )  ----------------------------------------------------------------------------------------------------------
def main():                                          # Initialize GUI, defining a function named main
    root = tk()                                      # using Tkinter for creating the GUI
    root.title("Process Scheduler")                  # the title 
    root.geometry("500x500")                         # the size
    algorithm_label = algorithm_label (root, text="Select Algorithm:")    # Create widgets
    algorithm_label.pack()                                                # 
 
    algorithm_var = algorithm_var(root)                   #
    algorithm_var.set("FCFS")                             #

    algorithm_menu = algorithm_menu(root, algorithm_var, "FCFS", "RR", "SJF", "SRT")    #
    algorithm_menu.pack()                                 #

    file_label = file_label(root, text="Input File:")     #
    file_label.pack()                                     #

    file_entry = file_entry(root)                         #
    file_entry.pack()                                     #

    context_switch_label = context_switch_label(root, text="Context Switching Time:")   #
    context_switch_label.pack()                           #

    context_switch_entry = context_switch_entry(root)     #
    context_switch_entry.pack()                           #

    quantum_label = quantum_label(root, text="Time Quantum (RR Only):")     #
    quantum_label.pack()                                  #

    quantum_entry = quantum_entry(root)                   #
    quantum_entry.pack()                                  #

    output_label = output_label(root, text="Output:")     #
    output_label.pack()                                   #
 
    output_text = output_text(root, height=20)            #
    output_text.pack()                                    #

    def run_scheduler():
        # Get inputs
        input_file = file_entry.get()
        algorithm = algorithm_var.get()
        switchT = int(context_switch_entry.get())
        time_quantum = int(quantum_entry.get()) if algorithm == "RR" else None

        # Load processes from file
        Task = Task(input_file)

        # Schedule Task using selected algorithm
        if algorithm == "FCFS":
            schedule = fcfs(Task, switchT)
        # elif algorithm == "RR":
        #     schedule = rr(Task, switchT, time_quantum)
        # elif algorithm == "SJF":
        #     schedule = sjf(Task, switchT)
        # elif algorithm == "SRT":
        #     schedule = srt(Task, switchT)

        # Display output
        output_text.delete("1.0", 'END')
        for process in schedule:
            output_text.insert('END', str(process) + "\n")

    # Add run button
    run_button = run_button(root, text="Run", command=run_scheduler)
    run_button.pack()

    root.mainloop()

# The interface -------------------------------------------------------------------------------------------------------------
class Application(tk.Frame):                        #
    def __init__(self, master=None):                #
        super().__init__(master)                    #
        self.master = master                        #
        self.pack()                                 #
        self.create_widgets()                       #

    def create_widgets(self):
        self.input_label = tk.Label(self, text="Input File:")  # Label for input file
        self.input_label.grid(row=0, column=0)              #

        self.input_path = tk.Entry(self)                    # Entry field for input file path
        self.input_path.grid(row=0, column=1)               #

        self.input_button = tk.Button(self, text="Browse", command=self.browse_input_file)   # Button to select input file
        self.input_button.grid(row=0, column=2)             #

        self.algorithm_label = tk.Label(self, text="Scheduling Algorithm:")   # Label for scheduling algorithm 
        self.algorithm_label.grid(row=1, column=0)          #

        self.algorithm_var = tk.StringVar()                 # Dropdown menu for scheduling algorithm
        self.algorithm_options = ["First Come First Serve", "Round Robin", "Shortest Job First", "Shortest Remaining Time"]
        self.algorithm_dropdown = tk.OptionMenu(self, self.algorithm_var, *self.algorithm_options)
        self.algorithm_dropdown.grid(row=1, column=1)

        self.context_label = tk.Label(self, text="Context Switching Time:")   # Label for context switching time
        self.context_label.grid(row=2, column=0)            #

        self.context_time = tk.Entry(self)                  # Entry field for context switching time
        self.context_time.grid(row=2, column=1)             #

        self.quantum_label = tk.Label(self, text="Time Quantum:")   # Label for time quantum
        self.quantum_label.grid(row=3, column=0)            #

        self.quantum_time = tk.Entry(self)                  # Entry field for time quantum
        self.quantum_time.grid(row=3, column=1)             #

        self.schedule_button = tk.Button(self, text="Schedule", command=self.schedule_processes)    # Button to start scheduling
        self.schedule_button.grid(row=4, column=1)          #

    def browse_input_file(self):                            # Open file dialog to select input file
        file_path = filedialog.askopenfilename()            #
        self.input_path.delete(0, tk.END)                   #
        self.input_path.insert(0, file_path)                #

    def schedule_processes(self):                           # Retrieve user input values and start scheduling
        file_path = self.input_path.get()                   #
        algorithm = self.algorithm_var.get()                #
        context_time = float(self.context_time.get())       #
        quantum_time = float(self.quantum_time.get())       #
        # Call scheduling functions here with the provided inputs

root = tk.Tk()                                              #
app = Application(master=root)                              #
app.mainloop()                                              #

