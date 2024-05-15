def is_safe_state(available, maximum, allocation): 
    processes = len(allocation) 
    resources = len(available) 
 
    work = available[:] 
    finish = [False] * processes 
 
    need = [[maximum[i][j] - allocation[i][j] for j in range(resources)] for i 
in range(processes)] 
 
    safe_sequence = [] 
 
    while True: 
        found = False 
        for i in range(processes): 
            if not finish[i]: 
                if all(need[i][j] <= work[j] for j in range(resources)): 
                    found = True 
                    finish[i] = True 
                    for j in range(resources): 
                        work[j] += allocation[i][j] 
                    safe_sequence.append(i) 
                    break 
 
        if not found: 
            break 
 
    return all(finish), safe_sequence 
 
Name: - Yogeshwar Narsing Rekhawar 
Division :- AI&DS-C Roll No. :- 01 PRN No. :- 12110764 
def main(): 
    processes = int(input("Enter the number of processes: ")) 
    print("Number of Processes are:",processes) 
    resources = int(input("Enter the number of resources: ")) 
    print("Number of Resources are:",resources) 
 
    available = [int(x) for x in input("Enter the available resources 
separated by space: ").split()] 
    print("Available resources:", available) 
 
    maximum = [] 
    print("Enter the maximum resource allocation for each process (separated 
by space for each process):") 
    for i in range(processes): 
        max_resources = [int(x) for x in input().split()] 
        maximum.append(max_resources) 
        print("Maximum allocation for process", i + 1, ":", max_resources) 
 
    allocation = [] 
    print("Enter the current resource allocation for each process (separated 
by space for each process):") 
    for i in range(processes): 
        allocation.append([int(x) for x in input().split()]) 
        print("Current resource allocation for Process", i + 1, ":", 
allocation[i]) 
 
    safe, sequence = is_safe_state(available, maximum, allocation) 
    if safe: 
        print("The system is in a safe state.") 
        print("Safe sequence:", sequence) 
    else: 
        print("The system is not in a safe state.") 
 
if __name__ == "__main__": 
    main()
