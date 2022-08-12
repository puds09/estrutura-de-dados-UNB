n = int(input())

for i in range(n):
    plan = input()
    schedule = []
    # set the input as a list, goal: use the 'remove' method
    for char in plan:
        schedule.append(char)

    subjects = []
    for j in range(3):
        task_to_do = input()
        subjects.append(task_to_do)

    flag = True
    for j in range(len(subjects)):
        if(flag):
            for char in subjects[j]:
                try: schedule.remove(char)            
                except: 
                    print("You died!")
                    flag = False
                    break 
    if(flag):
        if(len(schedule) == 0):
            print("It's in the box!")
        else:
            seted_list = list(set(schedule))
            seted_list.sort()
            print("Bora ralar: ", end="")
            for char in seted_list:
                print(char, end="")
            print()



