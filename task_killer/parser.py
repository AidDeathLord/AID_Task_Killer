import os
import subprocess


NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


# open file with servers list
def open_server_file():
    check_server_file()
    servers = open('server_list/servers.txt', 'r')
    server_str = servers.readlines()
    result = []
    for i in server_str:
        result.append(i.strip())
    return sorted(result)


# if file does not exist creates it
def check_server_file():
    if not os.path.exists('server_list'):
        os.mkdir('server_list')
    if not os.path.exists('server_list/servers.txt'):
        with open('server_list/servers.txt', 'x'):
            pass


# opens tasks list on remote computer and outputs in the desired format
def get_tasks(server):
    # get tasks in str format
    tasks = subprocess.check_output(f'powershell.exe Get-Process -ComputerName {server} | '
                                    f'Select-Object ProcessName, SI, Id |'
                                    f' Format-Table -hidetableheaders', universal_newlines=True)
    tasks_list = tasks.split()

    # lead information to dict format
    result = []
    index = 0
    while index < len(tasks_list):
        task_dict = dict()
        task_dict['Program'] = tasks_list[index]

        # if there are processes consisting of several words
        # do a check, if the next element is not a number, add it to the previous one
        index += 1
        if tasks_list[index][0] in NUMBERS:
            task_dict['User'] = tasks_list[index]
        else:
            task_dict['Program'] = f"{task_dict.get('Program')} {tasks_list[index]}"
            index += 1
            task_dict['User'] = tasks_list[index]

        index += 1
        task_dict['PID'] = tasks_list[index]

        result.append(task_dict)
        index += 1

    return result


def get_users(server):
    users = subprocess.check_output(f'powershell.exe Get-TerminalSession -ComputerName {server}| '
                                    f'Select-Object Id, UserName |'
                                    f' Format-Table -HideTableHeaders', universal_newlines=True)
    users_list = users.split()

    result = []
    index = 1
    while index < len(users_list) - 1:
        users_dict = dict()
        users_dict['ID'] = users_list[index]

        index += 1
        users_dict['User'] = users_list[index]

        result.append(users_dict)
        index += 1
    return result
