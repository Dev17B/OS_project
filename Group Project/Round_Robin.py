from terminaltables import AsciiTable

class main:
    def data_processor(self, press_start):
        if press_start == ("yes"):
            process_id = []      # Process Number
            a_time = []          # Arrival Time
            b_time = []          # Burst Time / Execution Time
            priority = []        # Priority
            blank_space = []     # Whitespace in .txt files
            raw_dat = []         # Collection of data grouped by process

            r_txt = open(input('Enter .txt file: '),'r')  # Reading the .txt file given
            total_p = r_txt.readline(1)   # Assigning the total number of processes
            n = 0

            # Creating a while loop that iterates through as many lines of text as there are number of processes
            while n < int(total_p):
                # Getting rid of blank space between numbers
                blank_space.append(r_txt.readline())
                # Adding each process number to list, id
                process_id.append(r_txt.readline(1))
                # Getting rid of blank space between numbers
                blank_space.append(r_txt.readline(1))
                # Adding each arrival time to list, a_time
                a_time.append(r_txt.readline(1))
                # Getting rid of blank space between numbers
                blank_space.append(r_txt.readline(1))
                # Adding each burst time to list, b_time
                b_time.append(r_txt.readline(1))
                # Getting rid of blank space between numbers
                blank_space.append(r_txt.readline(1))
                # Adding each priority number to list, priority
                priority.append(r_txt.readline(1))
                n = n + 1
                i = 0
            while i < int(total_p):
                raw_dat.append([int(process_id[i]),int(a_time[i]), int(b_time[i]), 0, int(b_time[i])])
                i = i + 1
            quantum_time = int(input('How long should each proccess run for: ')) # Quantum Time
            main.round_robin(self, total_p, raw_dat, quantum_time, process_id, a_time, b_time)

        
    def round_robin(self, total_p, raw_dat, quantum_time, process_id, a_time, b_time):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        raw_dat.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        while 1:
            normal_queue = []
            temp = []
            for i in range(len(raw_dat)):
                if raw_dat[i][1] <= s_time and raw_dat[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if raw_dat[i][0] == ready_queue[k][0]:
                                present = 1
                    '''
                    The above if loop checks that the next process is not a part of ready_queue
                    '''
                    if present == 0:
                        temp.extend([raw_dat[i][0], raw_dat[i][1], raw_dat[i][2], raw_dat[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    '''
                    The above if loop adds a process to the ready_queue only if it is not already present in it
                    '''
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                    '''
                    The above if loop makes sure that the recently executed process is appended at the end of ready_queue
                    '''
                elif raw_dat[i][3] == 0:
                    temp.extend([raw_dat[i][0], raw_dat[i][1], raw_dat[i][2], raw_dat[i][4]])
                    normal_queue.append(temp)
                    temp = []

            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break

            if len(ready_queue) != 0:
                if ready_queue[0][2] > quantum_time:
                    '''
                    If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    '''
                    start_time.append(s_time)
                    s_time = s_time + quantum_time
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(raw_dat)):
                        if raw_dat[j][0] == ready_queue[0][0]:
                            break
                    raw_dat[j][2] = raw_dat[j][2] - quantum_time
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= quantum_time:
                    '''
                    If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    '''
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(raw_dat)):
                        if raw_dat[j][0] == ready_queue[0][0]:
                            break
                    raw_dat[j][2] = 0
                    raw_dat[j][3] = 1
                    raw_dat[j].append(e_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                if normal_queue[0][2] > quantum_time:
                    '''
                    If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    '''
                    start_time.append(s_time)
                    s_time = s_time + quantum_time
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(raw_dat)):
                        if raw_dat[j][0] == normal_queue[0][0]:
                            break
                    raw_dat[j][2] = raw_dat[j][2] - quantum_time
                elif normal_queue[0][2] <= quantum_time:
                    '''
                    If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    '''
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(raw_dat)):
                        if raw_dat[j][0] == normal_queue[0][0]:
                            break
                    raw_dat[j][2] = 0
                    raw_dat[j][3] = 1
                    raw_dat[j].append(e_time)
        turning_time = main.turn_around_time(self, raw_dat, a_time)
        waiting_time = main.wait_time(self, turning_time, b_time)
        main.results(self, total_p, raw_dat, process_id, a_time, b_time, turning_time, waiting_time)
        main.Round_Robin_Algorithm(self, raw_dat, turning_time, waiting_time)
 

    def turn_around_time(self, raw_dat, a_time):
        t_time = []
        i = 0
        while i < len(a_time):
            t_time.append((raw_dat[i][5]) - (int(a_time[int(i)])))
            i = i + 1
        return t_time

    def wait_time(self, turning_time, b_time):
        w_time = []
        i = 0
        while i < len(b_time):
            w_time.append((turning_time[i])-int(b_time[i]))
            i = i + 1
        return w_time

    def results(self, total_p, raw_dat, process_id, a_time, b_time, turning_time, waiting_time):
        legend = ['Process ID', 'Arrival Time', 'Burst Time', 'Completion Time', 'Turn-Around Time', 'Waiting Time']
        i = 0
        data = [legend]
        while i < int(total_p):
            data.append([process_id[i], a_time[i], b_time[i], raw_dat[i][5] ,turning_time[i], waiting_time[i]])
            i = i + 1
        table = AsciiTable(data)
        print(table.table)

        total_turn_around_time = 0
        for num in turning_time:
            total_turn_around_time += num
        avg_turn_around_time = total_turn_around_time / int(len(turning_time))
        print('Average Turn-Around Time: ', avg_turn_around_time) # Average turn around time

        total_wait_time = 0
        for num in waiting_time:
            total_wait_time += num
        avg_wait_time = total_wait_time / int(len(waiting_time))
        print('Average Wait Time: ', avg_wait_time) # Average Wait time
        # process id | arrival time | burst time | execution time | turn around time | wait time |
    
    def Round_Robin_Algorithm(self, raw_dat, turning_time, waiting_time):
        # Completion Time, Turn-Around Time and Wait time will change depending on which Algorithm
        Round_Robin_Completion_time = []
        Round_Robin_TurnAround_time = []
        Round_Robin_Wait_time = []
        i = 0
        while i < len(turning_time):
                Round_Robin_Completion_time.append(int(raw_dat[i][5]))
                Round_Robin_TurnAround_time.append(turning_time[i])
                Round_Robin_Wait_time.append(waiting_time[i])
                i = i + 1
        print("\nRound Robin Completion times: ", Round_Robin_Completion_time, "\nRound Robin Turn-Around times: ", Round_Robin_TurnAround_time, "\nRound Robin Wait times: ",Round_Robin_Wait_time)


if __name__ == "__main__":
    press_start = input('Would you like to begin: ')
    Round_Robin = main()
    Round_Robin.data_processor(press_start)