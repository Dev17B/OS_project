import time
from time import sleep
st = time.process_time()

# class to represent process
class Process:
    def __init__(self, pid, a_time, b_time, priority):
        self.pid = pid
        self.a_time = a_time  # Arrival Time
        self.b_time = b_time  # Burst Time
        self.priority = priority

    # string to represent Process object
    def __repr__(self):
        return f"Process {self.pid} ({self.a_time}, {self.b_time}, {self.priority})"


# function to read input and create a list of process objects
def read_inp_file(inp_file):
    with open(inp_file, "r") as f:
        num_processes = int(f.readline().strip())  # read number of processes from first line
        processes = []  # list to store process objects
        for x in range(num_processes):
            pid, a_time, b_time, priority = map(int, f.readline().strip().split())
            processes.append(Process(pid, a_time, b_time, priority))
    return processes


def sjf_scheduling(processes):
    processes.sort(key=lambda p: p.priority)
    c_time = 0  # completion time
    w_time = 0  # wait time
    ta_time = 0  # turnaround time
    r_time = 0  # response time

    for x in processes:
        if x.a_time > c_time:
            c_time = x.a_time #if arrival time is above completed time, arrival time is not equal to completed time
        c_time += x.b_time #burst time is added to completed time (essentially arrival time + burst time)
        ta_time = c_time - x.a_time #completed time - arrival time to get turn around time
        w_time = ta_time - x.b_time #turn around time - burst time to give us wait time
        r_time = x.a_time - st - (w_time - ta_time) # calculates response time as the difference between start time and when the process first starts (when it leaves queue)
        print(x)
        print(f"Completion Time is: {c_time:.0f}")
        print(f"Turnaround time is: {ta_time:.0f}")
        print(f"Wait time is: {w_time:.0f}")
        print(f"Response time is: {r_time:.2f}")
        print('''
                
                ''')



    avg_w_time = w_time / len(processes)
    avg_ta_time = ta_time / len(processes)

    return c_time, ta_time, w_time, avg_ta_time, avg_w_time, r_time


if __name__ == "__main__":
    processes = read_inp_file("test1.txt")
    c_time, ta_time, w_time, avg_ta_time, avg_w_time, r_time = sjf_scheduling(processes)
    print('''
    
    ''')
    print(f"Average turnaround time: {avg_ta_time:.2f}")
    print(f"Average wait time: {avg_w_time:.2f}")
