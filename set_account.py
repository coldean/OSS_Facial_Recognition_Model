#모든 매개변수는 string

import os
from tkinter import *
from tkinter import filedialog

def change_pin(user, pin):
    f = open(user + "/pin.txt", "w")
    f.write(pin)
    f.close()

def read_tasks(user):
    f = open(user + "/tasks.txt", "r")
    l = f.readlines();
    return l

def set_tasks(user, tasks):
    f = open(user + "/tasks.txt", "w")
    for t in tasks:
        f.write(t + "\n")
    f.close()
    return tasks

def add_tasks(user, tasks):
    if os.path.exists(user + "/tasks.txt"):
        list = []
        with open(user + "/tasks.txt") as f:
            for t in tasks:
                if t not in f.read():
                    list.append(t)
                    print(t)
                f.seek(0)
        f.close()
        f = open(user + "/tasks.txt", "a")
        for l in list:
            f.write(l + "\n")
        f.close()

        return list

    else:
        return set_tasks(user, tasks)

def delete_tasks(user, tasks):
    templist = read_tasks(user)
    olist = newline_delete(templist) #리스트의 문자열 요소의 공백문자 제거
    oset = set(olist)
    tset = set(tasks)
    nset = oset - tset
    nlist = list(nset)
    set_tasks(user, nlist)
    return list(tset)

def select_task_file():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/home", title="choose your file",
                                               filetypes=(("txt files", "*.txt"),("all files", "*")))
    root.withdraw()
    sys.stdout.flush()
    return root.filename

def select_task_directory():
    dirname = filedialog.askdirectory()
    sys.stdout.flush()
    return dirname

def newline_delete(list):
    newlist = [tlist.rstrip() for tlist in list]
    return newlist

def select_option(user):
    while True:
        print("\033[34m" + "================= main menu ==================")
        print("select menu")
        print("1. change pin\n2. add tasks\n3. delete tasks\n4. exit")
        print("===================================" + "\033[0m")
        menu = int(input(">> "))

        if menu == 1:
            print("\n---------------- change pin ----------------")
            pin = input("input new pin >> ")
            change_pin(user, pin)
            print("new pin : ", pin)
        elif menu == 2:
            task_list = []
            print("\033[31m" + "\n---------------- add tasks ----------------")
            print("you can add multiple tasks\nselect menu")
            print("1. add task - file\n2. add task - open directory\n3. done" + "\033[0m")
            print("--registered tasks--\n", newline_delete(read_tasks(user)))
            while True:
                add_tasks_num = int(input(">> "))
                if add_tasks_num == 1:
                    task_list.append(select_task_file())
                    print("selected tasks : ", task_list)
                elif add_tasks_num == 2:
                    task_list.append(select_task_directory())
                    print("selected tasks : ", task_list)
                elif add_tasks_num == 3:
                    task_set = set(task_list)
                    task_list = list(task_set)

                    print("added tasks : ",add_tasks(user, task_list))
                    print("whole tasks : ",newline_delete(read_tasks(user)))
                    break;
                else:
                    print("wrong menu\n")

        elif menu == 3:
            if not os.path.exists(user + "/tasks.txt"):
                print("no tasks to delete!")
                continue

            delete_list = []
            print("\033[31m" + "\n---------------- delete tasks ----------------")
            print("you can delete multiple tasks\nselect menu")
            print("1. delete task - file\n2. delete task - directory\n3. done" + "\033[0m")
            print("--registered tasks--\n", newline_delete(read_tasks(user)))
            while True:
                delete_task_num = int(input(">> "))
                if delete_task_num == 1:
                    delete_list.append(select_task_file())
                    print("selected tasks : ", delete_list)
                elif delete_task_num == 2:
                    delete_list.append(select_task_directory())
                    print("selected tasks : ", delete_list)
                elif delete_task_num == 3:
                    delete_set = set(delete_list)
                    delete_list = list(delete_set)
                    print("deleted tasks : ", delete_tasks(user, delete_list))
                    print("whole tasks : ", newline_delete(read_tasks(user)))
                    break;
                else:
                    print("wrong menu\n")

        elif menu == 4:
            break


#만약 오픈할 파일이 .desktop이라면 gtk-launch
#만약 오픈할 파일이 텍스트라면 gedit
select_option("man")